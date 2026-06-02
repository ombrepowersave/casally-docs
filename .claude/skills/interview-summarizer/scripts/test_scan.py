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
