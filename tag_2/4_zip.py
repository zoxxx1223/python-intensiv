"""
zip-Funktion: zwei oder mehr Iterables im Reißverschluss-Verfahren durchlaufen
zip nimmt immer das kürzeste Iterable (im itertools package gibt es zip-longest)
"""

students = ["Bob", "Alice", "Grumpy"]
grades = [1, 2, 4]

for student, grade in zip(students, grades):
    print(student, grade)


"""
(LEICHT)
Gegeben sind zwei Listen:


geraete = ["Kühlschrank", "Fernseher", "Waschmaschine", "Laptop"]
stromverbrauch = ["1.2", "0.3", "2.0", "0.05"]  # Angaben in kWh

Erstelle ein Dict, wobei der Key der Gerätename ist und der Value der entsprechende Verbrauch.
Konvertiere die Werte aus stromverbrauch dazu vorab in floats.

Das neue Dict soll nur Geräte beinhalten, deren Stromverbrauch >= 0.2 kWh

Ergebnis:
{
'Fernseher': 0.3,
 'Kühlschrank': 1.2,
 'Waschmaschine': 2.0
 }

"""
from pprint import pprint

geraete = ["Kühlschrank", "Fernseher", "Waschmaschine", "Laptop"]
stromverbrauch = ["1.2", "0.3", "2.0", "0.05"]  # Angaben in kWh

d = {}
for device, power in zip(geraete, stromverbrauch):
    power = float(power)
    if power >= 0.2:
        d[device] = power

pprint(d, width=1, sort_dicts=False)
