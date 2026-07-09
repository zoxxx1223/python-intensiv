import csv
import json
from pathlib import Path

FILE_IN = Path("active_volcanos.csv")
FILE_OUT = Path("volcanos.json")


def load_volcanos(csv_file: Path, country: str) -> list[dict[str, str]]:
    """Lädt alle Vulkane eines Landes mit bekanntem Risikowert.

    Args:
        csv_file: Pfad zur CSV-Datei.
        country: Land, nach dem gefiltert werden soll.

    Returns:
        Liste mit den gefilterten Vulkanen.
    """
    volcanos: list[dict[str, str]] = []

    with open(csv_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Country"] == country and row["risk"] != "NULL":
                volcanos.append(
                    {
                        "name": row["V_Name"],
                        "latitude": row["Latitude"],
                        "longitude": row["Longitude"],
                        "risk": row["risk"],
                        "country": row["Country"],
                        "region": row["Region"],
                    }
                )

    return volcanos


def save_json(data: list[dict[str, str]], json_file: Path) -> None:
    """Speichert eine Liste von Vulkanen als JSON-Datei.

    Args:
        data: Zu speichernde Daten.
        json_file: Zieldatei.
    """
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_json(json_file: Path) -> list[dict[str, str]]:
    """Lädt Vulkan-Daten aus einer JSON-Datei.

    Args:
        json_file: Pfad zur JSON-Datei.

    Returns:
        Liste der Vulkan-Datensätze.
    """
    with open(json_file, encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    """Programmstart."""
    volcanos = load_volcanos(FILE_IN, "Germany")
    save_json(volcanos, FILE_OUT)

    data = load_json(FILE_OUT)
    print(data)


main()
