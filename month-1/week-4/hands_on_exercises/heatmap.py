# Heatmap (Seaborn)

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
correlation = df.corr(numeric_only=True)

sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()
