"""
Datentyp String (Sequenz => haben eine Länge, und sind per Index-Operator addressierbar)
"""
first_name = "Bob"
print(first_name, type(first_name))
print("LÄnge von bob:", len(first_name) )  # len ruft intern __len__ auf

print("Alle Eigentschaften eines Objetks:", dir(first_name))
print("Zeichen an index 0:", first_name[0])
print("Das letzte Zeichen:", first_name[-1])
# print("Zeichen an index 10:", first_name[10]) # IndexError: string index out of range

other_name = "Bob"
if first_name == other_name:
    print("Firstname und othername sind gleich")

# Umwandeln eines Ints in String
value = str(3)
print("Das ist ein Wert:", value)