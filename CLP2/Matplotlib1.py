import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = [30, 32, 31, 29, 28, 27, 26]

plt.plot(days, temps, marker="o", linestyle="-", color="b")

plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Weekly Temperature Variations")

plt.show()
