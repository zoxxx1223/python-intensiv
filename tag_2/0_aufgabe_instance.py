""" 
built funktionen: isinstance
"""
x = 1.1

if isinstance(x, (int, float)):
    print("x ist ein int")

# Aufgabe: gegeben ist eine Liste mit Werten
# und soll gefiltert werden nach int. ERgebnist ist eine Liste von int

values = [1, 3, "3", 3.3, [3, 2], 3]
new_values = []

for value in values:
    if isinstance(value, int):
        new_values.append(value)