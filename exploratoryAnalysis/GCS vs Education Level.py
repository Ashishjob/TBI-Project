import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('TBI-Data.csv')

# Convert columns to numeric
df['GCSTot'] = pd.to_numeric(df['GCSTot'], errors='coerce')
df['EDUCATION'] = pd.to_numeric(df['EDUCATION'], errors='coerce')

# Replace 'Other Edcucation' with 10
df['EDUCATION'] = df['EDUCATION'].replace(77, 10)

# Filter data to only include rows with valid values
df = df[df['EDUCATION'] < 10]

# Remove rows with invalid values
df = df[~df['EDUCATION'].isin([777, 999]) & ~df['GCSTot'].isin([77, 88, 999])]
df = df.dropna(subset=['GCSTot', 'EDUCATION'])

x = df['GCSTot']
y = df['EDUCATION']

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
plt.title("GCSTot vs. EDUCATION")
plt.xlabel('GCS Total')
plt.ylabel('Education Level')
plt.show()

# Scatter Graph
plt.scatter(x, y)
plt.title("GCSTot vs. EDUCATION")
plt.xlabel('GCS Total')
plt.ylabel('Education Level')
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9], ['< 8th Grade', '8th Grade', '9 - 11th Grade', 'High School', 'Some College', 'Associate Degree', 'Bachelor Degree', 'Master Degree', 'Doctorate Degree'])
plt.figtext(0.5, 0.02, f"Equation: {equation}; R-Squared: {r_squared:.3f}", ha="center", fontsize=12, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
plt.show()