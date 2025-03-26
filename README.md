# GradInsights: Professional Graduate Statistical Profile Analysis

A statistical analysis project examining demographic characteristics and living conditions of recent graduates through confidence interval estimation and data visualization.

## Project Overview

GradInsights analyzes data from recent professional graduates to create a comprehensive statistical profile covering age, household income, broadband access, and family status. Using confidence interval estimation techniques, the project provides reliable insights into the broader graduate population while quantifying the precision of these estimates through rigorous statistical methods.

## Key Features

- **Confidence Interval Analysis**: Implements 95% confidence intervals for all key metrics
- **Demographic Profiling**: Analyzes age, household income, broadband access, and parental status
- **Statistical Methodology**: Applies appropriate statistical techniques based on variable types
- **Data Visualization**: Creates multiple visualization types for clearer data interpretation
- **Sample Size Calculation**: Provides guidance on required sample sizes for future studies
- **Error Margin Quantification**: Explicitly calculates and displays error margins for all estimates

## Analysis Components

### Descriptive Statistics & Confidence Intervals

The project calculates and presents:

1. **Mean Age with CI**: Average age of recent graduates with 95% confidence bounds
2. **Mean Household Income with CI**: Average income levels with statistical uncertainty
3. **Broadband Access Proportion with CI**: Percentage of graduates with internet access
4. **Graduates with Children Proportion with CI**: Percentage of graduates who are parents

### Visualization Suite

For each metric, multiple visualization types are implemented:

- **Bar Charts**: Display means/proportions with error bars showing confidence intervals
- **Pie Charts**: Show proportional breakdowns of categorical variables 
- **Line Plots**: Present means with shaded confidence interval regions
- **Count Plots**: Show raw frequency distributions of key variables

## Key Findings

The analysis reveals:

1. **Age Profile**: The average graduate age is approximately 30 years with a narrow confidence interval
2. **Economic Status**: Average household income of approximately $75,000 with defined confidence bounds
3. **Digital Access**: About 62% of graduates have broadband internet access
4. **Family Status**: Approximately 53% of graduates have children

All findings include statistically rigorous confidence intervals to indicate estimate precision.

## File Structure

- `data_analysis.py`: Analyzes graduate age demographics
- `means_household_newgraduates.py`: Examines household income with confidence intervals
- `broadband_access.py`: Investigates internet accessibility among graduates
- `graduates_children.py`: Analyzes the proportion of graduates with children
- `visualizations_mean_ng.py`: Provides specialized visualizations for income data
- `methodology.py`: Documents statistical approaches and sample size calculations
- `illustrations.py`: Generates summary statistics
- `Professional.xlsx`: Dataset containing graduate information

## How to Run

1. Clone the repository
   ```
   git clone https://github.com/yourusername/GradInsights.git
   cd GradInsights
   ```

2. Install required packages
   ```
   pip install pandas numpy matplotlib seaborn scipy
   ```

3. Run individual analysis scripts
   ```
   python data_analysis.py
   python means_household_newgraduates.py
   python broadband_access.py
   python graduates_children.py
   ```

## Technologies Used

- **Python**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Statistical calculations
- **Matplotlib & Seaborn**: Data visualization
- **SciPy**: Statistical testing and confidence interval calculations

## Statistical Methodology

The project employs:

- **Z-statistic** based confidence intervals for proportions
- **T-statistic** based confidence intervals for means (where appropriate)
- Standard error calculations for all point estimates
- 95% confidence level for all interval estimates
- Appropriate formulas for categorical vs. continuous variables

## Future Work

- Implement hypothesis testing to compare graduate subgroups
- Add multivariate analysis to examine relationships between variables
- Create interactive dashboards for data exploration
- Include longitudinal data to track changes over time
- Expand the analysis to include employment outcomes and career trajectories

## Author

Adithya Sriramoju

## Acknowledgments

- The statistical community for established confidence interval methodologies
- The Python data science ecosystem for their powerful analytical tools
