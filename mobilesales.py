import pandas as pd

sales = pd.Series(
    [120, 150, 180, 170, 200, 190, 210, 175, 160, 220, 205, 230],
    index=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
)

print("Monthly Mobile Phone Sales:")
print(sales)

print("\nHighest Sales:", sales.max())
print("Lowest Sales:", sales.min())
print("Average Monthly Sales:", sales.mean())