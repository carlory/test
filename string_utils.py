"""Small string utilities for the test repo."""


def slugify(text: str, separator: str = "-") -> str:
    """Make a URL-friendly slug from ``text``.

    Lowercases the string, collapses runs of whitespace into a single
    ``separator``, and strips leading/trailing separators.

    >>> slugify("Hello World")
    'hello-world'
    >>> slugify("  Multiple   Spaces  ")
    'multiple-spaces'
    >>> slugify("a b c", separator="_")
    'a_b_c'
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    if not isinstance(separator, str):
        raise TypeError(f"separator must be str, got {type(separator).__name__}")
    return separator.join(text.lower().split())


def title_case(text: str) -> str:
    """Capitalize the first letter of every whitespace-separated word.

    >>> title_case("hello world")
    'Hello World'
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    return " ".join(word.capitalize() for word in text.split())
