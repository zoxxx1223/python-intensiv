"""
Range-Objekt: [START:END:STEP]
"""
for i in range(1, 10):
    print(i)


cities = ["HH", "B", "N", "FÜ"]
for i in range(len(cities)):
    print(cities[i])

# von 2 - 18 in Schrittweite 4 (20 ist exclusive)
for i in range(2, 20, 4):
    print(i)


# Aufgabe: Gruppieren von Personen in 3-Personen-Gruppen 
import random
people = ["a", "b", "c", "d", "e", "f", "g", "h"]
random.shuffle(people)
groups = []

# for ....:
#     print("....") # a b c d e f, g h