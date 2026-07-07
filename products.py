import pandas as pd

data = {
    "Product ID": [101, 102, 103, 104],
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [50000, 500, 1200, 10000],
    "Quantity": [2, 5, 3, 2],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics"]
}

df = pd.DataFrame(data)

df["Total Amount"] = df["Price"] * df["Quantity"]

print(df)