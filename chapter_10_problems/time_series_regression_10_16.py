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
import matplotlib.ticker as mtick

plt.figure(figsize=(10, 6))
sns.scatterplot(x="Date", y="Acres Burned", data=wildfires, label="Observed")
sns.lineplot(x="Date", y="Trend", data=wildfires, color="red", label="Trend Line")

plt.title(f"U.S. Wildfires - Acres Burned ({wildfires['Date'].min()}–{wildfires['Date'].max()})")
plt.xlabel("Year")
plt.ylabel("Acres Burned")

# Format y-axis in millions
plt.gca().yaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f'{x*1e-6:.1f}M')
)

# Add regression equation and R² to the chart
equation_text = (
    f"y = {linear_regression.slope:.0f}x + {linear_regression.intercept:.0f}\n"
    f"R² = {linear_regression.rvalue**2:.2f}"
)
plt.text(wildfires["Date"].min() + 1,
         wildfires["Acres Burned"].max()*0.9,
         equation_text,
         fontsize=10, color="black",
         bbox=dict(facecolor="white", alpha=0.5))

plt.legend()
plt.show()