from pyagnostics.source import InMemorySource
from pyagnostics.spans import SourceId, SourceSpan


def test_read_span_with_context_lines() -> None:
    source = InMemorySource("aaa\n  bbb\nccc\n", name="example")
    source_id = SourceId()
    span = SourceSpan(6, 9, source_id=source_id)
    expected_column = 2
    expected_line_count = 2

    contents = source.read_span(span, context_lines_before=1, context_lines_after=1)

    assert contents.text.plain == "aaa\n  bbb\nccc\n"
    assert contents.span == SourceSpan(0, len(contents.text.plain), source_id=source_id)
    assert contents.line == 1
    assert contents.column == expected_column
    assert contents.line_count == expected_line_count
    assert contents.name == "example"
