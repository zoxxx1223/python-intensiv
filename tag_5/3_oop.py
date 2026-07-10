"""
Mini-Aufgabe: Eine Klasse City (population, name, bundesland)
berlin = City(....)
print(berlin) # Berlin in <Bundesland>
berlin.add_people(n=3) # zählt Population hoch

City
"""


class City:
    def __init__(self, population: int, name: str, bundesland: str) -> None:
        self.name = name
        self.population = population
        self.bundesland = bundesland

    def add_people(self, n=3) -> None:
        """Bevölkerungszahl hochzählen."""
        self.population += n

    def __str__(self) -> str:
        return f"{self.name} in {self.bundesland}"


berlin = City(3434343, "Berlin", "Berlin")
# man braucht PER DEFAULT keine Getter und Setter
berlin.name = "Berlini"
print(berlin.name)
berlin.population = -1  # das sollte per getter und setter geregelt werden
