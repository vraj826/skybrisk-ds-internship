# Pandas: Filter rows

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Score": [80, 92, 75]
}

df = pd.DataFrame(data)
filtered_df = df[df["Score"] > 80]

print("Original DataFrame:\n", df)
print("\nFiltered DataFrame (Score > 80):\n", filtered_df)
