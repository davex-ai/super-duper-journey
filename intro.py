from pandas import pandas as pd

data = {
    "name": ["Dave", "Ada", "John", "Mary", "Paul"],
    "age": [15, 18, 21, 17, 19],
    "score": [90, 85, 88, 72, 95]
}

df = pd.DataFrame(data)
print(df)