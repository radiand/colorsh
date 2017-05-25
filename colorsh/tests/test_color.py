import unittest
from colorsh import Color, Term16

class TestColor(unittest.TestCase):
    def test_parse_from_string_in_term16_range(self):
        c = Color("black")
        self.assertEqual(c.name, "black")
        self.assertEqual(c.value, 0)

        c = Color("white")
        self.assertEqual(c.name, "white")
        self.assertEqual(c.value, 15)

    def test_parse_from_string_not_in_term16_range(self):
        c = Color("toopretty")
        self.assertEqual(c.name, None)
        self.assertEqual(c.value, None)

    def test_parse_from_string_is_case_insensitive(self):
        c = Color("blue")
        self.assertEqual(c.name, "blue")
        self.assertEqual(c.value, 12)

        c = Color("BLUE")
        self.assertEqual(c.name, "blue")
        self.assertEqual(c.value, 12)

        c = Color("Blue")
        self.assertEqual(c.name, "blue")
        self.assertEqual(c.value, 12)

    def test_parse_from_string_is_whitespace_resilient(self):
        c = Color("\tyellow\r\n           ")
        self.assertEqual(c.name, "yellow")
        self.assertEqual(c.value, 11)

    def test_parse_from_int_in_8bit_range(self):
        c = Color(10)
        self.assertEqual(c.name, "lime")
        self.assertEqual(c.value, 10)

        c = Color(240)
        self.assertEqual(c.name, None)
        self.assertEqual(c.value, 240)

    def test_parse_from_int_not_in_8bit_range(self):
        c = Color(1984)
        self.assertEqual(c.name, None)
        self.assertEqual(c.value, None)

    def test_parse_from_invalid_type(self):
        c = Color(float(1337.0))
        self.assertEqual(c.name, None)
        self.assertEqual(c.value, None)

    def test_parse_from_term16(self):
        c = Color(Term16.red)
        self.assertEqual(c.name, "red")
        self.assertEqual(c.value, 9)

    def test_setting_name_also_sets_value(self):
        c = Color()
        c.name = "red"
        self.assertEqual(c.name, "red")
        self.assertEqual(c.value, 9)

    def test_setting_value_also_sets_name(self):
        c = Color()
        c.value = 9
        self.assertEqual(c.name, "red")
        self.assertEqual(c.value, 9)


if __name__ == '__main__':
    unittest.main()

