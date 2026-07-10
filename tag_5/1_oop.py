"""
Einführung in OOP in Python
"""


class Person:
    def __init__(self, name: str, job: str):
        # Alle Attribute eines Objekts sollten hier angelget werden
        self.name = name
        self.job = job
        self.last_sickday = None


bob = Person(name="bob", job="dev")  # Instanziierung (Objekte)
alice = Person(name="Alice", job="admin")

print(bob is alice)  # id(bob) == Id(alice): False
print(isinstance(bob, Person))

print("Die Eigenschaften von Person:", dir(bob))
# bob + alice

# Dynamisch Attribute einem Objekt zuordnen (bad practice)
bob.age = 43
print(f"{bob.name=}", bob.age)

print(bob)  # String-Repräsentation des Bob-Objekts
print([1, 2, 3])  # STring-Repräsentation der Liste
