# 📉 Unemployment Analysis in India using Python

## Project Overview
This project analyzes unemployment trends in India using real-world data. It focuses on understanding how unemployment rates vary over time, across regions, and by month. Data visualization techniques are used to present insights clearly and effectively.

## Objective
- Analyze unemployment trends over time in India
- Compare unemployment rates across different regions
- Study monthly variations in unemployment
- Understand relationships between employment indicators

## Technologies Used
Python, Pandas, NumPy, Matplotlib, Seaborn

## Project Structure
Unemployment-Analysis/
├── unemployment_analysis.py  
├── Unemployment_in_India_cleaned.csv  
├── images/  
│   ├── unemployment_trend.png  
│   ├── region_wise_unemployment.png  
│   ├── month_wise_unemployment.png  
│   └── correlation_heatmap.png  
└── README.md  

## Dataset Description
Unemployment_in_India_cleaned.csv contains unemployment statistics collected across various regions in India.

Columns:
- Date – Observation date  
- Region – State or region name  
- Estimated Unemployment Rate (%) – Percentage of unemployed individuals  
- Estimated Employed – Number of employed individuals  
- Estimated Labour Participation Rate (%) – Workforce participation percentage  
- Month_Name – Month of observation  

## Exploratory Data Analysis
- Time series analysis of unemployment rate
- Region-wise average unemployment comparison
- Month-wise unemployment trend analysis
- Correlation analysis among employment indicators

## Visualizations
- Line plot showing unemployment trend over time
- Bar chart comparing average unemployment by region
- Bar chart showing monthly unemployment averages
- Heatmap displaying correlations between employment variables

## How to Run the Project
1. Navigate to the project directory  
2. Run the Python script using:  
   python unemployment_analysis.py

## Results
The analysis highlights significant variations in unemployment rates across regions and months, providing insights into seasonal and regional employment patterns in India.

## Conclusion
This project demonstrates how Python-based data analysis and visualization can be used to study socio-economic indicators like unemployment and extract meaningful insights from data.

## Future Enhancements
- Add year-wise comparison analysis
- Perform predictive modeling on unemployment trends
- Integrate interactive dashboards using Plotly or Streamlit

## Author
Prajwal Ghawat

## License
Educational use only
