"""
Der Datentyp Tuple (unveränderlich)
"""

# Tuple definieren
leeres_tuple = ()
x = 1, 2
y = (1, 2)
z = (1,)  # Tuple mit einem Element
print("z:", type(z))

# Tuple Unpacking: oder allgemeiner Sequenz-Unpacking
values = (1, 2, 3)

# oldschool
a = values[0]
b = values[1]
c = values[2]

# pythonisch
a, b, c = values

*x, y = values
print("*x, y:", x, y)

# ad-hoc  Entpacken von Tupeln in einer Iteration
for index, value in enumerate(range(3), start=10):
    print(index, value)

# Entpacken von Rückgabe-Tupeln in a, b
a, b = divmod(5, 2)

# Entpacken von Strings
x, y, *stringliste = "hallo welt"
print(x, y, ",".join(stringliste))
