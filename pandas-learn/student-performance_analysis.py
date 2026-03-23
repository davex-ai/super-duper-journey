import numpy as np
import pandas as pd

data = {
    "name": ["Dave", "Ada", "John", "Mary", "Paul", "Jane", "Mike", "Sara"],
    "age": [15, 18, 21, 17, 19, 20, 22, 16],
    "math_score": [90, 85, 88, 72, 95, 80, 78, 84],
    "english_score": [85, 88, 90, 70, 92, 79, 75, 82],
    "attendance": [90, 95, 85, 60, 98, 88, 70, 92]
}

df = pd.DataFrame(data)
# print(df.head())
# print(df.info())
# print(df.describe())
df['avg_score'] = (df['math_score'] + df['english_score']) / 2
# print(df['avg_score'].mean())
passed = df['avg_score'] >= 50
high_attendance = df['attendance'] >= 90

high_performers = df[(df['attendance'] >= 90) & (df['avg_score'] > 85)]
struggling_student = df[df['attendance'] < 70]
# print(struggling_student)
top_3_high_performers = df.nlargest(3, 'avg_score')
# print(top_3_high_performers)
df['attendance_group'] = np.where(df['attendance'] >= 90, 'High', 'Low')

comparison = df.groupby('attendance_group')['avg_score'].mean()

df['overall_performance'] = (df['avg_score'] * 0.5) + (df['attendance'] * 0.5)
best_overall = df.nlargest(1, 'overall_performance')
# print(best_overall)

# print(df.nlargest(1, 'attendance'))
# print(df.nlargest(1, 'avg_score'))



# print(comparison)
# print(df.sort_values('avg_score', ascending=False))
# print(df.sort_values('attendance', ascending=False))