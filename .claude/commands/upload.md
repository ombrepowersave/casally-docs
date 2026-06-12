---
description: 把当前新文档 git 保存、提交并推送到 origin/main（当天合并进单个「日常更新」commit）
argument-hint: "[可选：自定义提交说明，追加在日常更新标题后]"
allowed-tools: Bash(git status:*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Bash(git log:*), Bash(git diff:*), Bash(date:*)
---

# upload — 保存并推送文档

把工作区里新增/改动的文档提交并推送到 `origin/main`。本仓库是简单文档库，遵循约定：
**同一天的文档合并进单个「日常更新」commit**，通过 amend + 强推维持每天一个提交。

## 执行步骤

1. 查看当前状态，确认有可提交的改动：
   - 运行 `git status --short`。若工作区干净（无改动），告知用户"没有新文档需要提交"并停止。

2. 暂存所有改动（含未跟踪的新文件）：
   - 运行 `git add -A`。

3. 计算今天日期：`date +%F`（得到 `YYYY-MM-DD`）。今天的标准提交标题为：
   `docs: 日常更新 <YYYY-MM-DD>`
   - 如果用户传入了 `$ARGUMENTS`，把它作为补充说明拼到标题后，例如：
     `docs: 日常更新 <YYYY-MM-DD> — $ARGUMENTS`

4. 判断 HEAD 是否已是「今天的日常更新」commit：
   - 运行 `git log -1 --pretty=%s` 取得 HEAD 的提交标题。
   - **若 HEAD 标题以 `docs: 日常更新 <今天日期>` 开头**（即今天已经提交过）：
     - 用 amend 把本次改动并入今天的提交：`git commit --amend -m "<今天的标题>"`
     - 因为改写了已推送的历史，用安全强推：`git push --force-with-lease origin main`
   - **否则（今天还没有日常更新 commit）**：
     - 新建提交：`git commit -m "<今天的标题>"`
     - 普通推送：`git push origin main`

5. 报告结果：简要列出本次提交涉及的文件（`git show --stat --oneline HEAD`），并确认已推送到 `origin/main`。

## 注意

- 强推仅用于「改写当天自己的日常更新 commit」这一受控场景，符合本库约定，不要对其他历史强推。
- 若 `git push` 因远端有新提交而被拒绝，先停下来告知用户，不要盲目用 `--force` 覆盖。
- 提交信息统一用中文标题前缀 `docs:`，与现有历史保持一致。
