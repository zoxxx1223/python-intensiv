"""
Scopes: globale Scope, Funktionsscope, builtin-Scope
"""

MAX_LENGTH = 42
MIN_LENGTH = 1
x = 3  # globale Variable
print(x)


def connect_database(host: str, port: int, values: list[int]) -> bool:
    """mit locals() kann man den lokalen Scope angucken."""
    MAX_LENGTH = 43  # Shadowing (Überschatten einer globalen Variable)
    print("*" * 40)
    print("Globale Variable lesen:", MIN_LENGTH)
    connection = True
    print(locals())
    return connection


my_values = [1, 2, 3]
connection = connect_database("localhost", 6532, my_values)
print(connection)

print(globals())
