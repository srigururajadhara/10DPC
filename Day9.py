import numpy as np
import pandas as pd

# --------------------------------------------------
# Step 1: NumPy for Numerical Operations
# --------------------------------------------------
# Create a NumPy 1D array of base employee salaries
base_salaries = np.array([55000, 72000, 61000, 48000, 95000])

# Perform vectorized math (e.g., apply a 10% bonus across all salaries)
bonuses = base_salaries * 0.10
total_salaries = base_salaries + bonuses

print("NumPy Array - Total Salaries:")
print(total_salaries)
print("Average Salary:", np.mean(total_salaries))

# --------------------------------------------------
# Step 2: Pandas for Tabular Data Manipulation
# --------------------------------------------------
# Build a DataFrame using standard Python and NumPy arrays
data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["Sales", "Engineering", "Sales", "HR", "Engineering"],
    "Base_Salary": base_salaries,
    "Bonus": bonuses,
    "Total_Salary": total_salaries,
}

df = pd.DataFrame(data)

# Add a conditional column using NumPy's np.where
df["Senior_Band"] = np.where(df["Total_Salary"] >= 70000, "Senior", "Junior")

print("\n--- Full DataFrame ---")
print(df)

# Filter: Employees earning above $65,000 in Engineering
engineering_high_earners = df[
    (df["Department"] == "Engineering") & (df["Total_Salary"] > 65000)
]
print("\n--- Filtered: Engineering > $65,000 ---")
print(engineering_high_earners[["Employee", "Total_Salary"]])

# Aggregate: Average total salary by Department
dept_avg = df.groupby("Department")["Total_Salary"].mean().reset_index()
print("\n--- Department Average Salary ---")
print(dept_avg)