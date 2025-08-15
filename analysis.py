# Email: 23f1001177@ds.study.iitm.ac.in
# Interactive Data Analysis Notebook
# Demonstrating variable relationships with Marimo

import marimo as mo
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def __():
    # Cell 1: Introduction and Data Generation
    # This cell introduces the analysis and generates synthetic data
    mo.md(
        """
        # Interactive Data Analysis: Temperature vs Energy Consumption
        
        This notebook demonstrates the relationship between temperature and energy consumption
        using interactive widgets and dynamic visualizations.
        
        **Author**: 23f1001177@ds.study.iitm.ac.in  
        **Purpose**: Research institution data analysis demonstration
        """
    )
    return


def __():
    # Cell 2: Data Generation with Dependencies
    # This cell creates synthetic data that will be used by subsequent cells
    np.random.seed(42)
    
    # Generate synthetic temperature data (Celsius)
    days = 365
    temperature = 15 + 10 * np.sin(2 * np.pi * np.arange(days) / 365) + np.random.normal(0, 3, days)
    
    # Generate energy consumption data (kWh) - inversely related to temperature
    # Higher consumption when it's cold (heating) or very hot (cooling)
    base_consumption = 50
    heating_factor = np.maximum(0, 18 - temperature) * 2  # Heating when below 18°C
    cooling_factor = np.maximum(0, temperature - 25) * 1.5  # Cooling when above 25°C
    energy_consumption = base_consumption + heating_factor + cooling_factor + np.random.normal(0, 5, days)
    
    # Create DataFrame
    df = pd.DataFrame({
        'day': range(1, days + 1),
        'temperature': temperature,
        'energy_consumption': energy_consumption,
        'month': [(i // 30) + 1 for i in range(days)]  # Approximate months
    })
    
    mo.md(f"**Data Generated**: {len(df)} days of temperature and energy consumption data")
    return df,


def __(df):
    # Cell 3: Interactive Slider Widget
    # This cell creates an interactive slider to filter data by temperature range
    # Depends on: df from Cell 2
    
    temp_range_slider = mo.ui.range_slider(
        start=int(df['temperature'].min()),
        stop=int(df['temperature'].max()),
        value=[int(df['temperature'].min()), int(df['temperature'].max())],
        label="Temperature Range (°C)",
        step=1
    )
    
    # Display the slider
    mo.md(
        f"""
        ## Interactive Temperature Filter
        
        Use the slider below to filter the data by temperature range:
        
        {temp_range_slider}
        """
    )
    return temp_range_slider,


def __(df, temp_range_slider):
    # Cell 4: Dynamic Data Filtering
    # This cell filters the data based on the slider selection
    # Depends on: df from Cell 2, temp_range_slider from Cell 3
    
    # Filter data based on slider values
    min_temp, max_temp = temp_range_slider.value
    filtered_df = df[
        (df['temperature'] >= min_temp) & 
        (df['temperature'] <= max_temp)
    ]
    
    # Calculate statistics for the filtered data
    stats = {
        'count': len(filtered_df),
        'avg_temp': filtered_df['temperature'].mean(),
        'avg_consumption': filtered_df['energy_consumption'].mean(),
        'correlation': filtered_df['temperature'].corr(filtered_df['energy_consumption'])
    }
    
    return filtered_df, stats


def __(filtered_df, stats, temp_range_slider):
    # Cell 5: Dynamic Markdown Output
    # This cell generates dynamic markdown based on the current widget state
    # Depends on: filtered_df and stats from Cell 4, temp_range_slider from Cell 3
    
    min_temp, max_temp = temp_range_slider.value
    
    # Create dynamic content based on current selection
    correlation_interpretation = ""
    if stats['correlation'] < -0.5:
        correlation_interpretation = "**Strong negative correlation** - Energy consumption decreases as temperature increases"
    elif stats['correlation'] < -0.2:
        correlation_interpretation = "**Moderate negative correlation** - Some inverse relationship between temperature and consumption"
    elif stats['correlation'] < 0.2:
        correlation_interpretation = "**Weak correlation** - Little linear relationship between variables"
    else:
        correlation_interpretation = "**Positive correlation** - Energy consumption increases with temperature"
    
    mo.md(
        f"""
        ## Analysis Results for Temperature Range: {min_temp}°C to {max_temp}°C
        
        ### Summary Statistics:
        - **Data Points**: {stats['count']} days
        - **Average Temperature**: {stats['avg_temp']:.1f}°C
        - **Average Energy Consumption**: {stats['avg_consumption']:.1f} kWh
        - **Correlation Coefficient**: {stats['correlation']:.3f}
        
        ### Interpretation:
        {correlation_interpretation}
        
        The filtered dataset shows how temperature variations affect energy consumption patterns.
        This analysis helps identify optimal temperature ranges for energy efficiency planning.
        """
    )
    return


def __(filtered_df):
    # Cell 6: Interactive Visualization
    # This cell creates a dynamic scatter plot of the filtered data
    # Depends on: filtered_df from Cell 4
    
    # Create interactive scatter plot
    fig = px.scatter(
        filtered_df, 
        x='temperature', 
        y='energy_consumption',
        title='Temperature vs Energy Consumption (Filtered Data)',
        labels={
            'temperature': 'Temperature (°C)',
            'energy_consumption': 'Energy Consumption (kWh)'
        },
        opacity=0.7,
        color='month',
        color_continuous_scale='viridis'
    )
    
    # Add trend line
    fig.add_trace(
        go.Scatter(
            x=filtered_df['temperature'].sort_values(),
            y=np.poly1d(np.polyfit(filtered_df['temperature'], filtered_df['energy_consumption'], 1))(filtered_df['temperature'].sort_values()),
            mode='lines',
            name='Trend Line',
            line=dict(color='red', dash='dash')
        )
    )
    
    fig.update_layout(
        width=800,
        height=500,
        showlegend=True
    )
    
    return mo.ui.plotly(fig)


def __(df):
    # Cell 7: Data Flow Documentation
    # This cell documents the data flow and dependencies between cells
    # Depends on: df from Cell 2 (for data description)
    
    mo.md(
        f"""
        ## Data Flow Documentation
        
        This notebook demonstrates cell dependencies and data flow in Marimo:
        
        ### Cell Dependencies:
        1. **Introduction Cell** → No dependencies (standalone)
        2. **Data Generation Cell** → Creates `df` with {len(df)} observations
        3. **Slider Widget Cell** → Depends on `df` for min/max temperature values
        4. **Data Filtering Cell** → Depends on `df` and `temp_range_slider`
        5. **Dynamic Markdown Cell** → Depends on `filtered_df`, `stats`, and `temp_range_slider`
        6. **Visualization Cell** → Depends on `filtered_df`
        7. **Documentation Cell** → Depends on `df` for metadata
        
        ### Variable Flow:
        ```
        df (raw data) 
        ↓
        temp_range_slider (user input)
        ↓
        filtered_df + stats (processed data)
        ↓
        dynamic_markdown + visualization (outputs)
        ```
        
        ### Interactive Features:
        - **Temperature Range Slider**: Filters data in real-time
        - **Dynamic Statistics**: Updates automatically with filter changes
        - **Interactive Plot**: Responsive scatter plot with trend line
        - **Contextual Documentation**: Adapts explanations to current data state
        
        This reactive programming model ensures all dependent cells update automatically
        when the slider value changes, demonstrating the power of Marimo's execution model.
        """
    )
    return


if __name__ == "__main__":
    # This allows the notebook to be run as a script
    print("Marimo notebook created successfully!")
    print("Run with: marimo run analysis.py")
