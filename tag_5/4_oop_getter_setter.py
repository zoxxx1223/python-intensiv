"""
Getter und Setter
"""


class City:
    def __init__(self, population: int, name: str, bundesland: str) -> None:
        self.name = name
        self.population = population
        self.bundesland = bundesland

    @property
    def population(self) -> int:
        return self._population

    @population.setter
    def population(self, n):
        if n < 0:
            raise ValueError("Die Anzahl an Personen in einer Stadt muss positiv sein.")
        self._population = n

    def add_people(self, n=3) -> None:
        """Bevölkerungszahl hochzählen."""
        self.population += n

    def __str__(self) -> str:
        return f"{self.name} in {self.bundesland}"


class BigCity(City):
    def __init__(
        self, population: int, name: str, bundesland: str, crimerate: int
    ) -> None:
        super().__init__(population, name, bundesland)
        self.crimerate = crimerate


berlin = City(3, "a", "b")
ny = BigCity(23, "aa", "bb", 343)
# Angucken, was für Attribute ein Objekt hat
print(vars(berlin), berlin.__dict__)
# berlin.set_population(-1)
berlin.name = "sadjflkasdjflökasdj"
berlin.population = 2
# berlin.set_population(-1)
