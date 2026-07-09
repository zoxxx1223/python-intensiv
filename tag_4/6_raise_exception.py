"""
Exceptions auslösen
[1, 2, 3, ]
("bob", 2, "hamburg")
"""

from typing import NamedTuple
import traceback


class Hero(NamedTuple):
    name: str
    level: int


class InvalidLevelException(Exception):
    """Eigene Exceptions erben immer von Exception."""

    pass


def create_character(name: str, level: int) -> Hero:
    # Wenn Aufgabe nicht erfüllt werden kann, wird eine eigene Exception erhoben
    if level < 1:
        raise InvalidLevelException("Der Level darf nicht < 1 sein!")

    return Hero(name=name, level=level)


held1 = create_character(name="Bob", level=1)
print(isinstance(held1, tuple))
print(held1.name, held1.level)

try:
    held1 = create_character(name="Bob", level=0)
except InvalidLevelException as e:
    print(f"Der Held konnte nicht erstellt werden: {e}")
    traceback.print_exc()
    # print(e.__traceback__.tb_lineno)

# "xxx".find("y")
