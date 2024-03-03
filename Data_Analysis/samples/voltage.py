import pandas as pd

def add_eeg_column(file_path, output_path):
    # Constants for the formula
    V_CC = 3.3  # Operation Voltage in Volts
    G_EEG = 41782  # EEG Sensor Gain
    n = 10  # Number of bits of the channel (assumed)

    # Load the CSV file
    data = pd.read_csv(file_path)

    # Calculate the EEG (V) column
    data['EEG (V)'] = ( ((data['Analog 4'] / (2**n ))- 0.5) * V_CC) / G_EEG

    # Save the dataframe to a new CSV file
    data.to_csv(output_path, index=False)
    print(f"File saved as '{output_path}'")

# Example usage
file_path = '/Users/omarg/Desktop/SYP/revolution-python-api/Analog4_O2_on_our_dev/27_11_2023__16_44_39.csv'  # Replace with the path to your input CSV file
output_path = '/Users/omarg/Desktop/SYP/revolution-python-api/Analog4_O2_on_our_dev/27_11_2023__16_44_39.csv'  # Replace with the desired path for the output CSV file
add_eeg_column(file_path, output_path)
