# colorsh
Simple python3 module and cli script for text colorization and decoration in shell.

## Overview example
As a python3 module:
```python
>>> print(Colorsh.decorate("TEXT", enc="ansi", fg=Color("red"), style=Style("bold"))
\0331;38;5;9mTEXT0m

>>> print(Colorsh.decorate("TEXT", enc="tmux", fg=Color("red"), style=Style("bold"))
#[fg=colour9,bold]TEXT
```

As a cli script:
```shell
$ echo -e 'TEXT' | colorsh-cli -e ansi -f red -s bold
\0331;38;5;9mTEXT0m
```

## Installation
In cloned directory of this repo:
```shell
pip3 install .
```

## Module usage
Colorsh exposes just one function:
```python
Colorsh.decorate(msg, enc, fg, bg, style))
```

As an encoding (_enc_) pass string - it can be either "ansi" or "tmux".

As a foreground or background color (_fg_, _bg_) pass *Color* object. *Color* can be created from
0-255 integer value, string (e. g. "red") or colorsh.Term16 enum element (e. g. Term16.red).
Available string names are the same as defined in colorsh.Term16 enum.

As a style (_style_) pass *Style* object. *Style* can be created from list of strings (e. g.
["bold", "faint"]) or list of colorsh.Styles enum elements.

## Script usage
Just pipe desired string to `colorsh-cli` with flags -e (--encoding), -f (--fg), -b (--bg) and -s 
(--style). Style is an array and multiple args are passed as: `-s bold faint`.

