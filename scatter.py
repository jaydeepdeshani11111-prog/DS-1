import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("study.csv")
plt.plot(df["Study Hours"],df["Marks"])
plt.title("Monthly Sales scatter plot")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()