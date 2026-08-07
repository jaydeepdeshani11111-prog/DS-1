import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("acsales_data.csv")
plt.bar(df["Month"],df["AC Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("AC Sales")
plt.show()