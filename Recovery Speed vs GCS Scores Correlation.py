import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('TBI-Data.csv')

# Convert columns to numeric
df['TFCDays'] = pd.to_numeric(df['TFCDays'], errors='coerce')
df['GCSEye'] = pd.to_numeric(df['GCSEye'], errors='coerce')
df['GCSVer'] = pd.to_numeric(df['GCSVer'], errors='coerce')
df['GCSMot'] = pd.to_numeric(df['GCSMot'], errors='coerce')
df['GCSTot'] = pd.to_numeric(df['GCSTot'], errors='coerce')

# Remove rows with invalid values
df = df[df['TFCDays'] <= 150]
df = df.dropna(subset=['TFCDays', 'GCSEye', 'GCSVer', 'GCSMot', 'GCSTot'])

GCStype = ['GCSEye', 'GCSVer', 'GCSMot', 'GCSTot']

for GCStype in GCStype:
    if GCStype == 'GCSEye':
        df = df[df['GCSEye'] <= 4]
    elif GCStype == 'GCSVer':
        df = df[df['GCSVer'] <= 5]
    elif GCStype == 'GCSMot':
        df = df[df['GCSMot'] <= 6]
    elif GCStype == 'GCSTot':
        df = df[df['GCSTot'] <= 15]

    x = df['TFCDays']
    y = df[GCStype]

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
    plt.title(f"TFCDays vs. {GCStype}")
    plt.xlabel('TFCDays')
    plt.ylabel(GCStype)
    if GCStype != 'GCSTot':
        plt.ylim(bottom = 0.5)
    else:
        plt.ylim(bottom = 2)
    plt.figtext(0.5, 0.02, f"Equation: {equation}; R-Squared: {r_squared:.3f}", ha="center", fontsize=12, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
    plt.show()

    # Scatter Graph
    plt.scatter(x, y)
    plt.title(f"TFCDays vs. {GCStype}")
    plt.xlabel('TFCDays')
    plt.ylabel(GCStype)
    if GCStype != 'GCSTot':
        plt.ylim(bottom = 0.5)
    else:
        plt.ylim(bottom = 2)
    plt.figtext(0.5, 0.02, f"Equation: {equation}; R-Squared: {r_squared:.3f}", ha="center", fontsize=12, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
    plt.show()