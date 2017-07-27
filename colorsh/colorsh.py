from enum import IntEnum

ANSI_ESCAPE_SEQUENCE = "\033["


class Styles(IntEnum):
    normal = 0
    bold = 1
    faint = 2
    italics = 3
    underline = 4
    slow_blink = 5
    fast_blink = 6


class Term16(IntEnum):
    black = 0
    maroon = 1
    green = 2
    olive = 3
    navy = 4
    purple = 5
    teal = 6
    silver = 7
    grey = 8
    red = 9
    lime = 10
    yellow = 11
    blue = 12
    fuchsia = 13
    aqua = 14
    white = 15


class Color:
    def __init__(self, data=None):
        if type(data) is int:
            self._parse_as_int(data)
        elif type(data) is str:
            self._parse_as_str(data)
        elif type(data) is Term16:
            self._parse_as_enum(data)

    _name = None
    _value = None

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @name.setter
    def name(self, new):
        self._name = new
        enum_member = get_member_with_name(Term16, new)
        self._value = enum_member.value if enum_member is not None else None

    @value.setter
    def value(self, new):
        self._value = new
        enum_member = get_member_with_value(Term16, new)
        self._name = enum_member.name if enum_member is not None else None

    def _parse_as_int(self, item):
        self.value = item if item >= 0 and item <= 255 else None

    def _parse_as_str(self, item):
        try:
            self._parse_as_int(int(item))
        except ValueError:
            if get_member_with_name(Term16, item) is not None:
                self.name = item.lower().strip()

    def _parse_as_enum(self, item):
        self._name = item.name
        self._value = item.value

class Style:
    def dispatch(self, data):
        if type(data) is int:
            self._parse_as_int(data)
        elif type(data) is str:
            self._parse_as_str(data)
        elif type(data) is list:
            self._parse_as_list(data)
        elif type(data) is Styles:
            self._parse_as_enum(data)

    def __init__(self, data=None):
        self._styles = []
        if data is None:
            return
        else:
            self.dispatch(data)

    def __getitem__(self, key):
        return self._styles[key]

    @property
    def styles(self):
        return self._styles

    def _parse_as_int(self, item):
        found = get_member_with_value(Styles, item)
        if found is not None:
            self._styles.append(found)

    def _parse_as_str(self, item):
        found = get_member_with_name(Styles, item)
        if found is not None:
            self._styles.append(found)

    def _parse_as_enum(self, item):
        self._styles.append(item)

    def _parse_as_list(self, item):
        for it in item:
            self.dispatch(it)


def get_member_with_name(enumerator, name):
    for nm, member in enumerator.__members__.items():
        if nm == name.lower().strip():
            return member
    return None

def get_member_with_value(enumerator, value):
    for va, member in enumerator.__members__.items():
        if member.value == value:
            return member
    return None


class Colorsh:
    def _build_ansi(msg, fg, bg, style):
        # build formatting
        if style.styles:
            stl = style[0].value
        else:
            stl = Styles.normal.value

        # build fg color
        if type(fg) is Color and fg.value is not None:
            fg = ";38;5;{}".format(fg.value)
        else:
            fg = ""

        # build bg color
        if type(bg) is Color and bg.value is not None:
            bg = ";48;5;{}".format(bg.value)
        else:
            bg = ""

        return "{0}{1}{2}{3}m{4}{5}0m".format(
            ANSI_ESCAPE_SEQUENCE, stl, fg, bg, msg, ANSI_ESCAPE_SEQUENCE)

    def _build_tmux(msg, fg, bg, style):
        # build fg
        fgs = []
        if type(fg) is Color and fg.value is not None:
            fgs.append("colour{}".format(fg.value))

        for s in style:
            fgs.append(s.name)

        # build bg
        bgs = []
        if type(bg) is Color and bg.value is not None:
            bgs.append("colour{}".format(bg.value))

        return "#[{0}{1}{2}]{3}".format(
            "fg=" + ",".join(fgs) if fgs else "",
            "," if fgs and bgs else "",
            "bg=" + ",".join(bgs) if bgs else "",
            msg)


    @staticmethod
    def decorate(msg, enc=None, fg=None, bg=None, style=Style([])):
        if enc is None or not (fg or bg or style):
            return msg

        enc = enc.lower().strip()

        if enc == "ansi":
            return Colorsh._build_ansi(msg, fg, bg, style)
        if enc == "tmux":
            return Colorsh._build_tmux(msg, fg, bg, style)

    @staticmethod
    def ansi(msg, fg=None, bg=None, style=Style([])):
        return Colorsh.decorate(msg, "ansi", fg, bg, style)

    @staticmethod
    def tmux(msg, fg=None, bg=None, style=Style([])):
        return Colorsh.decorate(msg, "tmux", fg, bg, style)

