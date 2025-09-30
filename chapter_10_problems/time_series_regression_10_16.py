# time_series_regression_10_16.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Load the wildfires dataset
wildfires = pd.read_csv("wildfires.csv")

# Preview the first few rows
print(wildfires.head())

# Clean up column names (remove quotes if they exist)
wildfires.columns = wildfires.columns.str.strip().str.replace('"', '')

# Extract x (Date) and y (Acres Burned)
x = wildfires["Date"]
y = wildfires["Acres Burned"]

# Run a simple linear regression
linear_regression = stats.linregress(x, y)

print(f"Slope: {linear_regression.slope}")
print(f"Intercept: {linear_regression.intercept}")
print(f"R-squared: {linear_regression.rvalue ** 2}")

# Add regression line to DataFrame for plotting
wildfires["Trend"] = linear_regression.slope * x + linear_regression.intercept

# Plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Date", y="Acres Burned", data=wildfires, label="Observed")
sns.lineplot(x="Date", y="Trend", data=wildfires, color="red", label="Trend Line")

plt.title("U.S. Wildfires - Acres Burned (2000–2015)")
plt.xlabel("Year")
plt.ylabel("Acres Burned")
plt.legend()
plt.show()