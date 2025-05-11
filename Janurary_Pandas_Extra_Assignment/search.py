import pandas as pd
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Sample DataFrame
data_df = pd.read_csv('rawdata/LMG_Inspection_Violations_of_Failed_Restaurants.csv')

# Create textbox widget for numeric input
textbox = widgets.IntText(description="Enter Zip Code: ", style={'description_width':'initial'})

# Create output widget for displaying results
output = widgets.Output()

# Function to search DataFrame and update plot
def search_and_plot(value):
    with output:
        output.clear_output()
        if value is not None:
            # Filter DataFrame based on textbox value
            filtered_df = data_df[data_df['premise_zip'] == value]
            zipcode_count = filtered_df["premise_zip"].count()

            if not filtered_df.empty:
                # Create bar plot
                plt.bar(filtered_df.index, filtered_df['score'], color=["red"])
                plt.xlabel(f"Zip Code {value} \n {zipcode_count} \n  Failed Inspections Found")
                plt.ylabel('Score')
                plt.title(f'You searched for Zip Code {value}')
                plt.axhline(y=10, xmin=0, xmax=100, color='b', linestyle='-')
                plt.axhline(y=20, xmin=0, xmax=100, color='b', linestyle='-')
                plt.axhline(y=30, xmin=0, xmax=100, color='b', linestyle='-')
                plt.axhline(y=40, xmin=0, xmax=100, color='b', linestyle='-')
                plt.axhline(y=50, xmin=0, xmax=100, color='b', linestyle='-')
                plt.axhline(y=60, xmin=0, xmax=100, color='b', linestyle='-')
                plt.axhline(y=70, xmin=0, xmax=100, color='b', linestyle='-')
                plt.axhline(y=80, xmin=0, xmax=100, color='b', linestyle='-')
                plt.show()
            else:
                 print(f"No matching Zip Codes found for {value}.")

# Observe changes in textbox value
def on_value_change(change):
    search_and_plot(change['new'])
    

textbox.observe(on_value_change, names='value')


# Group by 'Premise Zip Code'
filtered_df = data_df[data_df['score'] < 85]
grouped = filtered_df.groupby('premise_zip')
zipcode_count = filtered_df["premise_zip"].count()


def plot():
    plt.bar(x=filtered_df['premise_zip'], height=filtered_df['score'], color=["red"])
    plt.ylabel("Scores")
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

# Display widgets
display(textbox, output)