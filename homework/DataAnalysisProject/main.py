# Read the data, use the csv module to read the data from a CSV file
import pandas as pd 

df = pd.read_csv('homework/DataAnalysisProject/DataAnalysisProjectData.txt')

print(df)
# Explore data: try to print out its column names, and print out how many rows it has.
print("number of rows:", df.shape[0])
print("number of columns:", df.shape[1])

print("Column names:", df.columns.tolist())
print("Row names (index):", df.index.tolist())
# What is the average salary of all employees
average_salary=df["Salary"].mean()
print("The average salary of all employees:", average_salary)
# What is the average age of all employees?
average_age = df['Age'].mean()
print("Average age of all employees:", average_age)
# What are the years of experience range amongst all employees?
min_exp = df['YearsOfExperience'].min()
max_exp = df['YearsOfExperience'].max()
print(f"Years of experience range: {min_exp} to {max_exp}")
# How many departments are there and what are these departments?
departments = df['Department'].unique()  
num_departments = len(departments) 
print(f"Number of departments: {num_departments}")

print("Departments:", departments)
# Optional: If you are done with the statistics part, try to visualize the 
# percentage of people in each department via a pie chart. 
# Use the matplotlib module to visualize the results (pie charts, graphs, etc).
import matplotlib.pyplot as plt

dept_counts = df['Department'].value_counts()

print(f'total number of employees in each department:{dept_counts}')
# Name:count ,dtyp:int64, it comes in my terminal with column names because
# It’s a panada series. That means when we print column and
#  it’s values  with panda, then obviously this line Name:count ,dtyp:int64 comes in my terminal.
# df[“column”]- pandas series
# df[[“column”]] – pandas dataframe with one column


plt.figure(figsize=(8, 8))

plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=140)
# dept_counts,  Sales  index   -     120 value

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

with open('homework/DataAnalysisProject/management_summary.txt', 'w') as f:
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