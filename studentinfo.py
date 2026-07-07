
import pandas as pd

data = {
    "Roll Number": [101, 102, 103, 104, 105],
    "Name": ["jaydeep", "shakti", "Rahul", "yash", "hiren"],
    "Gender": ["Male", "male", "Male", "male", "Male"],
    "Course": ["BSc", "BSc", "BCom", "BTech", "BTech"],
    "Marks": [85, 92, 78, 88, 81]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)

print("\nStructure of the DataFrame:")
print(df.info())