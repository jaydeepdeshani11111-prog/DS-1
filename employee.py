import pandas as pd

data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Karan"],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales"],
    "Salary": [45000, 60000, 55000, 50000, 65000],
    "Experience": [2, 5, 4, 3, 6]
}

employees = pd.DataFrame(data)

print("Employee Details:")
print(employees)

print("\nSelected Columns (Name and Salary):")
print(employees[["Name", "Salary"]])


print("\nEmployee Information:")
employees.info()