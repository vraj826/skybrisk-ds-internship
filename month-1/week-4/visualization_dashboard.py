# --------------------------------------------------------
# CLIENT PROJECT – BASIC VISUALIZATION DASHBOARD
# Week 4: Matplotlib & Seaborn Only
# --------------------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset from Seaborn
df = sns.load_dataset("tips")

plt.figure(figsize=(14, 6))

# 1. Scatter Plot – Bill vs Tip
plt.subplot(1, 3, 1)
sns.scatterplot(data=df, x="total_bill", y="tip")
plt.title("Total Bill vs Tip")

# 2. Histogram of Total Bill
plt.subplot(1, 3, 2)
plt.hist(df["total_bill"])
plt.title("Total Bill Distribution")

# 3. Box Plot of Tips
plt.subplot(1, 3, 3)
sns.boxplot(data=df, y="tip")
plt.title("Tip Amount Spread")

plt.tight_layout()
plt.show()
