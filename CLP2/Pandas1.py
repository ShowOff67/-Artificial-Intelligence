import pandas as pd  

df = pd.read_csv("sales.csv")

df["Total Revenue"] = df["Quantity"] * df["Price"]
total_rev = df.groupby("Product")["Total Revenue"].sum()

print("Total Revenue per Product:\n", total_rev)
