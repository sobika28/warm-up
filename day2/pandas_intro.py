from pathlib import Path
import pandas as pd
import numpy as np

folder = Path(__file__).parent
input_file = folder / "marks_data.csv"
output_file = folder / "cleaned_marks.csv"

#Load the CSV
df = pd.read_csv(input_file)

#Inspect the data
print("First five rows:")
print(df.head())

print("\nDataFrame information:")
df.info()

print("\nStatistical summary:")
print(df.describe())

#Check missing values
print("\nMissing values:")
print(df.isnull().sum())

#Fill missing marks with the overall median
df["marks"] = df["marks"].fillna(df["marks"].median())

#Convert marks to NumPy array
marks_array = np.array(df["marks"])
print("\nNumPy marks array:", marks_array)

#Filter students scoring at least 85
high_scores = df[df["marks"] >= 85]
print("\nStudents scoring 85 or above:")
print(high_scores)

# Group by department and calculate average marks
department_summary = df.groupby("department").agg(
    student_count=("name", "count"),
    average_marks=("marks", "mean"),
    highest_marks=("marks", "max")
)
print("\nDepartment summary:")
print(department_summary)
#Save the cleaned dataset
df.to_csv(output_file, index=False)
print(f"\nCleaned CSV saved to: {output_file}")

