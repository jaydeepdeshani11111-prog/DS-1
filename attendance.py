import pandas as pd

attendance = pd.Series([82, 68, 91, 74, 88],
    index=["jaydeep", "hiren", "yash", "hari", "anand"]
)

print("Attendance Percentage:")
print(attendance)

print("\nStudents having attendance less than 75%:")
print(attendance[attendance < 75])