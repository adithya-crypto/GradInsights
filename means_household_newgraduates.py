import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_excel("Professional.xlsx")

# Extract the 'Household Income ($)' column
household_income = data["Household Income ($)"]

# Calculate the sample mean household income
mean_income = np.mean(household_income)

# Calculate the standard error (SE) for the mean household income
std_error_income = np.std(household_income, ddof=1) / np.sqrt(len(household_income))

# Calculate the margin of error for a 95% confidence interval
z_score = 1.96  # For a 95% confidence interval
margin_of_error = z_score * std_error_income

# Calculate the 95% confidence interval for the mean household income
confidence_interval = (mean_income - margin_of_error, mean_income + margin_of_error)

# Print the results
print(f"Sample Mean Household Income: ${mean_income:.2f}")
print(f"Standard Error (SE) for the Mean Household Income: ${std_error_income:.2f}")
print(
    f"95% Confidence Interval for the Mean Household Income: (${confidence_interval[0]:.2f}, ${confidence_interval[1]:.2f})"
)

# Visualize the mean household income
plt.bar(
    "Mean Household Income",
    mean_income,
    yerr=margin_of_error,
    capsize=5,
    color="skyblue",
)
plt.xlabel("Household Income")
plt.ylabel("Mean Household Income")
plt.title("Mean Household Income with 95% Confidence Interval")
plt.show()
