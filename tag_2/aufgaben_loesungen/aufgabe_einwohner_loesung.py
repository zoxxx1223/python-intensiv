populations = {
    "Minas Tirith": 1854000,
    "Edoras": 274000,
    "Hobbingen": 132000,
    "Bruchtal": 486000,
    "Dale": 821000,
}


def convert_to_millions(population: dict) -> dict:
    population_mil = {}

    for city, inhabitants in population.items():
        population_mil[city] = inhabitants / 1_000_000

    return population_mil


populations_mil = convert_to_millions(populations)

for city, inhabitants in populations_mil.items():
    city_type = "Großstadt" if inhabitants >= 1 else "Kleinstadt"
    print(f"{city} hat {inhabitants:.1f} Mio. Einwohner ({city_type})")
