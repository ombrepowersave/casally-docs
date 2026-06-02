# interview-summarizer 技能 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 创建本项目专用技能 `interview-summarizer`，按访谈主题把 `interviews/` 下的 `.txt` 逐字稿提炼成结构化中文 `.md` 摘要，并规整文件命名。

**Architecture:** 方案 2——`SKILL.md` 管主流程与主题映射，`references/*.md` 每个主题一份提炼维度（含通用兜底 `generic.md`），`scripts/scan.py` 负责确定性的"找未处理文件 + 解析文件名日期"。`scan.py` 用 TDD 开发；其余为内容文件。

**Tech Stack:** Markdown 技能文件、Python 3.9（标准库 `re`/`pathlib`/`argparse`，无第三方依赖）、pytest（仅测试 scan.py）。

---

## File Structure

```
.claude/skills/interview-summarizer/
├── SKILL.md                  # 主流程、主题映射表、跳过/重做、命名规则
├── scripts/
│   ├── scan.py               # find_unprocessed() + parse_date_from_filename() + CLI
│   └── test_scan.py          # pytest 测试
└── references/
    ├── pain-point.md
    ├── demo-feedback.md
    ├── energy-expert.md
    ├── hardware.md
    └── generic.md
```

每个文件单一职责：`scan.py` 只做文件发现与日期解析（不读正文、不判断主题、不重命名——这些由运行技能的 Claude 完成）。

---

## Task 1: scan.py — 解析文件名中的日期

**Files:**
- Create: `.claude/skills/interview-summarizer/scripts/scan.py`
- Test: `.claude/skills/interview-summarizer/scripts/test_scan.py`

- [ ] **Step 1: 写失败测试**

创建 `.claude/skills/interview-summarizer/scripts/test_scan.py`：

```python
import scan


def test_parses_yyyymmdd_embedded_in_parentheses():
    assert scan.parse_date_from_filename("Harry Jackson（Span员工20260524）.txt") == "2026-05-24"


def test_parses_yyyymmdd_with_surrounding_spaces():
    assert scan.parse_date_from_filename("10. Kingshuk Roy 20260203.txt") == "2026-02-03"


def test_returns_none_when_no_date():
    assert scan.parse_date_from_filename("1-Amos Elberg.txt") is None


def test_ignores_recording_timestamp_like_numbers():
    # 00:13:26 这类录音时间戳不是日期，也不构成 8 位 YYYYMMDD
    assert scan.parse_date_from_filename("Interview 001326 notes.txt") is None


def test_rejects_invalid_month_or_day():
    assert scan.parse_date_from_filename("foo 20261345.txt") is None
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd .claude/skills/interview-summarizer/scripts && python3 -m pytest test_scan.py -v`
Expected: FAIL，`ModuleNotFoundError: No module named 'scan'` 或 `AttributeError`。

- [ ] **Step 3: 写最小实现**

创建 `.claude/skills/interview-summarizer/scripts/scan.py`：

```python
"""扫描访谈目录：找出未处理的 .txt，并从文件名解析访谈日期。

只负责确定性逻辑。主题识别、内容提炼、最终重命名由运行技能的 Claude 完成。
"""
import re
from pathlib import Path

# 匹配 8 位 YYYYMMDD，YYYY 限定 20xx，避免误命中无关数字
_DATE_RE = re.compile(r"(20\d{2})(\d{2})(\d{2})")


def parse_date_from_filename(name):
    """从文件名解析日期，返回 'YYYY-MM-DD'；解析不到或非法返回 None。"""
    for y, m, d in _DATE_RE.findall(name):
        month, day = int(m), int(d)
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"{y}-{m}-{d}"
    return None
```

- [ ] **Step 4: 运行测试确认通过**

Run: `cd .claude/skills/interview-summarizer/scripts && python3 -m pytest test_scan.py -v`
Expected: 5 passed。

- [ ] **Step 5: 提交**

```bash
git add .claude/skills/interview-summarizer/scripts/scan.py .claude/skills/interview-summarizer/scripts/test_scan.py
git commit -m "feat(skill): add filename date parser for interview-summarizer"
```

---

## Task 2: scan.py — 找出未处理的 .txt

判定规则：一份 `.txt` 若**没有同名 `.md` 兄弟文件**，即视为未处理。（处理后 `.txt` 与 `.md` 会被规整成同一基名，故已处理的会被自动跳过。）

**Files:**
- Modify: `.claude/skills/interview-summarizer/scripts/scan.py`
- Test: `.claude/skills/interview-summarizer/scripts/test_scan.py`

- [ ] **Step 1: 追加失败测试**

在 `test_scan.py` 末尾追加：

```python
def test_find_unprocessed_lists_txt_without_md_sibling(tmp_path):
    (tmp_path / "a.txt").write_text("x")
    (tmp_path / "b.txt").write_text("x")
    (tmp_path / "b.md").write_text("done")  # b 已处理
    result = scan.find_unprocessed(tmp_path)
    names = sorted(p.name for p in result)
    assert names == ["a.txt"]


def test_find_unprocessed_recurses_subdirs(tmp_path):
    sub = tmp_path / "s1-pain-point-interviews"
    sub.mkdir()
    (sub / "c.txt").write_text("x")
    result = scan.find_unprocessed(tmp_path)
    assert [p.name for p in result] == ["c.txt"]


def test_find_unprocessed_accepts_single_file(tmp_path):
    f = tmp_path / "a.txt"
    f.write_text("x")
    # 单文件：无论是否已有 .md，都返回它自身（单文件强制重做）
    (tmp_path / "a.md").write_text("done")
    result = scan.find_unprocessed(f)
    assert [p.name for p in result] == ["a.txt"]
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd .claude/skills/interview-summarizer/scripts && python3 -m pytest test_scan.py -v`
Expected: 新增 3 个测试 FAIL（`AttributeError: module 'scan' has no attribute 'find_unprocessed'`）。

- [ ] **Step 3: 写实现**

在 `scan.py` 末尾追加：

```python
def find_unprocessed(path):
    """返回待处理 .txt 列表（Path）。

    - path 为单个 .txt：返回 [path]（单文件强制重做，忽略是否已有 .md）。
    - path 为目录：递归找出所有没有同名 .md 兄弟的 .txt。
    """
    path = Path(path)
    if path.is_file():
        return [path]
    result = []
    for txt in sorted(path.rglob("*.txt")):
        if not txt.with_suffix(".md").exists():
            result.append(txt)
    return result
```

- [ ] **Step 4: 运行测试确认通过**

Run: `cd .claude/skills/interview-summarizer/scripts && python3 -m pytest test_scan.py -v`
Expected: 8 passed。

- [ ] **Step 5: 提交**

```bash
git add .claude/skills/interview-summarizer/scripts/scan.py .claude/skills/interview-summarizer/scripts/test_scan.py
git commit -m "feat(skill): add find_unprocessed scanner"
```

---

## Task 3: scan.py — CLI 封装

让技能能直接 `python3 scan.py <path>`，输出每份待处理文件及其解析出的日期，供 Claude 后续命名。

**Files:**
- Modify: `.claude/skills/interview-summarizer/scripts/scan.py`
- Test: `.claude/skills/interview-summarizer/scripts/test_scan.py`

- [ ] **Step 1: 追加失败测试**

在 `test_scan.py` 末尾追加：

```python
import json
import subprocess
import sys
from pathlib import Path


def test_cli_outputs_json_lines(tmp_path):
    (tmp_path / "Foo 20260203.txt").write_text("x")
    (tmp_path / "Bar.txt").write_text("x")
    script = Path(__file__).parent / "scan.py"
    out = subprocess.check_output([sys.executable, str(script), str(tmp_path)], text=True)
    rows = [json.loads(line) for line in out.splitlines() if line.strip()]
    by_name = {Path(r["path"]).name: r["date"] for r in rows}
    assert by_name["Foo 20260203.txt"] == "2026-02-03"
    assert by_name["Bar.txt"] is None
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd .claude/skills/interview-summarizer/scripts && python3 -m pytest test_scan.py::test_cli_outputs_json_lines -v`
Expected: FAIL（无 CLI 输出 / 非 JSON）。

- [ ] **Step 3: 写实现**

在 `scan.py` 末尾追加：

```python
import argparse
import json
import sys


def main(argv=None):
    parser = argparse.ArgumentParser(description="列出待处理访谈 .txt 及解析出的日期")
    parser.add_argument("path", help="单个 .txt 文件、某个目录，或 interviews 根目录")
    args = parser.parse_args(argv)
    for txt in find_unprocessed(args.path):
        row = {"path": str(txt), "date": parse_date_from_filename(txt.name)}
        sys.stdout.write(json.dumps(row, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: 运行全部测试确认通过**

Run: `cd .claude/skills/interview-summarizer/scripts && python3 -m pytest test_scan.py -v`
Expected: 9 passed。

- [ ] **Step 5: 提交**

```bash
git add .claude/skills/interview-summarizer/scripts/scan.py .claude/skills/interview-summarizer/scripts/test_scan.py
git commit -m "feat(skill): add scan.py CLI emitting json lines"
```

---

## Task 4: references/ — 四个主题维度文件

每份内容来自设计文档第 6 节。这些是 Claude 在识别主题后读取的"提炼骨架"。

**Files:**
- Create: `.claude/skills/interview-summarizer/references/pain-point.md`
- Create: `.claude/skills/interview-summarizer/references/demo-feedback.md`
- Create: `.claude/skills/interview-summarizer/references/energy-expert.md`
- Create: `.claude/skills/interview-summarizer/references/hardware.md`

- [ ] **Step 1: 创建 `pain-point.md`**

```markdown
# 提炼维度：用户痛点（pain-point）

这是骨架，不是死模板。读到受访者反复强调、情绪强烈、讲得具体的地方，要顺着往细里拆，宁细勿漏。

## 必提
- **具体痛点清单**：逐条列出，每条写清现象、发生场景、触发原因。
- **痛的程度 / 紧迫性**：引用用户原话里的情绪强度（"crazy""hate""every month"）作为佐证。
- **当前应对 / 替代方案**：用了什么 app、设备、土办法；为什么不够用。
- **未被满足的需求 / 期望**：用户明确或隐含希望产品做到什么。

## 注意
- 访谈者是 Casally 团队成员（提问方），提炼聚焦**受访者**的表达。
- 区分"真痛点"（反复提、有具体代价）与"随口一提"。
```

- [ ] **Step 2: 创建 `demo-feedback.md`**

```markdown
# 提炼维度：Demo 反馈（demo-feedback）

骨架而非死模板。受访者对某个功能反应强烈处（惊喜、困惑、抵触）要展开细写。

## 必提
- **逐功能反应**：对看到的每个功能/界面，分别记喜欢 / 困惑 / 不喜欢及原因。
- **可用性问题 / 卡点**：哪里看不懂、点错、卡住。
- **功能请求 / 改进建议**：受访者主动提出的想要的东西。
- **购买 / 付费意愿信号**：愿不愿付费、价格敏感度、愿付多少、什么条件下会买。

## 注意
- 聚焦受访者反应，而非访谈者的引导话术。
- 留意"嘴上说喜欢但行为/语气犹豫"的不一致信号。
```

- [ ] **Step 3: 创建 `energy-expert.md`**

```markdown
# 提炼维度：专业咨询（energy-expert）

骨架而非死模板。专家讲到的关键判断、反直觉观点要原汁原味记清。

## 必提
- **专业观点 / 行业知识点**：专家给出的事实、判断、经验。
- **对产品方向的专业建议**：建议做什么 / 别做什么及理由。
- **技术 / 政策 / 术语**：提到的电价结构、净计量(NEM)、储能、TOU、关税补贴等，简要解释。

## 注意
- 区分"已被验证的事实"与"专家的个人推测"。
- 保留关键数字、单位、政策名称的准确原文。
```

- [ ] **Step 4: 创建 `hardware.md`**

```markdown
# 提炼维度：硬件（hardware）

骨架而非死模板。受访者对设备的具体型号、痛点、集成需求要细写。

## 必提
- **硬件相关需求 / 约束**：对接什么设备、协议、安装/兼容限制。
- **设备情况**：太阳能、EV、电池(Powerwall 等)、温控/HVAC、智能电表、Span 面板等的具体型号与使用现状。

## 注意
- 保留品牌/型号原文（如 Tesla Powerwall、Span panel）。
- 记清设备之间如何协同、当前痛在哪。
```

- [ ] **Step 5: 提交**

```bash
git add .claude/skills/interview-summarizer/references/pain-point.md \
        .claude/skills/interview-summarizer/references/demo-feedback.md \
        .claude/skills/interview-summarizer/references/energy-expert.md \
        .claude/skills/interview-summarizer/references/hardware.md
git commit -m "docs(skill): add four theme dimension references"
```

---

## Task 5: references/generic.md — 通用兜底

**Files:**
- Create: `.claude/skills/interview-summarizer/references/generic.md`

- [ ] **Step 1: 创建 `generic.md`**

```markdown
# 提炼维度：通用兜底（generic）

当目录与内容都无法判定为已知主题时使用。

## 做法
- 先从内容里识别这场访谈实际围绕的主线/目的，一句话写明。
- 按主线自适应展开提炼，不必套固定子标题，但要覆盖：
  - 受访者关心/反复强调的核心点（顺着往细拆，宁细勿漏）。
  - 具体事实、场景、数字、设备、原话佐证。
  - 对产品的任何启示（需求、建议、机会、风险）。

## 注意
- 聚焦受访者，访谈者为 Casally 团队提问方。
- 宁可结构略松，也不要漏掉受访者真正重视的信息。
```

- [ ] **Step 2: 提交**

```bash
git add .claude/skills/interview-summarizer/references/generic.md
git commit -m "docs(skill): add generic fallback reference"
```

---

## Task 6: SKILL.md — 主流程

技能入口。包含 frontmatter（name/description）、主流程、主题映射表、跳过/重做规则、命名规则、摘要模板。

**Files:**
- Create: `.claude/skills/interview-summarizer/SKILL.md`

- [ ] **Step 1: 创建 `SKILL.md`**

````markdown
---
name: interview-summarizer
description: 把本项目 interviews/ 目录下的访谈逐字稿(.txt)按主题提炼成结构化中文摘要(.md)，并规整文件命名。当用户要"总结/提炼访谈""处理 interviews 目录""把逐字稿整理进知识库/gbrain"，或指定某个访谈文件要总结时，使用本技能。涉及 Casally 用户访谈、痛点访谈、demo 反馈、能源专家咨询、硬件访谈的整理归档都适用。
---

# Interview Summarizer

把 `interviews/` 下的访谈逐字稿 `.txt` 按主题提炼成结构化中文 `.md` 摘要，并把文件名规整为 `YYYY-MM-DD-访谈人-主题`。下游知识库 gbrain 只读 `.md`、忽略 `.txt`，所以摘要必须是 `.md`，原稿保持 `.txt`。

## 处理范围（三选一）
- **单文件**：用户指定某个 `.txt` → 只处理它，且**强制重做**（即使已有同名 `.md` 也覆盖）。
- **单目录**：某个 `sX-xxx/` → 处理其中所有**未处理**的 `.txt`。
- **全部**：整个 `interviews/` → 处理所有目录里**未处理**的 `.txt`。

"未处理"= 该 `.txt` 没有同名 `.md` 兄弟文件。

## 步骤

### 1. 列出待处理文件
运行扫描脚本（输出每行一个 JSON：`{"path","date"}`，date 解析自文件名，解析不到为 null）：
```bash
python3 .claude/skills/interview-summarizer/scripts/scan.py "<文件或目录路径>"
```
单目录/全部：脚本已自动跳过有同名 `.md` 的。单文件：直接处理该文件。

### 2. 逐份处理
对每个待处理 `.txt`：

**a) 识别主题**——先按所在目录前缀查映射表，再读正文确认/校正；都不匹配用 `generic`。

| 目录前缀 | 主题 | reference | slug |
|---|---|---|---|
| `s1-pain-point-interviews` | 用户痛点 | references/pain-point.md | `pain-point` |
| `s2-demo-1.0` / `s3-demo-2.0` | Demo 反馈 | references/demo-feedback.md | `demo` |
| `s4-Energy expert...` | 专业咨询 | references/energy-expert.md | `energy-expert` |
| `s5-Hardware1.0` | 硬件 | references/hardware.md | `hardware` |
| （无法判定） | 未知 | references/generic.md | `generic` |

> 目录是初判，正文为准：若内容明显不符目录主题，以内容为准并相应改 slug。

**b) 读对应 reference**，按其维度提炼。reference 是骨架不是死模板——顺着受访者重点强调处往细拆，宁细勿漏。

**c) 写摘要**，中文为主，英文金句保留原句，用下面模板：

```markdown
# [访谈人] · [主题] · [日期或"日期未知"]

## 受访者画像
背景、住房/家庭/地区；如有：太阳能/EV/电池/温控/Span 面板等设备情况。

## 主题判定
判定为 X 主题，依据：……

## 核心提炼
（按该主题 reference 的维度展开，受访者重点处往细拆）

## 关键金句
- "original English quote" —— [说话人]

## 行动项 / 机会点
- ……
```

**d) 确定规整文件名**：`YYYY-MM-DD-访谈人-slug`
- 日期取脚本解析结果；为 null 则省略日期段，变 `访谈人-slug`。
- 访谈人取受访者本名（多为英文，如 `Amos Elberg`）；去掉原名里的序号前缀("1-")和括号备注("（Span员工）")，这类身份信息写进摘要正文。
- slug 用上表的英文 slug。
- 例：`Harry Jackson（Span员工20260524）.txt` → 基名 `2026-05-24-Harry Jackson-hardware`。

**e) 写文件并改名**（`.txt` 与 `.md` 共用同一基名，保留在原目录）：
```bash
# 用 git mv 重命名原 txt，再写同名 md（示意）
git mv "<原 txt 路径>" "<同目录>/<基名>.txt"
# 然后把摘要写入 "<同目录>/<基名>.md"
```
单文件重做时若已存在 `.md`，直接覆盖写。

### 3. 报告
处理完后简述：共处理几份、跳过几份、各自规整成什么名、主题分布。

## 扩展（新增主题）
出现新访谈系列时：在 `references/` 加一个 `<新主题>.md`（照现有格式写维度），并在上面映射表加一行。主流程无需改动。无法归类的仍走 `generic`。
````

- [ ] **Step 2: 校验 frontmatter 可被解析**

Run: `python3 -c "import re,sys; t=open('.claude/skills/interview-summarizer/SKILL.md').read(); m=re.match(r'^---\n(.*?)\n---', t, re.S); print('OK' if m and 'name: interview-summarizer' in m.group(1) and 'description:' in m.group(1) else 'BAD')"`
Expected: `OK`

- [ ] **Step 3: 提交**

```bash
git add .claude/skills/interview-summarizer/SKILL.md
git commit -m "feat(skill): add interview-summarizer SKILL.md main workflow"
```

---

## Task 7: 端到端冒烟测试（真实文件）

用一份真实访谈验证整条链路（不污染仓库——在副本上试，验证后清理或保留）。

**Files:**
- 临时：复制一份真实 `.txt` 到 `/tmp` 做演练

- [ ] **Step 1: 跑扫描脚本看输出**

Run: `python3 .claude/skills/interview-summarizer/scripts/scan.py "interviews/s5-Hardware1.0"`
Expected: 输出若干 JSON 行，含 `path` 与解析出的 `date`（如 `Harry Jackson（Span员工20260524）.txt` 对应 `2026-05-24`）。

- [ ] **Step 2: 手动走一遍单文件流程（演练，不改原仓库）**

把一份真实文件复制到 tmp，按 SKILL.md 步骤：识别主题 → 读 reference → 生成一份摘要 `.md` 到 `/tmp`。

Run:
```bash
mkdir -p /tmp/iv-smoke && cp "interviews/s5-Hardware1.0/Harry Jackson（Span员工20260524）.txt" /tmp/iv-smoke/
python3 .claude/skills/interview-summarizer/scripts/scan.py /tmp/iv-smoke
```
然后由执行者按 SKILL.md 生成 `/tmp/iv-smoke/2026-05-24-Harry Jackson-hardware.md`。

- [ ] **Step 3: 人工检查摘要质量**

确认：中文为主、英文金句保留原句、维度齐全且对受访者重点有细化、文件名格式正确、`.md`/`.txt` 同基名。如不满意，回到对应 reference 或 SKILL.md 调整后重跑。

- [ ] **Step 4: 清理临时文件**

Run: `rm -rf /tmp/iv-smoke`

- [ ] **Step 5: 全量测试回归**

Run: `cd .claude/skills/interview-summarizer/scripts && python3 -m pytest test_scan.py -v`
Expected: 9 passed。

（本任务无代码改动则无需提交；若过程中改了 reference/SKILL.md，按改动内容提交。）

---

## Self-Review

- **Spec 覆盖**：范围三粒度(Task6) ✓；跳过/重做(Task2+Task6) ✓；目录→内容主题识别(Task6) ✓；四主题+generic 维度(Task4/5) ✓；中文为主+英文金句(Task6 模板) ✓；命名 YYYY-MM-DD-访谈人-主题 + 缺日期省略(Task1+Task6) ✓；.txt/.md 同名(Task6) ✓；易更新(Task6 扩展段) ✓；scan 脚本(Task1-3) ✓。
- **占位符**：无 TBD/TODO；所有代码与命令均完整给出。
- **类型/接口一致**：`parse_date_from_filename(name)->str|None`、`find_unprocessed(path)->list[Path]`、`main(argv=None)` 在 Task1-3 及 SKILL.md 调用处用法一致；slug 集合 `pain-point/demo/energy-expert/hardware/generic` 在映射表与命名步骤一致。
