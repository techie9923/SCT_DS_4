📌 Project Title: Traffic Accident Analysis Based on Road, Weather, and Time Conditions

🚀 Objective
The goal of this project is to analyze traffic accident data to identify critical patterns influenced by:
Road conditions
Weather conditions
Time of day and week
Through this, we aim to visualize accident hotspots and discover the main contributing factors to improve road safety and awareness.

📁 Dataset Description
The dataset contains detailed records of real-world traffic accidents, including:
Date & Time of accident
Weather & Road Conditions
Lighting Conditions
Crash Types
Contributing Causes
Injury Severity

Key columns used in the project:
crash_date, crash_hour, crash_day_of_week, crash_month
weather_condition, roadway_surface_cond, lighting_condition
prim_contributory_cause, injuries_total, injuries_fatal

🔍 Analysis Performed
1. Data Preprocessing
Converted date-time columns.
Removed rows with missing or invalid entries in critical fields.

2. Time-Based Accident Patterns
Plotted accidents by hour, day of week, and month.
Observed peak times for crashes (e.g., evenings, weekends).

3. Weather & Road Surface Analysis
Identified weather conditions with the highest number of accidents.
Dry conditions had the most accidents (due to frequency), but wet/icy roads had higher injury ratios.

4. Lighting Condition Study
Compared accident counts during daylight vs nighttime.
Darkness (even with road lights) increases risk.

5. Top 10 Contributing Factors
Found top causes like:
Failing to yield
Distracted driving
Following too closely

📊 Visualizations
Accidents by Hour of Day
Accidents by Day of Week
Weather Conditions vs Accidents
Road Surface Conditions
Lighting Conditions
Contributing Factors (Top 10)

💡 Insights & Conclusions
Most accidents occur during daytime and rush hours.
Clear weather and dry roads still dominate crash stats due to traffic volume.
Night crashes are fewer in number but more severe.
Human error is the top contributor, not environment.

🛠 Tech Stack
Python
Pandas
Matplotlib & Seaborn
Jupyter Notebook (or .py script)

🧠 Skills Applied
Data cleaning and transformation
Exploratory data analysis (EDA)
Data visualization and interpretation
Real-world dataset handling
