
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_folder = Path(__file__).resolve().parent
data_folder = project_folder / "data"
chart_folder = project_folder / "reports" / "charts"
chart_folder.mkdir(parents=True, exist_ok=True)
print("Task 3 Started Successfully")

print("\nNUMPY ANALYSIS")

marks = np.array([[80, 75, 90],[85, 88, 92],[70, 65, 78],[90, 95, 85]])
print("Student Marks:")
print(marks)
print("Array Shape:", marks.shape)
student_average = np.mean(marks, axis=1)
print("Student Averages:", student_average)

subject_average = np.mean(marks, axis=0)
print("Subject Averages:", subject_average)

updated_marks = marks + 5
print("Updated Marks:")
print(updated_marks)

weights = np.array([0.4, 0.3, 0.3])
weighted_scores = np.dot(marks, weights)
print("Weighted Scores:", weighted_scores)

print("\nPANDAS ANALYSIS")
employee_file = data_folder / "employees.csv"
employees = pd.read_csv(employee_file)
print("Employee Data:")
print(employees)
print("\nData Information:")
employees.info()
print("\nData Description:")
print(employees.describe())
print("\nUsing loc:")
print(employees.loc[0:2, ["name", "salary"]])
print("\nUsing iloc:")
print(employees.iloc[0:3, 0:3])
print("\nEmployees earning above 50000:")
print(employees[employees["salary"] > 50000])

print("\nDATA CLEANING")
dirty_file = data_folder / "employees_dirty.csv"
dirty_employees = pd.read_csv(dirty_file)
print("Missing Values Before Cleaning:")
print(dirty_employees.isnull().sum())
print("Duplicate Rows Before Cleaning:")
print(dirty_employees.duplicated().sum())

salary_median = dirty_employees["salary"].median()
dirty_employees["salary"] = dirty_employees["salary"].fillna(salary_median)
dirty_employees = dirty_employees.drop_duplicates()

dirty_employees["id"] = dirty_employees["id"].astype(int)
dirty_employees["salary"] = dirty_employees["salary"].astype(int)

print("\nCleaned Employee Data:")
print(dirty_employees)

print("Missing Values After Cleaning:")
print(dirty_employees.isnull().sum())

print("Duplicate Rows After Cleaning:")
print(dirty_employees.duplicated().sum())

dirty_employees.to_csv(
    data_folder / "cleaned_employees.csv",
    index=False)

print("Cleaned Employee Data Saved Successfully")
print("\nDEPARTMENT ANALYSIS")

department_summary = dirty_employees.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max"))

print(department_summary)
print("\nDATA MERGING")
department_file = data_folder / "departments.csv"
departments = pd.read_csv(department_file)

inner_merge = pd.merge(
    dirty_employees,
    departments,
    on="department",
    how="inner")
print("\nInner Merge:")
print(inner_merge)


left_merge = pd.merge(
    dirty_employees,
    departments,
    on="department",
    how="left")
print("\nLeft Merge:")
print(left_merge)

outer_merge = pd.merge(
    dirty_employees,
    departments,
    on="department",
    how="outer")
print("\nOuter Merge:")
print(outer_merge)

employee_departments = dirty_employees["department"].unique()
empty_departments = departments[
    ~departments["department"].isin(employee_departments)]
print("\nDepartments Without Employees:")
print(empty_departments)
print("\nCREATING CHARTS")
department_salary = dirty_employees.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
plt.bar(department_salary.index, department_salary.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.legend(["Average Salary"])
plt.tight_layout()
plt.savefig(chart_folder / "bar_chart.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.hist(dirty_employees["salary"], bins=5, edgecolor="black")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend(["Employees"])
plt.tight_layout()
plt.savefig(chart_folder / "histogram.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(dirty_employees["id"], dirty_employees["salary"])
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(["Employees"])
plt.tight_layout()
plt.savefig(chart_folder / "scatter_chart.png")
plt.close()

plt.figure(figsize=(8, 5))
plt.plot(dirty_employees["id"],dirty_employees["salary"],marker="o")
plt.title("Employee Salary Trend")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(["Salary"])
plt.tight_layout()
plt.savefig(chart_folder / "line_chart.png")
plt.close()

print("All Four Charts Created Successfully")
print("\nTask 3 Completed Successfully")
