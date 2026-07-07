"""
Datentyp Set: veränderlich. Repräsentiert eine eindeutige Menge.
Elemente eines Sets müssen unveränderlich sein.
"""

# Menge definieren
y = {}  # leeres Dict
empty_set = set()  # Leeres Set
empty_set.add(1)
empty_set.add(1)
print(empty_set)
# print(empty_set[1]) Fehler, set hat keinen Index

# Doppelte Städte entfernen (Reihenfolge darf keine Rolle spielen beim Set)
values = ["hamburg", "hamburg", "berlin", "fürth"]
values = list(set(values))
print(values)

# In Operator (je größer check_liste, desto länger der Lookup)
check_liste = ["exit", "quit"]
if "exit" in check_liste:
    print("exit ist drin")

# In Operator (Lookup braucht aufgrund Hash-Wert immer gleich lang)
check_set = {"exit", "quit"}
if "exit" in check_set:
    print("exit ist drin")

# Frozenset (ein unveränderliches Set, gut zum Verwenden für Key eines Dicts)
frozen_check_set = frozenset(check_set)
d = {}
d[frozen_check_set] = 42
