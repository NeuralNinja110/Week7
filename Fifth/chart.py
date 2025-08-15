#!/usr/bin/env python3
# Customer Engagement Correlation Matrix
# Email: 23f1001177@ds.study.iitm.ac.in
# Created for Armstrong Oberbrunner and Okuneva

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic customer engagement metrics data
def generate_customer_data(num_customers=500):
    """Generate synthetic customer engagement metrics data"""
    
    # Customer engagement metrics
    metrics = {
        'Purchase Frequency': np.random.gamma(2, 2, num_customers),
        'Session Duration': np.random.normal(15, 5, num_customers),
        'Email Open Rate': np.random.beta(8, 3, num_customers) * 100,
        'Mobile App Usage': np.random.gamma(1.5, 3, num_customers),
        'Support Tickets': np.random.poisson(2, num_customers).astype(float),
        'Social Media Engagement': np.random.gamma(1, 3, num_customers),
        'Product Reviews': np.random.beta(1.5, 8, num_customers) * 10,
        'Loyalty Points': np.random.gamma(4, 500, num_customers)
    }
    
    # Introduce some realistic correlations
    # Higher purchase frequency slightly increases loyalty points
    metrics['Loyalty Points'] += metrics['Purchase Frequency'] * 300 + np.random.normal(0, 200, num_customers)
    
    # Mobile app users tend to have higher session durations
    metrics['Session Duration'] += metrics['Mobile App Usage'] * 0.8 + np.random.normal(0, 2, num_customers)
    
    # People who open emails tend to engage more on social media
    metrics['Social Media Engagement'] += metrics['Email Open Rate'] * 0.03 + np.random.normal(0, 1, num_customers)
    
    # People who write reviews tend to have more support tickets
    metrics['Support Tickets'] += metrics['Product Reviews'] * 0.3 + np.random.normal(0, 0.5, num_customers)
    
    return pd.DataFrame(metrics)

# Generate the data
customer_data = generate_customer_data(1000)

# Calculate the correlation matrix
corr_matrix = customer_data.corr()

# Create figure with specific size for 512x512 output
plt.figure(figsize=(8, 8))

# Set seaborn style for professional appearance
sns.set_style("white")
sns.set_context("paper", font_scale=1.2)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Create custom colormap for corporate feel - professional blue to white to red
colors = ["#0A2463", "#FFFFFF", "#FB3640"]  # dark blue, white, red
cmap = LinearSegmentedColormap.from_list("corporate_cmap", colors, N=100)

# Generate the heatmap
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
heatmap = sns.heatmap(
    corr_matrix,
    annot=True,           # Show the correlation values
    fmt=".2f",            # Format to 2 decimal places
    cmap=cmap,            # Custom corporate colormap
    vmin=-1,              # Min correlation value
    vmax=1,               # Max correlation value
    center=0,             # Center the colormap at zero
    square=True,          # Make cells square-shaped
    linewidths=0.5,       # Width of cell borders
    cbar_kws={"shrink": .8, "label": "Correlation Coefficient"},  # Colorbar customization
    mask=mask             # Show only bottom triangle
)

# Add title and adjust styling
plt.title("Customer Engagement Metrics Correlation Matrix", fontsize=16, pad=20, fontweight='bold')
plt.tight_layout()

# Add company branding as a footer
plt.figtext(0.5, 0.01, "© Armstrong Oberbrunner and Okuneva | Data-Driven Customer Experience Analytics", 
           ha="center", fontsize=10, fontstyle='italic')

# Save the plot with exact dimensions 512x512
plt.savefig('/workspaces/Week7/Fifth/chart.png', dpi=64, bbox_inches=None)

print("Customer Engagement Correlation Matrix has been generated successfully.")
print("Chart saved as chart.png with dimensions 512x512 pixels.")
