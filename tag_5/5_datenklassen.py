"""
Datenklassen (dataclasses)
- simplifizieren den Code
"""

from __future__ import annotations

from dataclasses import dataclass, field
from logging_config import setup_logging

setup_logging()


@dataclass(order=True)
class GameCard:
    rank: str
    suit: str = field(compare=False)

    def fn(self):
        return self.rank


class RegularGameCard:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"RegularGameCard({repr(self.rank)}, {repr(self.suit)})"


dataclass_card = GameCard("3", "♡")
print(dataclass_card)

c1 = GameCard("A", "♠")
c2 = GameCard("K", "♠")
c3 = GameCard("A", "♠")

print("c1 == c3", c1 == c3)
print("c1 < c2", c1 < c2)  # lexikograpischer Vergleich von rank
print("c1 > c2", c1 > c2)  # lexikograpischer Vergleich von rank


@dataclass
class Vector3D:
    x: int
    y: int
    z: int

    def __add__(self, other: object) -> Vector3D:
        if not isinstance(other, Vector3D):
            return NotImplemented

        return Vector3D(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )


u = Vector3D(1, 2, 3)
v = Vector3D(11, 22, 33)

# via __add__ haben wir den + Operator für Vector3D überladen
z = u + v
print(z)
