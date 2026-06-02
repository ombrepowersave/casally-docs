import scan


def test_parses_yyyymmdd_embedded_in_parentheses():
    assert scan.parse_date_from_filename("Harry Jackson（Span员工20260524）.txt") == "2026-05-24"


def test_parses_yyyymmdd_with_surrounding_spaces():
    assert scan.parse_date_from_filename("10. Kingshuk Roy 20260203.txt") == "2026-02-03"


def test_returns_none_when_no_date():
    assert scan.parse_date_from_filename("1-Amos Elberg.txt") is None


def test_ignores_recording_timestamp_like_numbers():
    assert scan.parse_date_from_filename("Interview 001326 notes.txt") is None


def test_rejects_invalid_month_or_day():
    assert scan.parse_date_from_filename("foo 20261345.txt") is None


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
