import sys
import pandas as pd
import os

file_path = sys.argv[1]

columns = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race",
    "gender", "capital_gain", "capital_loss",
    "hours_per_week", "native_country", "income"
]

df = pd.read_csv("data_raw.csv", names=columns, skipinitialspace=True)

df["income"] = df["income"].str.strip()

df["income"] = df["income"].map({
    "<=50K": 0,
    ">50K": 1
})

# ANALYTICS

# Average age
avg_age = df["age"].mean()

# Average working hours
avg_hours = df["hours_per_week"].mean()

# Correlation between education and income
corr_edu_income = df["education_num"].corr(df["income"])

# Correlation between hours and income
corr_hours_income = df["hours_per_week"].corr(df["income"])

#income based on age, education, and working hours
group_means = df.groupby("income")[["age", "education_num", "hours_per_week"]].mean()
low_income = group_means.loc[0]
high_income = group_means.loc[1]

#income based on the capital gain
capital_gain_effect = df[df["capital_gain"] > 0]["income"].value_counts(normalize=True)


# WRITE INSIGHTS



with open("insight1.txt", "w") as f:
    f.write(f"Average age: {avg_age}\n")
    f.write(f"Average working hours per week: {avg_hours}\n")

with open("insight2.txt", "w") as f:
    f.write(f"Correlation between education level and income: {corr_edu_income}\n")
    f.write(f"Correlation between working hours and income: {corr_hours_income}\n")

with open("insight3.txt","w") as f:
    f.write(f"High-income individuals tend to be older, more educated, and work more hours per week\n")
    f.write(f"Average values by income groups:\n\n")
    f.write(f"Low income (0) : \n")
    f.write(f"Age: {low_income['age']:.2f}\n")
    f.write(f"Education: {low_income['education_num']:.2f}\n")
    f.write(f"Hours per week: {low_income['hours_per_week']:.2f}\n\n")    
    f.write(f"High income (1) : \n")
    f.write(f"Age: {high_income['age']:.2f}\n")
    f.write(f"Education: {high_income['education_num']:.2f}\n")
    f.write(f"Hours per week: {high_income['hours_per_week']:.2f}")    

with open("insight4.txt", "w") as f:
    f.write(f"Individuals with non-zero capital gains are significantly more likely to earn high income\n")
    f.write(f"Capital gain impact on income:\n")
    f.write(f"{capital_gain_effect}\n")

print("Analytics done")

# call next step
os.system("python visualize.py data_preprocessed.csv")