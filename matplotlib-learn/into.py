import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import importlib.util
import sys
file_path = r'C:\Users\DELL\PycharmProjects\ML\pandas-learn\student-performance_analysis.py'

# Load the module dynamically
spec = importlib.util.spec_from_file_location("student_analysis", file_path)
student_analysis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student_analysis)

# np.random.seed(42) # Makes the "random" numbers the same every time you run it
# data = {
#     'attendance': np.random.randint(60, 100, 100),
#     'avg_score': np.random.normal(82, 8, 100) # Mean of 82, Spread of 8
# }
# df = pd.DataFrame(data)
# Now access your DataFrame
df = student_analysis.df
sns.set()
# plt.hist(df['avg_score'], bins=5)
# plt.title("Distribution of Average Scores")
# plt.xlabel("Average Score")
# plt.ylabel("Number of Students")
# plt.show()

# sns.scatterplot(x=df['attendance'], y=df['avg_score'])
# plt.title("Attendance vs Average Score")
# plt.xlabel("Attendance")
# plt.ylabel("Average Score")
# plt.show()

# sns.boxplot(x=df['attendance_group'], y=df['avg_score'])
# plt.title("Performance by Attendance Group")
# plt.show()


top_students = df.sort_values('avg_score', ascending=False)

sns.barplot(x='name', y='avg_score', data=top_students)
plt.title("Student Performance Ranking")
plt.xticks(rotation=45)
plt.show()

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True)
plt.title("Correlation Matrix")
plt.show()