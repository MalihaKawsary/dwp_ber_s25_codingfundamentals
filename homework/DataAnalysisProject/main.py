import pandas as pd 

df = pd.read_csv('homework/DataAnalysisProject/DataAnalysisProjectData.txt')

print(df)
print("number of rows:", df.shape[0])
print("number of columns:", df.shape[1])

print("Column names:", df.columns.tolist())
print("Row names (index):", df.index.tolist())

average_salary=df["Salary"].mean()
print("The average salary of all employees:", average_salary)
average_age = df['Age'].mean()
print("Average age of all employees:", average_age)
min_exp = df['YearsOfExperience'].min()
max_exp = df['YearsOfExperience'].max()
print(f"Years of experience range: {min_exp} to {max_exp}")

departments = df['Department'].unique()  
num_departments = len(departments) 
print(f"Number of departments: {num_departments}")

print("Departments:", departments)
import matplotlib.pyplot as plt

dept_counts = df['Department'].value_counts()

print(f'total number of employees in each department:{dept_counts}')

plt.figure(figsize=(8, 8))

plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=140)

plt.title('Percentage of Employees in Each Department')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
plt.show()


dept_counts = df['Department'].value_counts()

# Print department-wise counts and percentages in terminal
total_employees = dept_counts.sum()
print("Department-wise Employee Distribution:")
for dept, count in dept_counts.items():
    percentage = (count / total_employees) * 100
    print(f"{dept}: {count} employees ({percentage:.1f}%)")

with open('management_summary.txt', 'w') as f:
    f.write("Summary Statistics:\n")
    f.write(f"Average salary of all employees: {average_salary:.2f}\n")
    f.write(f"Average age of all employees: {average_age:.2f}\n")
    f.write(f"Years of experience range: {min_exp} to {max_exp}\n")
    f.write(f"Number of departments: {num_departments}\n")
    f.write(f"Departments: {', '.join(departments)}\n\n")
    f.write("Department-wise Employee Distribution:\n")
    for dept, count in dept_counts.items():
        percentage = (count / total_employees) * 100
        f.write(f"{dept}: {count} employees ({percentage:.1f}%)\n")