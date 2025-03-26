import pandas as pd
import scipy.stats as stats

data = pd.read_excel("Professional.xlsx")

summary = data.describe()

print(summary)
