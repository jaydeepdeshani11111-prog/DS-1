import pandas as pd

balances = pd.Series(
    [45000, 62000, 78000, 30000, 55000, 49000, 91000],
    index=["Amit", "Neha", "Rahul", "Priya", "Karan", "Sneha", "Rohan"]
)

print("Customer Account Balances:")
print(balances)

print("\nCustomers with balance greater than ₹50,000:")
print(balances[balances > 50000])