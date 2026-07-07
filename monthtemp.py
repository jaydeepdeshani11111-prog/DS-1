import pandas as pd

temperature = pd.Series(
    [18, 20, 25, 30, 35, 38, 36, 34, 32, 28, 22, 19],
    index=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
)
print("Average Temperature of 12 Months:")
print(temperature)

print("\nHottest Month:")
print(temperature.idxmax(), "-", temperature.max(), "°C")

print("\nColdest Month:")
print(temperature.idxmin(), "-", temperature.min(), "°C")

print("\nAverage Yearly Temperature:")
print(round(temperature.mean(), 2), "°C")