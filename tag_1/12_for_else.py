"""
for-else:
wenn eine Schleife NICHT mit break abgebrochen wurde,
dann führe else aus
"""
values = ["aa", "ba", "ca", "dd"]

# Ziel: Ausgeben, ob ein Element (ba) gefunden wurde, und wenn nein,
# dem User eine Meldung ausgeben (ba wurde nicht gefunden)

found = False
for value in values:
    if value == "ba":
        print("ba wurden gefunden!")
        found = True
        break

if not found:
    print("ba wurde nicht gefuden")


# pythonische Variante: else
for value in values:
    if value == "ba":
        print("ba wurden gefunden!")
        break
else:
    print("ba wurde nicht gefunden")