import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data from the CSV file
df = pd.read_csv('data.csv')

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Print the correlation matrix for reference
print("Correlation Matrix:")
print(correlation_matrix)

# Save the correlation matrix to CSV
correlation_matrix.to_csv('correlation.csv')

# Generate a heatmap visualization
plt.figure(figsize=(8, 8))  # Set figure size for 512x512 pixels
sns.set(style="white")

# Set figure to exact dimensions
plt.gcf().set_size_inches(8, 8)

# Create the heatmap with red-white-green color map
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
cmap = sns.diverging_palette(10, 130, as_cmap=True)  # Red-White-Green color palette (more Excel-like)

# Plot the heatmap
sns.heatmap(correlation_matrix, mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .8}, annot=True, fmt=".2f")

plt.title('Supply Chain Metrics Correlation Matrix', fontsize=16)
plt.tight_layout()

# Save the heatmap as PNG with 512x512 pixels
plt.savefig('heatmap.png', dpi=64, bbox_inches=None)

print("Analysis complete! Generated correlation.csv and heatmap.png")
