import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data_df = pd.read_csv('rawdata/LMG_Inspection_Violations_of_Failed_Restaurants.csv')

# Group by 'Premise Zip Code'
filtered_df = data_df[data_df['score'] < 85]
grouped = filtered_df.groupby('premise_zip')

# Iterate through groups
#for name, group in grouped:
#    print(f"Group: {name}")
    # Iterate through rows in each group
#    for index, row in group.iterrows():
        
#        print(f"Zip Code: {row['premise_zip']}, Score: {row['score']}, Critical Violation: {row['critical_yn']}")
#effect = filtered_df["premise_zip"].value_counts()
#filtered_df.plot(kind="bar", x="premise_zip", y="score", title="Inspections by Zip Code")
#plt.plot()
plt.bar(x=filtered_df['premise_zip'], height=filtered_df['score'], color=["red"])
plt.ylabel("Number of Failed Inspections")
plt.xlabel("Zip Code")
plt.title("Inspections by Zip Code")
#plt.figure(figsize=(8,6))
plt.show()