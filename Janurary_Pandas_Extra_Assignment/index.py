import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data_df = pd.read_csv('rawdata/LMG_Inspection_Violations_of_Failed_Restaurants.csv')

# Group by 'Premise Zip Code'
filtered_df = data_df[data_df['score'] < 85]
grouped = filtered_df.groupby('premise_zip')
zipcode_count = filtered_df["premise_zip"].count()



plt.bar(x=filtered_df['premise_zip'], height=filtered_df['score'], color=["red"])
plt.ylabel("Number of Failed Inspections")
plt.xlabel(f"Zip Code \n {zipcode_count} \n  Zip Codes Found")
plt.title("Inspections by Zip Code")
plt.axhline(y=10, xmin=0, xmax=100, color='b', linestyle='--')
plt.axhline(y=20, xmin=0, xmax=100, color='b', linestyle='--')
plt.axhline(y=30, xmin=0, xmax=100, color='b', linestyle='--')
plt.axhline(y=40, xmin=0, xmax=100, color='b', linestyle='--')
plt.axhline(y=50, xmin=0, xmax=100, color='b', linestyle='--')
plt.axhline(y=60, xmin=0, xmax=100, color='b', linestyle='--')
plt.axhline(y=70, xmin=0, xmax=100, color='b', linestyle='--')
plt.axhline(y=80, xmin=0, xmax=100, color='b', linestyle='--')
plt.show()