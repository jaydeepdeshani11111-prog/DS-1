import pandas as pd

data = {
    "Patient ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Age": [35, 28, 45, 32, 50],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Disease": ["Diabetes", "Fever", "Hypertension", "Asthma", "Arthritis"],
    "Doctor Name": ["Dr. Sharma", "Dr. Mehta", "Dr. Patel", "Dr. Shah", "Dr. Joshi"]
}

df = pd.DataFrame(data)

print("Patient Details:")
print(df)

print("\nSummary Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())