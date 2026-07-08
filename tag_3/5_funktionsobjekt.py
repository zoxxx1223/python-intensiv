"""
Das Funktionsobjekt (Funktionsreferenz)
Funktonale Programmierung: Funktionen sind first class citizens
"""

from typing import Callable


def summe(a, b):
    return a + b


def divison(a, b):
    return a / b


def g(fn: Callable):
    # hier wird die Funktion f aufgerufen
    fn()


def f():
    print("Ich bin f")


print(type(f))  # Objekt der Klasse <class 'function'>
g(f)


###############################################################
# Das folgende Beispiel zeigt die Möglichkeit, Keys auf Funktions-Referenzen
# zu mappen, zb. für einen Taschenrechner

# operations-dict mappt Operatoren auf Funktionen
operations = {
    "+": summe,
    "/": divison,
}

# Auf den Key + zugreifen und die Funtion mit zwei Argumenten aufrufen
operations["+"](3, 4)
