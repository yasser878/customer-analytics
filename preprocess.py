import sys
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

file_path = sys.argv[1]

columns = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race",
    "gender", "capital_gain", "capital_loss",
    "hours_per_week", "native_country", "income"
]

df = pd.read_csv(file_path, names=columns, skipinitialspace=True)

# replace ? with null so we can then drop them, then we remove duplicates if found, then bn encode categorical columns, ba3daha n3ml scale lel hagat el numerical, then n3ml drop lel columns el malhash lazma, then n3ml discretization lel hagat zay el age tkoun young middle old

df.replace("?", pd.NA, inplace=True)

df.dropna(inplace=True)

df.drop_duplicates(inplace=True)

categorical_cols = [
    "workclass", "education", "marital_status",
    "occupation", "relationship", "race",
    "gender", "native_country", "income"
]

le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

scaler = StandardScaler()
numeric_cols = [
    "age", "education_num", "capital_gain",
    "capital_loss", "hours_per_week"
]

df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

df.drop(columns=["fnlwgt"], inplace=True)

df["age_group"] = pd.cut(
    df["age"],
    bins=3,
    labels=["young", "middle", "old"]
)

df.to_csv("data_preprocessed.csv", index=False)

print("Preprocess done")


os.system("python analytics.py data_preprocessed.csv")