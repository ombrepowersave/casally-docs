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
