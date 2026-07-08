"""
Einführung in Funktionen:
Schreibweise von Funktionsnamen: snake case

Typehints: seit 3.9
(Typ-Vorschläge, Meta-Informationen, die zur Laufzeit nicht berücksichtigt werden)

In Produktiv-Code sollte das Tool "Mypy" auf der CLI genutzt werden.

int, float, str, list, list[int]
"""


def summe(a: int, b: int) -> int:
    return a + b


result = summe(2, 4)
print("REsult von summe:", result)

result = summe("3", "4")
print("REsult von summe:", result)
