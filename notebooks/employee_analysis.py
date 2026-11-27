#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis
# 
# ## Project Overview
# 
# This project analyses employee data using Python, NumPy, Pandas, and Matplotlib.
# 
# ## Objectives
# 
# 1. Load employee data from CSV files.
# 2. Analyse employee salaries.
# 3. Handle missing and duplicate records.
# 4. Calculate department-wise statistics.
# 5. Create charts to visualise employee data.

# 

# In[1]:


# Import pandas library
import pandas as pd

# Load employee CSV file
employees = pd.read_csv("../data/employees.csv")

# Display the first 5 rows
employees.head()


# In[ ]:





# In[2]:


# Import pandas library
import pandas as pd

# Load employee CSV file
employees = pd.read_csv("../data/employees.csv")

# Display the first 5 rows
employees.head()


# In[ ]:





# In[3]:


# Display all rows and columns
employees


# In[ ]:





# In[4]:


# Check the number of rows and columns
employees.shape


# In[ ]:





# In[5]:


# Get information about the dataset
employees.info()


# In[ ]:





# In[6]:


# Calculate statistical information about employee salaries
employees["salary"].describe()


# In[ ]:





# In[7]:


# Filter employees with salary greater than 50000
high_salary = employees[employees["salary"] > 50000]

# Display the result
high_salary


# In[8]:


# Select employees who belong to Chennai
chennai_employees = employees.loc[employees["city"] == "Chennai"]

# Display Chennai employees
chennai_employees


# In[ ]:





# In[9]:


# Select only name and salary columns
employees.loc[:, ["name", "salary"]]


# In[ ]:





# In[10]:


# Sort employees by salary in descending order
sorted_employees = employees.sort_values(
    by="salary",
    ascending=False
)

# Display sorted employees
sorted_employees


# In[ ]:





# In[11]:


# Calculate average salary for each department
department_salary = employees.groupby("department")["salary"].mean()

# Display the result
department_salary


# In[ ]:





# In[12]:


# Count employees in each department
department_count = employees.groupby("department")["id"].count()

# Display the result
department_count


# In[ ]:





# In[13]:


# Select the first employee
employees.iloc[0]


# In[ ]:





# In[14]:


# Select the first three employees
employees.iloc[0:3]


# In[ ]:





# In[15]:


# Load the dirty employee dataset
dirty_employees = pd.read_csv("../data/employees_dirty.csv")

# Display the first 5 rows
dirty_employees.head()


# In[ ]:





# In[16]:


# Count missing values in each column
dirty_employees.isnull().sum()


# In[ ]:





# In[17]:


# Remove duplicate employee records
dirty_employees = dirty_employees.drop_duplicates()

# Display the updated dataset
dirty_employees


# In[ ]:





# In[18]:


# Calculate the median salary
median_salary = dirty_employees["salary"].median()

# Fill missing salary values with the median
dirty_employees["salary"] = dirty_employees["salary"].fillna(median_salary)

# Display the updated salary column
dirty_employees["salary"]


# In[ ]:





# In[19]:


# Check missing values after cleaning
print("Missing values:")
print(dirty_employees.isnull().sum())

# Check duplicate records after cleaning
print("\nDuplicate records:")
print(dirty_employees.duplicated().sum())


# In[ ]:





# In[20]:


# Display cleaned employee information
dirty_employees.info()


# In[21]:


# Load department information
departments = pd.read_csv("../data/departments.csv")

# Display department records
departments


# In[ ]:





# In[22]:


# Display department column names
print("Department columns:")
print(departments.columns)

# Display department dataset information
print("\nDepartment information:")
departments.info()


# In[ ]:





# In[23]:


# Perform Inner Join
inner_join = pd.merge(
    dirty_employees,
    departments,
    on="department",
    how="inner"
)

# Display the result
inner_join


# In[ ]:





# In[24]:


# Perform Left Join
left_join = pd.merge(
    dirty_employees,
    departments,
    on="department",
    how="left"
)

# Display the result
left_join


# In[ ]:





# In[ ]:





# In[25]:


# Perform Outer Join
outer_join = pd.merge(
    dirty_employees,
    departments,
    on="department",
    how="outer"
)

# Display the result
outer_join


# In[ ]:





# In[26]:


# Find departments without employees
departments_without_employees = outer_join[
    outer_join["id"].isnull()
]

# Display departments without employees
departments_without_employees


# In[ ]:





# In[27]:


# Import NumPy
import numpy as np

# Create an array of employee marks
marks = np.array([75, 80, 85, 90, 95])

# Display the array
print("Employee Marks:", marks)

# Calculate average marks
print("Average Marks:", np.mean(marks))

# Calculate maximum marks
print("Maximum Marks:", np.max(marks))

# Calculate minimum marks
print("Minimum Marks:", np.min(marks))


# In[ ]:





# In[28]:


# Create a 2-dimensional NumPy array
marks = np.array([
    [75, 80, 85],
    [90, 95, 88]
])

# Display the array
print("Marks Array:")
print(marks)

# Check array shape
print("Array Shape:", marks.shape)

# Check number of dimensions
print("Array Dimensions:", marks.ndim)

# Check total number of elements
print("Total Elements:", marks.size)


# In[ ]:





# In[29]:


# Create an array of employee marks
marks = np.array([75, 80, 85, 90, 95])

# Add 5 marks to every employee
updated_marks = marks + 5

# Display original and updated marks
print("Original Marks:", marks)
print("Updated Marks:", updated_marks)


# In[ ]:





# In[ ]:





# In[30]:


# Create two NumPy arrays
employee_hours = np.array([8, 7, 9])
hourly_rate = np.array([100, 120, 150])

# Calculate total salary
total_salary = np.dot(employee_hours, hourly_rate)

# Display the result
print("Employee Hours:", employee_hours)
print("Hourly Rates:", hourly_rate)
print("Total Salary:", total_salary)


# In[ ]:





# In[31]:


# Import Matplotlib
import matplotlib.pyplot as plt

# Calculate average salary by department
department_salary = employees.groupby("department")["salary"].mean()

# Create bar chart
department_salary.plot(kind="bar")

# Add chart title and labels
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Display chart
plt.show()


# In[ ]:





# In[32]:


# Create a histogram for employee salaries
plt.hist(employees["salary"], bins=5, edgecolor="black")

# Add chart title and labels
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

# Display chart
plt.show()


# In[ ]:





# In[33]:


# Create a scatter plot
plt.scatter(employees["id"], employees["salary"])

# Add chart title and labels
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")

# Display chart
plt.show()


# In[ ]:





# In[34]:


# Create a line chart
plt.plot(
    employees["name"],
    employees["salary"],
    marker="o",
    label="Employee Salary"
)

# Add chart title and labels
plt.title("Employee Salary Comparison")
plt.xlabel("Employee Name")
plt.ylabel("Salary")

# Display legend
plt.legend()

# Display chart
plt.show()


# In[ ]:





# In[ ]:





# ## Data Visualization Findings
# 
# 1. Bar Chart: Finance has the highest average salary.
# 2. Histogram: Shows the distribution of employee salaries.
# 3. Scatter Plot: Compares employee IDs with salaries.
# 4. Line Chart: Karthik has the highest salary, while Arun has the lowest.

# In[36]:


# Measure the execution time of calculating average salary
get_ipython().run_line_magic('timeit', 'employees["salary"].mean()')


# 
