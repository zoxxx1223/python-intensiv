"""
yield => ernten
"""

from typing import NamedTuple, Generator
from pathlib import Path


class DataPoint(NamedTuple):
    x: float
    y: float
    z: float


def reader(file) -> Generator:
    for line in file:
        cols = line.strip().split(",")
        cols = [float(v) for v in cols]
        yield DataPoint(*cols)  # cols[0], cols[1], cols[2]


def file_reader(filename: str) -> None:
    with open(Path(__file__).parent / filename) as f:
        # über das ERgebnis des Generators iterieren
        for dp in reader(f):
            print(dp)


file_reader("datapoints.csv")
