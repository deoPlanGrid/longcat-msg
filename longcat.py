import string
from random import choice

import click

LONGCAT_NUMBER = {
    "0": ":long-cat-zero:",
    "1": ":long-cat-one:",
    "2": ":long-cat-two:",
    "3": ":long-cat-three:",
    "4": ":long-cat-four:",
    "5": ":long-cat-five:",
    "6": ":long-cat-six:",
    "7": ":long-cat-seven:",
    "8": ":long-cat-eight:",
    "9": ":long-cat-nine:",
}

LONGCAT_OTHER = {
    "!": ":long-cat-bang:",
    "|": ":long-cat-pipe:",
    "+": ":long-cat-plus:",
    ":": ":long-cat-colon:",
    ",": ":long-cat-comma:",
    "#": ":long-cat-pound:",
    "~": ":long-cat-tilde:",
    "$": ":long-cat-dollar:",
    "=": ":long-cat-equals:",
    "-": ":long-cat-hyphen:",
    ".": ":long-cat-period:",
    "@": ":long-cat-at:",
    "&": ":long-cat-amp:",
    "*": ":long-cat-asterisk:",
    "/": ":long-cat-fwdslash:",
    "<": ":long-cat-lessthan:",
    ">": ":long-cat-morethan:",
    "?": ":long-cat-question:",
    "(": ":long-cat-openparen:",
    ")": ":long-cat-closeparen:",
    "_": ":long-cat-underscore:",
    "[": ":long-cat-openbracket:",
    "]": ":long-cat-closebracket:",
}

LONGCAT_SPACE = [
    ":long-cat-left-right:",
]

LONGCAT_HEAD = [
    ":long-cat-joy:",
    ":long-cat-lol:",
    ":long-cat-owo:",
    ":long-cat-evil:",
    ":long-cat-blush:",
    ":long-cat-happy:",
    ":long-cat-heart:",
    ":long-cat-peace:",
    ":long-cat-hooray:",
    ":long-cat-salute:",
    ":long-cat-scream:",
    ":long-cat-praying:",
    ":long-cat-hungry-l:",
    ":long-cat-hungry-r:",
    ":long-cat-thumbsup:",
    ":long-cat-unamused:",
    ":long-cat-happyturn:",
    ":long-cat-embarrassed:",
    ":long-cat-exasperated:",
    ":long-cat-arms-crossed:",
]

LONGCAT_TAIL = [
    ":long-cat-tail-stand:",
    ":long-cat-tail-sit:",
    ":long-cat-sploot-tail:",
]


def longcatify(character: str):
    if character in string.ascii_lowercase:
        return f":long-cat-{character}:"
    elif character in string.ascii_uppercase:
        return f":long-cat-big-{character.lower()}:"
    elif character in string.digits:
        return LONGCAT_NUMBER[character]
    elif character in LONGCAT_OTHER:
        return LONGCAT_OTHER[character]
    else:
        return choice(LONGCAT_SPACE)


@click.command()
@click.argument("message", type=str)
def longcat(message):
    print(choice(LONGCAT_TAIL) + 
          "".join([longcatify(character) for character in message]) +
        choice(LONGCAT_HEAD)
    )
    


if __name__ == "__main__":
    longcat()
