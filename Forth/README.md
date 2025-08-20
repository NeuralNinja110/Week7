# Supply Chain Analytics: Correlation Matrix Visualization

## Contact Information
**Email:** 23f1001177@ds.study.iitm.ac.in

## Project Overview
This repository contains a correlation analysis of key supply chain metrics for OptimalFlow Logistics, a supply chain consulting firm helping a major automotive manufacturer optimize their procurement and inventory management processes.

## Business Context
A major automotive manufacturer has engaged OptimalFlow Logistics to analyze their supplier performance data from 68 different procurement transactions over the past quarter. The company wants to understand how different supply chain variables interact with each other to make data-driven decisions about supplier selection, inventory planning, and cost optimization.

The analysis examines relationships between the following critical supply chain metrics:
- **Supplier_Lead_Time**: Days from order placement to delivery
- **Inventory_Levels**: Current stock quantities (units)
- **Order_Frequency**: Number of orders placed per month
- **Delivery_Performance**: On-time delivery rate (%)
- **Cost_Per_Unit**: Unit cost in dollars ($)

## Repository Contents
- **README.md**: This file, containing project information and email contact
- **correlation.csv**: The correlation matrix data generated from Excel's Data Analysis ToolPak
- **heatmap.png**: Visualization of the correlation matrix using Excel's conditional formatting with Red-White-Green color scheme

## Key Findings
The correlation matrix reveals several important relationships between supply chain variables:

1. **Strong negative correlation between Supplier Lead Time and Delivery Performance**: Suppliers with longer lead times tend to have worse on-time delivery rates.

2. **Strong positive correlation between Supplier Lead Time and Cost Per Unit**: Longer lead times are associated with higher costs, suggesting that expediting might be increasing costs.

3. **Strong positive correlation between Order Frequency and Delivery Performance**: More frequent ordering is associated with better delivery performance.

4. **Moderate negative correlation between Inventory Levels and Order Frequency**: Higher inventory levels are associated with less frequent ordering.

## Business Recommendations
Based on the correlation analysis, OptimalFlow Logistics recommends:

1. **Supplier Segmentation**: Categorize suppliers based on lead time and delivery performance to identify which suppliers need improvement plans.

2. **Order Frequency Optimization**: Consider increasing order frequency for critical components to improve delivery performance.

3. **Lead Time Reduction**: Work with key suppliers to reduce lead times, which could simultaneously improve delivery performance and reduce costs.

4. **Inventory Strategy Review**: Develop tailored inventory strategies for different supplier segments based on their performance characteristics.
