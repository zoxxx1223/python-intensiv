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


print("*" * 40)

# Aufgabe: Gruppieren von Personen in 3-Personen-Gruppen 
import random
people = ["a", "b", "c", "d", "e", "f", "g", "h"]
random.shuffle(people)
groups = []
MAX_GROUP = 3

for i in range(0, len(people), MAX_GROUP):
    groups.append(
        people[i: MAX_GROUP + i]
    )

print(groups)