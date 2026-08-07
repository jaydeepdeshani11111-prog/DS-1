import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("laptopsales.csv")
plt.plot(df["Month"],df["Laptop Sales"],Marker='o')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Laptop Sales")
plt.show()