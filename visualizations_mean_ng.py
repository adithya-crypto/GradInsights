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

# Create a bar chart with error bars
plt.bar("Mean Household Income", mean_income, color="skyblue")
plt.errorbar(
    "Mean Household Income", mean_income, yerr=margin_of_error, fmt="ro", capsize=5
)

plt.xlabel("Household Income")
plt.ylabel("Mean Household Income")
plt.title("Mean Household Income with 95% Confidence Interval (Bar Chart)")
plt.show()

# Create a line plot with the confidence interval as a shaded region
x = ["Mean Household Income"]
y = [mean_income]
plt.plot(x, y, marker="o", color="blue", label="Mean Household Income")

# Create shaded region for the confidence interval
plt.fill_between(
    x,
    confidence_interval[0],
    confidence_interval[1],
    color="gray",
    alpha=0.3,
    label="95% Confidence Interval",
)

plt.xlabel("Household Income")
plt.ylabel("Mean Household Income")
plt.title("Mean Household Income with 95% Confidence Interval (Line Plot)")
plt.legend()
plt.show()
