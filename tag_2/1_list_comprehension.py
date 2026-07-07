"""
Listen Abstraktion (List Comprehensions)

List Comprehensions erzeugen IMMER eine neue Liste
"""

values = []
for i in range(10):
    values.append(i)


# als list comprehension
values = [i for i in range(10)]  # [0, 1, 2, 3, ....]#


# Negativ-Beispiel: Liste von 10 x None
# [print("hallo") for _ in range(10)]

persons = ["Bob", "Alice", "Grumpy", "Quux"]
# Alle Personen filtern, die mit B anfangen oder py aufhören
new_persons = [p for p in persons if p.startswith("B") or p.endswith("py")]
print(new_persons)

# übungsaufabe: filtere alle Zahlen aus der Liste, die durch 2 teilbar (%)
# und größer als 2 sind
liste = [1, 2, 3, 4, 9, 11, 24, 10, 7]
neue_liste = [l for l in liste if l % 2 == 0 and l > 2]
print(neue_liste)


# Praktischer Beispiel: Userinput und Eingaben splitten und type-casten
ui = "34 24.2 42 23".split()
# print(ui) # ['34', '24.2', '42', '23']

a, b, c, d = [float(i) for i in ui]
print(a, b, c, d)

# Spielkarten (kartesisches Produkt)
colors = ["♠", "♥", "♣", "♦"]
values = ["K", "Q", "A", "J"]

french_deck = [f"{a}{b}" for a in colors for b in values]
print(french_deck)
