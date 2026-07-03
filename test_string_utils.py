"""Tests for string_utils, using only the standard library."""

import unittest

from string_utils import slugify, title_case


class TestSlugify(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_collapses_whitespace(self):
        self.assertEqual(slugify("  Multiple   Spaces  "), "multiple-spaces")

    def test_mixed_whitespace(self):
        self.assertEqual(slugify("tab\there\r\nand newline"), "tab-here-and-newline")

    def test_custom_separator(self):
        self.assertEqual(slugify("a b c", separator="_"), "a_b_c")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")

    def test_non_string_raises(self):
        with self.assertRaises(TypeError):
            slugify(123)  # type: ignore[arg-type]


class TestTitleCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(title_case("hello world"), "Hello World")

    def test_extra_whitespace(self):
        self.assertEqual(title_case("  hello   world  "), "Hello World")

    def test_empty_string(self):
        self.assertEqual(title_case(""), "")


if __name__ == "__main__":
    unittest.main()
