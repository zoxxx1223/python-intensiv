"""
Funktionsargumente: postionell und Keywordword-Argumente
"""


def volume(a: int, b: int, c: int = 100) -> int:
    """Berechne das Volumen eines Körpers."""
    print(f"{a=} {b=} {c=}")
    return a * b * c


volume(1, 3, 4)  # 3 positionelle Argumente
volume(5, 6)  # 2 positionelle Argumente und ein Default (100)


def connect_to_database(*, username: str, password: str, database: str) -> None:
    """Verbinde mit Datenbank.
    alles rechts von dem * => muss per Keyword Argument aufgerufen werden"""
    print(username, password, database)


# connect_to_database("bob", "12345geheim", "local")  # per Position
connect_to_database(username="bob", password="12345geheim", database="local")
connect_to_database(password="12345geheim", database="local", username="bob")


def fn(*args, **kwargs):
    """args = eine unbestimmte Anzahl an positionellen Argumenten.
    kwargs = eine unbestimmte Anzahl an Keyword Argumenten."""
    print("args:", args)
    print("kwargs:", kwargs)


fn(234, 3, 24, a=12, b=34, c=34)
max(3, 3, 4, 2, 5, 3, 5, 6)  # Die Funktion max nimmt eine unbegrenzte Anzahl an Args
