import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('TBI-Data.csv')

# Convert columns to numeric
df['GCSTot'] = pd.to_numeric(df['GCSTot'], errors='coerce')
df['TFCDays'] = pd.to_numeric(df['TFCDays'], errors='coerce')

df = df[df['TFCDays'] <= 150]

# Remove rows with invalid values
df = df[~df['GCSTot'].isin([77, 88, 999]) & ~df['TFCDays'].isin([7777, 9999])]
df = df.dropna(subset=['GCSTot', 'TFCDays'])

x = df['GCSTot']
y = df['TFCDays']

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

# Plot Graph
plt.plot(x_line, y_line, c='red')
plt.title("GCSTot vs. TFCDays")
plt.xlabel('GCS Total')
plt.ylabel('TFCDays')
plt.figtext(0.5, 0.02, f"Equation: {equation}; R-Squared: {r_squared:.3f}", ha="center", fontsize=12, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
plt.show()

# Scatter Graph
plt.scatter(x, y)
plt.title("GCSTot vs. TFCDays")
plt.xlabel('GCS Total')
plt.ylabel('TFCDays')
plt.figtext(0.5, 0.02, f"Equation: {equation}; R-Squared: {r_squared:.3f}", ha="center", fontsize=12, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
plt.show()