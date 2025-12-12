# Histogram (Matplotlib)

import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 40, 40, 40, 50]

plt.hist(data)
plt.title("Histogram of Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
