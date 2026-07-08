"""
Der Funktions-Docstrings
"""


def berechne(a: int, b: int) -> int:
    """Die 1. Zeile ist die Summary Line.

    Eine vertiefte Beschreibung der Funktion
    bla blabb.

    Args:
        a: die Breite der Fläche
        b: die Länge der Fläche

    Returns:
        die Fläche
    """
    return a * b


print("Der Docstring der Funktion:", berechne.__doc__)
