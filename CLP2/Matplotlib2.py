import matplotlib.pyplot as plt 

regions = ["North", "South", "East", "West"]
sales = [5000, 7000, 5500, 6000]

plt.bar(regions, sales, color='skyblue', width=0.6)

plt.xlabel("Regions")
plt.ylabel("Sales Revenue ($)")
plt.title("Sales Revenue Across Regions")

plt.show()
