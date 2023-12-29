import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('TBI-Data.csv')

# Convert columns to numeric
df['GCSTot'] = pd.to_numeric(df['GCSTot'], errors='coerce')
df['BMI'] = pd.to_numeric(df['BMI'], errors='coerce')

# Remove rows with invalid values
df = df[~df['GCSTot'].isin([77, 88, 999]) & ~df['BMI'].isin([888, 999])]
df = df.dropna(subset=['GCSTot', 'BMI'])

x = df['GCSTot']
y = df['BMI']

# Find coefficients
coefficients = np.polyfit(x, y, 1)

poly = np.poly1d(coefficients)

x_line = np.linspace(min(x), max(x))
y_line = poly(x_line)

# Find R^2 [accuracy]
corr_matrix = np.corrcoef(x, y)
corr_coeff = corr_matrix[0,1]
r_squared = corr_coeff**2

equation = (f"y = {coefficients[0]:.3f}x + {coefficients[1]:.3f}")

# Graph
plt.scatter(x, y)
plt.plot(x_line, y_line, c='red')
plt.title("GCSTot vs. BMI")
plt.xlabel('GCS Total')
plt.ylabel('BMI')
plt.figtext(0.5, 0.02, f"Equation: {equation}; R-Squared: {r_squared:.3f}", ha="center", fontsize=12, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
plt.show()

# # Scatter Graph
# plt.scatter(x, y)
# plt.title("GCSTot vs. BMI")
# plt.xlabel('GCS Total')
# plt.ylabel('BMI')
# plt.yticks([10, 20, 30, 40, 50])
# plt.figtext(0.5, 0.02, f"Equation: {equation}; R-Squared: {r_squared:.3f}", ha="center", fontsize=12, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
# plt.show()