import unittest
from colorsh import Colorsh, Color, Encoding, ANSI_ESCAPE_SEQUENCE

class TestColorsh(unittest.TestCase):
    def test_not_decorate_if_no_encoding(self):
        self.assertEqual(
            "example",
            Colorsh.decorate("example"))

        self.assertEqual(
            "example",
            Colorsh.decorate("example", enc=Encoding.none))

    def test_decorate_ansi_color_fg(self):
        self.assertEqual(
            ANSI_ESCAPE_SEQUENCE + "0;38;5;9m" + "example" + ANSI_ESCAPE_SEQUENCE + "0m",
            Colorsh.decorate("example", enc=Encoding.ansi, fg=Color("red")))

    def test_decorate_ansi_color_bg(self):
        self.assertEqual(
            ANSI_ESCAPE_SEQUENCE + "0;48;5;12m" + "example" + ANSI_ESCAPE_SEQUENCE + "0m",
            Colorsh.decorate("example", enc=Encoding.ansi, bg=Color("blue")))

    def test_decorate_ansi_color_fg_bg(self):
        self.assertEqual(
            ANSI_ESCAPE_SEQUENCE + "0;38;5;9;48;5;12m" + "example" + ANSI_ESCAPE_SEQUENCE + "0m",
            Colorsh.decorate("example", enc=Encoding.ansi, fg=Color("red"), bg=Color("blue")))

    def test_decorate_tmux_color_fg(self):
        self.assertEqual(
            "#[fg=colour9]example",
            Colorsh.decorate("example", enc=Encoding.tmux, fg=Color("red")))

    def test_decorate_tmux_color_bg(self):
        self.assertEqual(
            "#[bg=colour12]example",
            Colorsh.decorate("example", enc=Encoding.tmux, bg=Color("blue")))

    def test_decorate_tmux_color_fg_bg(self):
        self.assertEqual(
            "#[fg=colour9,bg=colour12]example",
            Colorsh.decorate("example", enc=Encoding.tmux, fg=Color("red"), bg=Color("blue")))
