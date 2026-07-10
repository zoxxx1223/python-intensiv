"""
String Repräsentation und Methoden

Dunder-Methoden: Double Under: interne Methoden von Python

__str__: Informelle String-Repräsentation eines Objekts für Endnutzer
__repr__: Formelle String-Repräsentation eines Objekts für Debugging
"""


class Person:
    def __init__(self, name: str, job: str):
        self.name = name
        self.job = job

    def do_work(self) -> None:
        print(f"{self.name} should work...")

    def __len__(self) -> int:
        return 42

    def __str__(self) -> str:
        """String-Repräsentation eines Objekts."""
        return self.name

    def __repr__(self) -> str:
        """Formelle Repräsentation zeigt Instanzzierung."""
        return f"Person({repr(self.name)}, {repr(self.job)})"


bob = Person("Bob", "admin")
print(bob)  # ruft __str__() auf
str(bob)  # ruft __str__() auf
len(bob)  # ruft __len__() auf
print("Repr von Bob:", repr(bob))  # ruft __repr__ auf

bob.do_work()
