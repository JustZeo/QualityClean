from pathlib import Path

import qualityclean as qc

CURRENT_DIR = Path(__file__).parent
CSV_PATH = CURRENT_DIR / "dataset.csv"

df = qc.load(CSV_PATH)

print(df)
print(type(df))