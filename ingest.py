import sys
import pandas as pd
import os

file_path = sys.argv[1]

df = pd.read_csv(file_path)

df.to_csv("data_raw.csv", index=False)

print("Ingest done")

os.system("python preprocess.py data_raw.csv")