import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('TBI-Data.csv')

# Convert columns to numeric
df['GCSTot'] = pd.to_numeric(df['GCSTot'], errors='coerce')
df['ALCDrinks'] = pd.to_numeric(df['ALCDrinks'], errors='coerce')
df['Drugs'] = pd.to_numeric(df['Drugs'], errors='coerce')
df['MJUse'] = pd.to_numeric(df['MJUse'], errors='coerce')

substances = ['ALCDrinks', 'Drugs', 'MJUse']

# Remove rows with invalid values
df = df[~df['ALCDrinks'].isin([666, 777, 888, 999]) & ~df['GCSTot'].isin([77, 88, 999])]
df = df.dropna(subset=['GCSTot', 'ALCDrinks', 'Drugs', 'MJUse'])

substances = ['ALCDrinks', 'Drugs', 'MJUse']

for substance in substances:
    df = df[~df[substance].isin([66, 77, 88, 99, 999])]
    x = df['GCSTot']
    y = df[substance]

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
    plt.title(f"GCSTot vs. {substance}")
    plt.xlabel('GCS Total')
    plt.ylabel(substance)
    plt.figtext(0.5, 0.02, f"Equation: {equation}; R-Squared: {r_squared:.3f}", ha="center", fontsize=12, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
    plt.show()

    # Scatter Graph
    if substance == 'ALCDrinks':
        plt.scatter(x, y)
        plt.title(f"GCSTot vs. {substance}")
        plt.xlabel('GCS Total')
        plt.ylabel(substance)
        plt.figtext(0.5, 0.02, f"Equation: {equation}; R-Squared: {r_squared:.3f}", ha="center", fontsize=12, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
        plt.show()