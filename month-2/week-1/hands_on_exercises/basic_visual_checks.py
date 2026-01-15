import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data.csv")

plt.hist(df.select_dtypes(include='number').iloc[:,0])
plt.title("Basic Distribution Check")
plt.show()
1