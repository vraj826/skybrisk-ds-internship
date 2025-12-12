# Pandas: Create a simple DataFrame

import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Score": [80, 92, 75]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)
