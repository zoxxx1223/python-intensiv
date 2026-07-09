# einfache Lösung ohne List-Comprehension und DictReader

import csv
from pathlib import Path


def load_cities(filename: str, country=None) -> tuple[list, list]:
    """Load Cities from CSV File and return list."""
    city_rows = []
    with open(Path(__file__).parent / filename, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader)  # Rückt den Iterator eins weiter
        for row in reader:
            # Country Filter
            if country and isinstance(country, str):
                if row[4].lower() == country.lower():
                    city_rows.append(row)
                continue

            city_rows.append(row)
    return city_rows, header


def sort_cities_by_ascii_name(city_rows: list) -> list:
    """Sort cities by column ascii_name."""
    return sorted(city_rows, key=lambda e: e[1])


def save_cities_to_file(filename: str, city_rows: list, header: list) -> None:
    """Save rows to file."""
    with open(Path(__file__).parent / filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header)
        writer.writerows(city_rows)


def main() -> None:
    """Programmstart."""
    file_in = "world_cities.csv"

    country = input("Land: ").strip()
    file_out = f"world_cities_sorted_{country.replace(' ', '_').lower()}.csv"

    city_rows, header = load_cities(file_in, country=country)
    sorted_cities = sort_cities_by_ascii_name(city_rows)
    print(f"Sorted {len(sorted_cities)} Städte")
    save_cities_to_file(file_out, sorted_cities, header)

    print(f"{len(sorted_cities)} Städte aus {country} gespeichert.")


main()
