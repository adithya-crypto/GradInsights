import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_excel("Professional.xlsx")

# Extract the 'Age' column
ages = data["Age"]

# Calculate the sample mean age
mean_age = np.mean(ages)

# Calculate the standard error (SE) for the mean age
std_error_age = np.std(ages, ddof=1) / np.sqrt(len(ages))

# Calculate the margin of error for a 95% confidence interval
z_score = 1.96  # For a 95% confidence interval
margin_of_error = z_score * std_error_age

# Calculate the 95% confidence interval for the mean age
confidence_interval = (mean_age - margin_of_error, mean_age + margin_of_error)

# Print the results
print(f"Sample Mean Age: {mean_age:.2f}")
print(f"Standard Error (SE) for the Mean Age: {std_error_age:.2f}")
print(
    f"95% Confidence Interval for the Mean Age: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})"
)

# Visualize the mean age
plt.bar("Mean Age", mean_age, yerr=margin_of_error, capsize=5, color="skyblue")
plt.xlabel("Age")
plt.ylabel("Mean Age")
plt.title("Mean Age with 95% Confidence Interval")
plt.show()
