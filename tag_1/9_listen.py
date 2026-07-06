"""
Datentyp Liste: Sequenz, veränderlich, heterogen
"""
values = [1, 2, 1.2, "apple", [1, 2]]
backup = values # Backup erstellen (es wird nur die Referenz kopiert)

values[2] = 42 # Zuweisen von Werten an Listen-Index
print(values[2])

# Länge einer Liste
print("Länge von values:", len(values)) # __len__
print("Index von apple:", values.index("apple"))

# Ein Element anhängen
values.append("Cherry")  # inplace
values.insert(0, "Peach")
values.extend(["1", "3"])

new_values = [12, 134]

values += new_values
print(values)

# mit dem In-Operator ürüfen, ob ein Wert enthalten ist.
if "apple" in values:
    print("apple ist in der Liste")

print("*" * 40)
print(values)
print("*" * 40)
print(backup)