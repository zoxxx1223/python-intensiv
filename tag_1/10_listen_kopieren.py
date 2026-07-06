""" 
Listen kopieren.
Bei Zuweisung oder Übergabe an Funktionen wird nur die Referenz kopiert!!!

Jedes Objekt in Python hat eine Identität

Shallow Kopie: es wird eine flache Kopie erstellt
Tiefe Kopie: erstellt rekursiv eine echte Kopie der Ursprungsliste
"""
from copy import deepcopy

values = [[1], 2, 3]
copy_values = values # Referenz wird kopiert
shallow_copy_values = values.copy()  # values[:]
deep_copy_values = deepcopy(values)

values[0][0] = 99
print("shallow:", shallow_copy_values) # [[99], 2, 3]
print("deep:", deep_copy_values) # [[1], 2, 3]

print("Identität von values:", id(values))
print("Identität von values:", id(copy_values))
print("Identität von shallow_copy_values:", id(shallow_copy_values))

