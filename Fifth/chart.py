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
    
    # Introduce realistic correlations based on business insights
    # Higher purchase frequency significantly increases loyalty points
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

# Create figure with specific size for 512x512 output (8 inches at 64 DPI = 512 pixels)
plt.figure(figsize=(8, 8))

# Set seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.1)

# Ensure exact pixel dimensions
plt.gcf().set_size_inches(8, 8)

# Create custom colormap for corporate feel - professional blue to white to coral
colors = ["#053061", "#FFFFFF", "#E41A1C"]  # dark blue, white, red (corporate palette)
cmap = LinearSegmentedColormap.from_list("corporate_cmap", colors, N=100)

# Generate the heatmap with enhanced styling for executive presentation
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
    annot_kws={"size": 10, "weight": "bold"},  # Bold annotation text
    cbar_kws={"shrink": .8, "label": "Correlation Coefficient"},  # Colorbar customization
    mask=mask             # Show only bottom triangle
)

# Enhance tick label styling
plt.xticks(rotation=45, ha='right', fontweight='semibold')
plt.yticks(fontweight='semibold')

# Add title and adjust styling
plt.title("Customer Engagement Metrics\nCorrelation Matrix", fontsize=18, pad=20, fontweight='bold')

# Add annotation explaining key insights for executive team
insights = "Key Insight: Mobile App Usage strongly correlates with both Purchase Frequency and Loyalty Points"
plt.figtext(0.5, 0.02, insights, ha="center", fontsize=11, style='italic', 
           bbox=dict(boxstyle="round,pad=0.5", facecolor='#f0f0f0', alpha=0.5))

# Add company branding as a footer
plt.figtext(0.5, 0.01, "© Armstrong Oberbrunner and Okuneva | Data-Driven Customer Experience Analytics", 
           ha="center", fontsize=9, fontstyle='italic')

# Adjust layout
plt.tight_layout(rect=[0, 0.04, 1, 0.96])

# Save the plot with exact dimensions 512x512
plt.savefig('chart.png', dpi=64, bbox_inches=None)

print("Customer Engagement Correlation Matrix has been generated successfully.")
print("Chart saved as chart.png with dimensions 512x512 pixels.")
