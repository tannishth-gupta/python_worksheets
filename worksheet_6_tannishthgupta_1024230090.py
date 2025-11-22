import pandas as pd

print("Q1")
print(pd.__version__)
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
print(df)

print("\nQ2")
S1 = pd.Series([100, 200, 300, 400, 500])
print(S1)
print(S1.iloc[1], S1.iloc[3])
S2 = pd.Series([10, 20, 30, 40, 50])
print(S1 + S2)

print("\nQ3")
print(df[['Name', 'City']])
df['Salary'] = [50000, 60000, 70000]
print(df)
print(df['Age'].mean())
print(df['Salary'].sum())

print("\nQ4")
filtered = df[df['Age'] > 28]
print(filtered)
df2 = df.set_index('Name')
print(df2)
df2 = df2.reset_index()
print(df2)

print("\nQ5")
employees = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR'],
    'Salary': [50000, 60000, 55000]
})
print(employees)
filtered_emp = employees[employees['Salary'] > 55000]
print(filtered_emp)
print(filtered_emp[['Name', 'Department']])

print("\nQ6")
grouped_avg = employees.groupby('Department')['Salary'].mean()
print(grouped_avg)
grouped_minmax = employees.groupby('Department')['Salary'].agg(['min', 'max'])
print(grouped_minmax)

print("\nQ7")
df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})
df2 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience (Years)': [5, 7, 3]
})
merged = pd.merge(df1, df2, on='Name')
print(merged)

print("\nQ8")
sorted_df = merged.sort_values(by='Experience (Years)', ascending=False)
print(sorted_df)
