from enum import IntEnum

ANSI_ESCAPE_SEQUENCE = "\033["


class Encoding(IntEnum):
    none = 0
    ansi = 1
    tmux = 2


class Formatting(IntEnum):
    normal = 0
    bold = 1
    faint = 2
    italics = 3
    underline = 4
    slow_blink = 5
    fast_blink = 6


class Term8Color(IntEnum):
    fg_normal = 30
    bg_normal = 40
    fg_bright = 90
    bg_bright = 100


class Term8(IntEnum):
    black = 0
    red = 1
    green = 2
    yellow = 3
    blue = 4
    magenta = 5
    cyan = 6
    white = 7


def map_enum(enumerator, name):
    for n, member in enumerator.__members__.items():
        return member if n == name.lower().strip() else None


class Colorsh:
    def _is_proper_numeric(value):
        return True if type(value) is int and value >= 0 and value <= 255 else False

    def _build_ansi(msg, fg, bg, formatting):
        # build formatting
        if formatting:
            fmt = formatting[0].value
        else:
            fmt = Formatting.normal.value

        # build fg color
        if type(fg) is Term8:
            fg = ";{}".format(Term8Color.fg_normal.value + fg.value)
        elif Colorsh._is_proper_numeric(fg):
            fg = ";38;5;{}".format(fg)
        else:
            fg = ""

        # build bg color
        if type(bg) is Term8:
            bg = ";{}".format(Term8Color.fg_normal.value + bg.value)
        elif Colorsh._is_proper_numeric(bg):
            bg = ";48;5;{}".format(bg)
        else:
            bg = ""

        return "{0}{1}{2}{3}m{4}{5}0m".format(
            ANSI_ESCAPE_SEQUENCE, fmt, fg, bg, msg, ANSI_ESCAPE_SEQUENCE)

    def _build_tmux(msg, fg, bg, formatting):
        # build fg
        fgs = []
        if Colorsh._is_proper_numeric(fg):
            fgs.append("colour{}".format(fg))
        for fmt in formatting:
            fgs.append(fmt.name)

        # build bg
        bgs = []
        if Colorsh._is_proper_numeric(bg):
            bgs.append("colour{}".format(bg))

        return "#[{0}{1}]".format(
            "fg=" + ",".join(fgs) if fgs else "",
            "bg=" + ",".join(bgs) if bgs else "")


    @staticmethod
    def decorate(msg, enc=Encoding.none, fg=None, bg=None, formatting=[]):
        if enc is Encoding.none or not (fg or bg or formatting):
            return msg

        if enc is Encoding.ansi:
            return Colorsh._build_ansi(msg, fg, bg, formatting)
        if enc is Encoding.tmux:
            return Colorsh._build_tmux(msg, fg, bg, formatting)

    @staticmethod
    def ansi(msg, fg=None, bg=None, formatting=[]):
        return Colorsh.decorate(msg, Encoding.ansi, fg, bg, formatting)

    @staticmethod
    def tmux(msg, fg=None, bg=None, formatting=[]):
        return Colorsh.decorate(msg, Encoding.ansi, fg, bg, formatting)

