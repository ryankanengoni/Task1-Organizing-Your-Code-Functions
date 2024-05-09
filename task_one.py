from typing import TextIO

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('x_y_coordinates.txt', header=None, names=['x', 'y'])

print("Column names in the dataset:", data.columns)

# Create a scatter plot of the data
plt.scatter(data['x'], data['y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.grid(True)
plt.show()
