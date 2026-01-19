import re

from rich.console import Console
from rich.text import Text

from pyagnostics.report import LabeledSourceBlock
from pyagnostics.spans import LabeledSpan, SourceSpan


def test_labeled_source_block_preserves_whitespace() -> None:
    console = Console(width=80, record=True)
    block = LabeledSourceBlock(Text("a  b\nc"))

    console.print(block)
    output = console.export_text()

    assert "a  b" in output


def test_labeled_source_block_wraps_with_line_numbers() -> None:
    width = 20
    content = "A" * 60
    label_span = SourceSpan(55, 60)
    console = Console(width=width, record=True)
    block = LabeledSourceBlock(
        Text(content),
        labels=[LabeledSpan(label_span, "tail")],
    )

    console.print(block)
    output_lines = console.export_text().splitlines()

    line_number_lines = [
        line for line in output_lines if re.match(r"^\\s*\\d+ \\| ", line)
    ]

    assert len(line_number_lines) > 1


def test_labeled_source_block_renders_label_on_wrapped_line() -> None:
    width = 20
    content = "A" * 60
    label_span = SourceSpan(55, 60)
    console = Console(width=width, record=True)
    block = LabeledSourceBlock(
        Text(content),
        labels=[LabeledSpan(label_span, "tail")],
    )

    console.print(block)
    output = console.export_text()

    assert "tail" in output
