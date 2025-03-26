import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_excel("Professional.xlsx")

# Extract the 'Broadband Access?' column (assuming it contains binary values like 'Yes' and 'No')
broadband_access = data["Broadband Access?"]

# Calculate the sample proportion of graduates with broadband access
sample_proportion = broadband_access.value_counts(normalize=True)["Yes"]

# Calculate the standard error (SE) for the proportion
std_error_proportion = np.sqrt(
    sample_proportion * (1 - sample_proportion) / len(broadband_access)
)

# Calculate the margin of error for a 95% confidence interval
z_score = 1.96  # For a 95% confidence interval
margin_of_error = z_score * std_error_proportion

# Calculate the 95% confidence interval for the proportion
confidence_interval = (
    sample_proportion - margin_of_error,
    sample_proportion + margin_of_error,
)

# Print the results
print(f"Sample Proportion of Graduates with Broadband Access: {sample_proportion:.2%}")
print(f"Standard Error (SE) for the Proportion: {std_error_proportion:.4f}")
print(
    f"95% Confidence Interval for the Proportion: ({confidence_interval[0]:.4f}, {confidence_interval[1]:.4f})"
)

# Create multiple visualizations
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Bar chart
sns.countplot(x="Broadband Access?", data=data, ax=axes[0])
axes[0].set_title("Broadband Access Count")

# 2. Pie chart
data["Broadband Access?"].value_counts().plot.pie(autopct="%1.1f%%", ax=axes[1])
axes[1].set_title("Broadband Access Proportion")

# 3. Bar chart with confidence interval
axes[2].bar("Proportion", sample_proportion, color="skyblue")
axes[2].errorbar(
    "Proportion", sample_proportion, yerr=margin_of_error, fmt="ro", capsize=5
)
axes[2].set_title("Broadband Access Proportion with CI")

plt.show()
