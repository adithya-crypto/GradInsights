import pandas as pd
import scipy.stats as stats

# Load your dataset
data = pd.read_excel("Professional.xlsx")

# Define the desired confidence level (e.g., 95%)
confidence_level = 0.95

# Define the margin of error (e.g., 5% margin of error)
margin_of_error = 0.05

# Calculate the sample size for each variable
sample_sizes = {}

# Standard deviation for 'Age' and 'Household Income' (replace with your dataset's values)
std_dev_age = data["Age"].std()
std_dev_income = data["Household Income ($)"].std()

# Estimated proportion for 'Broadband Access' and 'Have Children'
estimated_proportion_broadband = data["Broadband Access?"].value_counts(normalize=True)[
    1
]
estimated_proportion_children = data["Have Children?"].value_counts(normalize=True)[
    "Yes"
]

# Calculate the sample sizes
sample_sizes["Age"] = int(
    (stats.norm.ppf((1 + confidence_level) / 2) * std_dev_age / margin_of_error) ** 2
)
sample_sizes["Household Income"] = int(
    (stats.norm.ppf((1 + confidence_level) / 2) * std_dev_income / margin_of_error) ** 2
)
sample_sizes["Broadband Access"] = int(
    (
        stats.norm.ppf((1 + confidence_level) / 2)
        * (estimated_proportion_broadband * (1 - estimated_proportion_broadband))
        / margin_of_error
    )
    ** 2
)
sample_sizes["Have Children"] = int(
    (
        stats.norm.ppf((1 + confidence_level) / 2)
        * (estimated_proportion_children * (1 - estimated_proportion_children))
        / margin_of_error
    )
    ** 2
)

# Print the calculated sample sizes
for variable, size in sample_sizes.items():
    print(f"Sample Size for {variable}: {size}")
