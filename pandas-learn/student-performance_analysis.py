import pandas as pd

data = {
    "name": ["Dave", "Ada", "John", "Mary", "Paul", "Jane", "Mike", "Sara"],
    "age": [15, 18, 21, 17, 19, 20, 22, 16],
    "math_score": [90, 85, 88, 72, 95, 80, 78, 84],
    "english_score": [85, 88, 90, 70, 92, 79, 75, 82],
    "attendance": [90, 95, 85, 60, 98, 88, 70, 92]
}

df = pd.DataFrame(data)