# Pandas: Merge only specific DataFrame columns

import pandas as pd

df1 = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023],
    'profit': [1500, 2500, 3500, 4500],
})


df2 = pd.DataFrame({
    'year': [2020, 2021, 2022, 2023],
    'employees': [10, 15, 20, 25],
    'CEO': ['A', 'B', 'C', 'D'],
    'CFO': ['Q', 'W', 'E', 'R']
})


df3 = df1.merge(
    df2[['year', 'employees']],
    on='year',
    how='left'
)

#    year  profit  employees
# 0  2020    1500         10
# 1  2021    2500         15
# 2  2022    3500         20
# 3  2023    4500         25
print(df3)