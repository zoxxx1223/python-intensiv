"""
Mengen-Operationen (Schnittmenge, prüfen ob Subset, Union)
"""

x = set(list("abcd"))
y = set(list("ade"))
z = set(list("ad"))

# -----------------------------------------------------------
# SCHNITTMENGE: &
# -----------------------------------------------------------
print(f"{x=} {y=}")
result = x & y
print("Schnittmenge von x & y:", result, type(result))

# -----------------------------------------------------------
# Union: |
# -----------------------------------------------------------
print(f"{x=} {y=}")
result = x | y
print("Union von x | y:", result, type(result))

# -----------------------------------------------------------
# ist Subset?  abc < abc
# -----------------------------------------------------------
z = set(list("ade"))
result = z < y  # Echte Untermenge
print(f"ist z eine echte Untermenge von y?: {result}")

result = z <= y  # Untermenge
print(f"ist z eine Untermenge von y?: {result}")

# -----------------------------------------------------------
# Aufgabe
# -----------------------------------------------------------
# Prüfen, ob Listen ein gemeinsames Element haben
alfa = [1, 3, 5, 8]
beta = [99, 3, 22]

# mit Walrus-Operator
if gemeinsame := set(alfa) & set(beta):
    print("ja!", gemeinsame)
