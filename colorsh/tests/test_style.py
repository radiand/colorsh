import unittest
from colorsh import Style, Styles

class TestColorsh(unittest.TestCase):
    def test_parse_from_int_in_range(self):
        s = Style(1)
        self.assertEqual(s.styles[0].name, "bold")
        self.assertEqual(s.styles[0].value, 1)

    def test_parse_from_int_not_in_range(self):
        s = Style(1984)
        self.assertEqual(s.styles, [])

    def test_parse_from_string_in_range(self):
        s = Style("bold")
        self.assertEqual(s.styles[0].name, "bold")
        self.assertEqual(s.styles[0].value, 1)

    def test_parse_from_string_not_in_range(self):
        s = Style("damnNiceStyleButNotSupported")
        self.assertEqual(s.styles, [])

    def test_parse_from_styles_enum(self):
        s = Style(Styles.bold)
        self.assertEqual(s.styles[0].name, "bold")
        self.assertEqual(s.styles[0].value, 1)

    def test_parse_from_uniform_list(self):
        s = Style(["bold", "faint"])
        self.assertEqual(s.styles[0].name, "bold")
        self.assertEqual(s.styles[0].value, 1)
        self.assertEqual(s.styles[1].name, "faint")
        self.assertEqual(s.styles[1].value, 2)

    def test_parse_from_not_uniform_list(self):
        s = Style([1, "faint", Styles.italics])
        self.assertEqual(s.styles[0].name, "bold")
        self.assertEqual(s.styles[0].value, 1)
        self.assertEqual(s.styles[1].name, "faint")
        self.assertEqual(s.styles[1].value, 2)
        self.assertEqual(s.styles[2].name, "italics")
        self.assertEqual(s.styles[2].value, 3)

    def test_parse_from_not_uniform_list_with_another_list_inside(self):
        s = Style([1, ["faint", Styles.italics]])
        self.assertEqual(s.styles[0].name, "bold")
        self.assertEqual(s.styles[0].value, 1)
        self.assertEqual(s.styles[1].name, "faint")
        self.assertEqual(s.styles[1].value, 2)
        self.assertEqual(s.styles[2].name, "italics")
        self.assertEqual(s.styles[2].value, 3)
