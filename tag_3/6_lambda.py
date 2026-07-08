"""
Lambda Ausdrücke: anonyme Funktionen
("Wegwerf-Funktionen")

Lambda Ausdruck erzeugt eine Funktionsreferenz

lambda Parameter1, Parameter2,... : Parameter1 + Parameter2 ...
"""


def f(a, b):
    return a + b


# als lambda
fn = lambda a, b: a + b
print("Result von fn:", fn(3, 4))
