"""
Sortieren mit Lambda bzw. Funktionsreferenzen
"""

chars = ["a", "f", "c", "d", "e"]
# chars.sort()  # inplace Sortierung (Timsort)
# print(chars)
print(ord("a"), ord("f"))  # 97 102

sorted_chars = sorted(chars, reverse=False)  # aufsteiend, absteigend
print("Sortieren Chars:", sorted_chars)

print("*" * 50)

chars = ["A", "a", "f", "b", "B", "A", "d", "e"]
# shadow[a, a, f, b, b, a, d, e], el steht für jedes Element der Liste, dass VOR
# der Sortierung modifiziert wird. Es wird defniert, was genau an dem Element eigentlich
# sortiert werden soll
sorted_chars = sorted(chars, key=lambda el: el.lower())
print("Sortieren Chars:", sorted_chars)


def sort_id(el: str) -> str:
    return el[-1]


ids = ["id5", "idx1", "id2", "idy5", "id4", "id3"]
sorted_ids = sorted(ids, key=lambda el: el[-1])
sorted_ids = sorted(ids, key=sort_id)
print("Sorted ids:", sorted_ids)

# Snacks nach Preis aufsteigend sortieren
# [(Skickers, 150), (Milka, 3.30),..]
snacks = {"Milka": 3.30, "Kekse": 5.20, "Snickers": 1.50}
sorted_snacks = dict(sorted(snacks.items(), key=lambda el: el[1]))
print(sorted_snacks)

print("*" * 50)

d = {"price": 3, "value": 42}
print(d["price"], d.get("price"))

# Snacks sortieren nach Preis (und sortieren nach x)
snacks = {
    1: {"name": "Erdnüsse", "price": 200, "amount": 50, "pos": {"x": 10}},
    2: {"name": "Milka", "price": 400, "amount": 20, "pos": {"x": 30}},
    3: {"name": "Snickers", "price": 100, "amount": 10, "pos": {"x": 50}},
}
# shadow list [200, 400, 100] => [100, 200, 400]
sorted_snacks = sorted(snacks.items(), key=lambda el: el[1]["price"])
print(sorted_snacks)
