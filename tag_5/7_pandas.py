import pandas as pd
import numpy as np
from pathlib import Path

v = np.array([1, 2, 3, 4]).astype(np.int8)
u = np.array([1, 2, 3, 4]).astype(np.int8)
print(v, v.dtype)
z = u + v
print(z)

m = np.array([[1, 2, 3], [2, 3, 4]])
print("transponierte Matrix m:\n", m.T)

###############################
volcanos = pd.read_csv(Path(__file__).parent / "volcanos.csv")
print(volcanos)
print(volcanos.head(3))

filtered_df = volcanos[(volcanos["Country"] == "Italy") & (volcanos["risk"] >= 3)]
print(filtered_df.head(20))
