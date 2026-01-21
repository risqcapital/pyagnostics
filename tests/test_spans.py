from pyagnostics.spans import SourceId


def test_source_id_is_unique() -> None:
    first = SourceId()
    second = SourceId()
    assert first != second
    assert first.value != second.value


def test_source_id_from_value() -> None:
    expected_value = 42
    source_id = SourceId.from_value(expected_value)
    assert source_id.value == expected_value
