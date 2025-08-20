import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set visual style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# Equipment Efficiency Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
efficiency_rates = [72.88, 72.2, 79.88, 75.14]
avg_efficiency = 75.02  # Calculated average
industry_target = 90

# Create DataFrame
df = pd.DataFrame({
    'Quarter': quarters,
    'Efficiency_Rate': efficiency_rates
})

# Calculate the gap from target
df['Gap_From_Target'] = industry_target - df['Efficiency_Rate']

# Print basic statistics
print("Equipment Efficiency Analysis - 2024")
print("-" * 40)
print(f"Data by Quarter: {dict(zip(quarters, efficiency_rates))}")
print(f"Average Efficiency Rate: {avg_efficiency}")
print(f"Industry Target: {industry_target}")
print(f"Average Gap from Target: {industry_target - avg_efficiency:.2f}")
print("-" * 40)

# Analyze trend
trend_direction = "improving" if efficiency_rates[-1] > efficiency_rates[0] else "declining"
peak_quarter = quarters[efficiency_rates.index(max(efficiency_rates))]
lowest_quarter = quarters[efficiency_rates.index(min(efficiency_rates))]
print(f"Overall Trend: {trend_direction}")
print(f"Peak Performance Quarter: {peak_quarter} ({max(efficiency_rates)})")
print(f"Lowest Performance Quarter: {lowest_quarter} ({min(efficiency_rates)})")

# Forecasting using simple linear regression
indices = np.array(range(1, len(efficiency_rates) + 1)).reshape(-1, 1)
values = np.array(efficiency_rates).reshape(-1, 1)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(indices, values)

# Forecast next 4 quarters
next_quarters = np.array(range(len(efficiency_rates) + 1, len(efficiency_rates) + 5)).reshape(-1, 1)
forecast = model.predict(next_quarters)
forecast = [round(val[0], 2) for val in forecast]

# Print forecast
print("\nEfficiency Rate Forecast:")
print("-" * 40)
for i, val in enumerate(forecast):
    print(f"Q{i+1} 2025: {val}")

# When would we reach the target if trend continues?
if model.coef_[0][0] > 0:  # If trend is positive
    quarters_to_target = int(np.ceil((industry_target - efficiency_rates[-1]) / model.coef_[0][0]))
    print(f"\nIf the current trend continues, the target of {industry_target} would be reached in approximately {quarters_to_target} quarters")
    target_date = datetime(2024, 12, 31)  # End of Q4 2024
    import datetime as dt
    for _ in range(quarters_to_target):
        target_date += dt.timedelta(days=90)  # Approximate quarter length
    print(f"Estimated achievement date: {target_date.strftime('%B %Y')}")
else:
    print("\nThe current trend is not positive, so the target will not be reached without intervention.")

# Calculate potential maintenance impact
# Assuming predictive maintenance can improve efficiency by 2% per quarter
maintenance_improvement = 2.0
quarters_with_maintenance = 4
improvement_projection = [efficiency_rates[-1]]
for i in range(quarters_with_maintenance):
    next_val = min(industry_target, improvement_projection[-1] + maintenance_improvement)
    improvement_projection.append(next_val)

print("\nPredictive Maintenance Impact Projection:")
print("-" * 40)
for i, val in enumerate(improvement_projection[1:], 1):
    print(f"Q{i} 2025: {val:.2f}")

quarters_to_target_with_maintenance = next((i for i, val in enumerate(improvement_projection) if val >= industry_target), None)
if quarters_to_target_with_maintenance:
    print(f"\nWith a predictive maintenance program, the target could be reached in {quarters_to_target_with_maintenance} quarters")
else:
    print("\nAdditional interventions may be needed to reach the target even with predictive maintenance")

# ---- VISUALIZATIONS ----

# 1. Bar chart showing quarterly performance vs target
plt.figure(figsize=(12, 6))
ax = sns.barplot(x='Quarter', y='Efficiency_Rate', data=df, palette='viridis')
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target: {industry_target}')
plt.axhline(y=avg_efficiency, color='b', linestyle='-.', label=f'Average: {avg_efficiency}')

# Add gap labels above bars
for i, bar in enumerate(ax.patches):
    gap = df['Gap_From_Target'].iloc[i]
    ax.text(
        bar.get_x() + bar.get_width()/2.,
        bar.get_height() + 1,
        f'Gap: {gap:.2f}',
        ha="center", va='bottom',
        color='red', fontweight='bold'
    )

plt.title('Equipment Efficiency Rate - 2024 Quarterly Performance', fontsize=16)
plt.ylabel('Efficiency Rate (%)', fontsize=14)
plt.xlabel('Quarter', fontsize=14)
plt.ylim(0, industry_target + 10)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('quarterly_performance.png')
plt.close()

# 2. Line chart with future projection
plt.figure(figsize=(14, 7))

# Historical data
plt.plot(quarters, efficiency_rates, marker='o', linewidth=2, markersize=10, label='Actual Efficiency')

# Extended quarters for forecasts
extended_quarters = quarters + [f'Q{i+1} 2025' for i in range(4)]

# Forecast based on trend
forecast_quarters = extended_quarters[4:]
plt.plot(forecast_quarters, forecast, marker='s', linestyle='--', linewidth=2, 
         markersize=8, label='Forecasted Trend')

# Forecast with maintenance program
plt.plot(forecast_quarters, improvement_projection[1:], marker='^', linestyle=':', linewidth=2,
         markersize=8, label='With Predictive Maintenance')

# Target line
plt.axhline(y=industry_target, color='r', linestyle='-', label=f'Industry Target: {industry_target}')

# Styling
plt.title('Equipment Efficiency Rate - Historical Data and Projections', fontsize=16)
plt.ylabel('Efficiency Rate (%)', fontsize=14)
plt.xlabel('Quarter', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(loc='lower right')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('efficiency_projections.png')
plt.close()

print("\nAnalysis complete. Visualizations have been saved.")
