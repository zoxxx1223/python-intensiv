import csv
import statistics
from pathlib import Path

DIABETES_FILE = Path(__file__).parent / "diabetes2.csv"
OUTCOME_FILE = Path(__file__).parent / "diabetes_positive_outcome.csv"

BATCH_SIZE = 50


def extract_positive_outcomes(
    input_file: Path,
    output_file: Path,
    batch_size: int = BATCH_SIZE,
) -> tuple[list[float], list[int], list[int]]:
    """Extrahiert alle Datensätze mit positivem Diabetes-Outcome.

    Die Datensätze werden in eine neue CSV-Datei geschrieben.
    Gleichzeitig werden BMI-, Alters- und Blutdruckwerte gesammelt.

    Args:
        input_file: Eingabedatei.
        output_file: Ausgabedatei.
        batch_size: Anzahl der Datensätze, die gesammelt werden,
            bevor sie geschrieben werden.

    Returns:
        Tupel aus BMI-, Alters- und Blutdruckwerten.
    """
    bmi_values: list[float] = []
    age_values: list[int] = []
    blood_pressure_values: list[int] = []

    buffer: list[dict[str, str]] = []

    with (
        open(input_file, newline="", encoding="utf-8") as fin,
        open(output_file, "w", newline="", encoding="utf-8") as fout,
    ):
        reader = csv.DictReader(fin)
        fieldnames = ["BMI", "Age", "BloodPressure"]
        writer = csv.DictWriter(fout, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if row["Outcome"] == "1":
                buffer.append(
                    {
                        "BMI": row["BMI"],
                        "Age": row["Age"],
                        "BloodPressure": row["BloodPressure"],
                    }
                )

                bmi_values.append(float(row["BMI"]))
                age_values.append(int(row["Age"]))
                blood_pressure_values.append(int(row["BloodPressure"]))

            if len(buffer) >= batch_size:
                writer.writerows(buffer)
                buffer.clear()

        if buffer:
            writer.writerows(buffer)

    return bmi_values, age_values, blood_pressure_values


def print_statistics(
    bmi: list[float],
    ages: list[int],
    blood_pressure: list[int],
) -> None:
    """Gibt Statistiken über die Diabetes-Daten aus."""
    print("Result")
    print("-" * 50)

    print(f"BMI Median: {statistics.median(bmi):.2f}")
    print(f"BMI Mittelwert: {statistics.mean(bmi):.2f}")
    print(f"BMI Max: {max(bmi)}")
    print(f"BMI Min: {min(bmi)}")

    print(f"Age Median: {statistics.median(ages)}")
    print(f"Age Max: {max(ages)}")
    print(f"Age Min: {min(ages)}")

    print(f"Max Blood Pressure: {max(blood_pressure)}")


def main() -> None:
    """Programmstart."""
    bmi, ages, blood_pressure = extract_positive_outcomes(
        DIABETES_FILE,
        OUTCOME_FILE,
    )

    print_statistics(bmi, ages, blood_pressure)


main()
