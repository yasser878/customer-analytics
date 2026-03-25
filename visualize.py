import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = sys.argv[1]

columns = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race",
    "gender", "capital_gain", "capital_loss",
    "hours_per_week", "native_country", "income"
]

df = pd.read_csv("data_raw.csv", names=columns, skipinitialspace=True)

# CLEAN minimal for plotting

df.replace("?", pd.NA, inplace=True)
df.dropna(inplace=True)

# convert needed columns
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["hours_per_week"] = pd.to_numeric(df["hours_per_week"], errors="coerce")
df["education_num"] = pd.to_numeric(df["education_num"], errors="coerce")

# PLOTTING

plt.figure(figsize=(15,5))

# 1. Histogram (Age)
plt.subplot(1,3,1)
plt.hist(df["age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

# 2. Scatter Plot
plt.subplot(1,3,2)
plt.scatter(df["education_num"], df["hours_per_week"])
plt.title("Education vs Working Hours")
plt.xlabel("Education Level (num)")
plt.ylabel("Hours per week")

# 3. Heatmap
plt.subplot(1,3,3)
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=False)
plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("summary_plot.png")

print("Visualization done")

# next step
os.system("python cluster.py data_preprocessed.csv")