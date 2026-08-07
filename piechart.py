import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("brandsales.csv")
plt.pie(df["Units Sold"],
    labels=df["Brand"],
    autopct='%1.2f%%'
        )
plt.title("smartphone sales distribution.")   
plt.show()