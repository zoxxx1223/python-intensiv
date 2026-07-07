"""
Dict Methoden
"""

from collections import Counter

persons = {
    "bob": {
        "age": 34,
        "hobbies": ("Coden", "Fantasy"),
        "profession": {
            "title": "dev",
            "gehalt": 4399,
        },
    }
}
print(
    "Gehalt von bob:",
    persons["bob"]["profession"]["gehalt"],
)

# persons.get("bobb", {}).get("profession", {}).get("gehalt")

population = {
    "Berlin": 3_748_148,
    "Hamburg": 1_822_445,
    "München": 1_471_508,
    "Cologne": 1_085_664,
    "Frankfurt": 753_056,
}

# über die keys iterieren
for key in population:
    print(key, population.get(key))

# über die Values iterieen: liefert Memory-View auf das original dict
population_values = population.values()
print(population_values)
for pop in population.values():
    print("pop=", pop)

# über Key Value Paare iterieren
for key, value in population.items():
    print(f"{key=} {value=}")


# Aufgabe: Wordcounter
# Tip: leeres dict, sentence split, dann iterativ prüfen,
# ob Wort im Dict enthalten,
# wenn ja +1, wenn nein 1
sentence = "the brown fox jumps over the lazy fox fox fox over"

words = {}

# WORD COUNTER
for word in sentence.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
print(words)

# Word Counter mit get()
d = {}
for char in sentence:
    value = d.get(char, 0) + 1
    d[char] = value

# mit Counter die Frequenz zählen
# from collections import Counter
c = Counter(sentence.split())
print(c)


# mit zip und dict ein Dict erstellen
names = ["Bob", "Alice"]
ages = [24, 12]
d = dict(zip(names, ages))
print(d)
