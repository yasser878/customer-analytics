import sys
import pandas as pd
from sklearn.cluster import KMeans

file_path = sys.argv[1]

df = pd.read_csv(file_path)

# remove non-numeric column
df = df.drop(columns=["age_group"])

# KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(df)

# Analyze clusters

cluster_summary = df.groupby("cluster").mean()

with open("clusters.txt", "w") as f:
    for i in range(3):
        count = (df["cluster"] == i).sum()

        avg_income = cluster_summary.loc[i, "income"]
        avg_edu = cluster_summary.loc[i, "education_num"]
        avg_hours = cluster_summary.loc[i, "hours_per_week"]

        description = ""

        if avg_income > 0:
            description += "Higher income, "
        else:
            description += "Lower income, "

        if avg_edu > 0:
            description += "higher education, "
        else:
            description += "lower education, "

        if avg_hours > 0:
            description += "more working hours"
        else:
            description += "fewer working hours"

        f.write(f"Cluster {i}: {count} records -> {description}\n")

print("Clustering done")