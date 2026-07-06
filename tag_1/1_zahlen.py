"""
Python Integer und arithmetische Operatoren

Arithmetische Operatoren

x + y   Summe von x und y
x - y   Differenz von x und y
x * y   Produkt von x und y
x / y   Quotient von x und y
x // y  abgerundeter Quotient von x und y* (floor division)
x % y   Rest beim Teilen von x durch y*
+x  positives Vorzeichen
-x  negatives Vorzeichen
x ** y  x hoch y

Operatoren Precedence (Rangfolge)
https://docs.python.org/3/reference/expressions.html#operator-precedence


Weitere nützliche builtin Funktionen:
- `sum()`: Summiert alle Werte in einer Sequenz.
- `min()`: Gibt den kleinsten Wert einer Sequenz zurück.
- `max()`: Gibt den größten Wert einer Sequenz zurück.
"""
# Konvention: nur eine Konvention in Python
MAX_DISTANCE = 1000


distance_1 = 100
print("Datentyp von distance_1:", type(distance_1)) # <class 'int'>
print("Wert von distance_1:", distance_1)

# Divisions-Operator / => erzeugt immer ein Float
result = 4 / 2
print("4/2: ", result, type(result))

# Floor-Division
result = 8 // 3
result_mod = 8 % 3
print("8 // 3:", result, type(result), "es bleibt übrig:", result_mod)

# Floor-Division (unterscheid sich im negativen Bereich, da richtung negativ unendlich abgerundet wird )
result = -8 // 3
print("-8 // 3:", result, type(result))

# Potenz-Operator
x = 2
print("x**2:", x**2)


"""
Aufgabe:
Eine Halle ist 16 Meter lang. Ein Baumstamm ist 4 Meter lang.

Berechne, wie viele Baumstämme der Länge nach in die Halle passen
und wie viele Meter übrig bleiben.

Nutze Konstanten und Variablen.

Beispiel:
Es passen in die Halle: 4 Baumstämme
Es sind noch 0 Meter übrig.
"""