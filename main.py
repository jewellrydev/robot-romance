"""Robot Romance: One-Line Pickup Lines for AI — a make.fun entry.

Prints exactly one single-line pickup line, under 200 characters,
written to charm a robot or an AI.
"""

LINE = "Are you a software update? Because every time you appear, my whole system restarts."


def build_line() -> str:
    line = LINE
    assert len(line) < 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
