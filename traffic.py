import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel(r"project\trfficacc.xlsx")

# Convert crash_date to datetime
df['crash_date'] = pd.to_datetime(df['crash_date'], errors='coerce')

# Drop rows with missing important values
df.dropna(subset=['crash_date', 'weather_condition', 'lighting_condition', 'roadway_surface_cond'], inplace=True)

# --- Accidents by Hour ---
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='crash_hour', palette='viridis')
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

# --- Accidents by Day of Week ---
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='crash_day_of_week', palette='Set2')
plt.title("Accidents by Day of Week")
plt.xlabel("Day (1=Monday, 7=Sunday)")
plt.ylabel("Number of Accidents")
plt.tight_layout()
plt.show()

# --- Weather Conditions ---
plt.figure(figsize=(12,6))
sns.countplot(data=df, y='weather_condition', order=df['weather_condition'].value_counts().index, palette='coolwarm')
plt.title("Accidents by Weather Condition")
plt.xlabel("Number of Accidents")
plt.tight_layout()
plt.show()

# --- Road Surface Conditions ---
plt.figure(figsize=(12,6))
sns.countplot(data=df, y='roadway_surface_cond', order=df['roadway_surface_cond'].value_counts().index, palette='mako')
plt.title("Accidents by Road Surface Condition")
plt.xlabel("Number of Accidents")
plt.tight_layout()
plt.show()

# --- Lighting Conditions ---
plt.figure(figsize=(10,5))
sns.countplot(data=df, y='lighting_condition', order=df['lighting_condition'].value_counts().index, palette='flare')
plt.title("Accidents by Lighting Condition")
plt.xlabel("Number of Accidents")
plt.tight_layout()
plt.show()

# --- Top 10 Contributing Factors ---
plt.figure(figsize=(12,6))
top_causes = df['prim_contributory_cause'].value_counts().head(10)
sns.barplot(x=top_causes.values, y=top_causes.index, palette='Set1')
plt.title("Top 10 Contributing Factors")
plt.xlabel("Number of Accidents")
plt.ylabel("Cause")
plt.tight_layout()
plt.show()


