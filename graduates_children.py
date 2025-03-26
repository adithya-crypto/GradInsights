import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_excel("Professional.xlsx")

# Extract the 'Have Children?' column (assuming it contains binary values like 'Yes' and 'No')
have_children = data["Have Children?"]

# Calculate the sample proportion of graduates with children
sample_proportion = have_children.value_counts(normalize=True)["Yes"]

# Calculate the standard error (SE) for the proportion
std_error_proportion = np.sqrt(
    sample_proportion * (1 - sample_proportion) / len(have_children)
)

# Calculate the margin of error for a 95% confidence interval
z_score = 1.96  # For a 95% confidence interval
margin_of_error = z_score * std_error_proportion

# Calculate the 95% confidence interval for the proportion
confidence_interval = (
    sample_proportion - margin_of_error,
    sample_proportion + margin_of_error,
)

# Create the bar chart showing the count of graduates with and without children
sns.countplot(x="Have Children?", data=data)
plt.title("Graduates with Children Count")
plt.xlabel("Have Children?")
plt.ylabel("Count")
plt.show()

# Create the pie chart representing the proportion of graduates with and without children
labels = ["Have Children", "No Children"]
sizes = data["Have Children?"].value_counts()
colors = ["skyblue", "lightcoral"]
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
plt.title("Proportion of Graduates with Children")
plt.show()

# Create a bar chart with the sample proportion and confidence interval
plt.bar("Proportion", sample_proportion, color="skyblue")
plt.errorbar("Proportion", sample_proportion, yerr=margin_of_error, fmt="ro", capsize=5)
plt.title("Proportion of Graduates with Children with 95% Confidence Interval")
plt.ylabel("Proportion")
plt.show()

# Print the results
print(f"Sample Proportion of Graduates with Children: {sample_proportion:.2%}")
print(f"Standard Error (SE) for the Proportion: {std_error_proportion:.4f}")
print(
    f"95% Confidence Interval for the Proportion: ({confidence_interval[0]:.4f}, {confidence_interval[1]:.4f})"
)
