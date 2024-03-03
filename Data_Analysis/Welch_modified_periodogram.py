import pandas as pd
import numpy as np
from scipy.signal import welch, firwin, lfilter
import matplotlib.pyplot as plt

# Load your data
df = pd.read_csv('DataCH4/SignalData.csv')  # Adjust the path as necessary

# Extract specific columns
sequence_numbers = df['Sequence Number n']  # Adjust column name as necessary
eeg_values = df['EEG (V)']  # Adjust column name as necessary

# Design the low-pass filter (assuming sampling rate is 1000 Hz, cutoff is 50 Hz)
fs = 1000  # Sampling rate
cutoff = 50  # Cutoff frequency in Hz
numtaps = 101  # Number of filter taps (filter length)
window = ('kaiser', 8.6)  # Kaiser window with beta parameter
taps = firwin(numtaps, cutoff, window=window, fs=fs)

# Apply the filter to the EEG signal data
filtered_eeg_values = lfilter(taps, 1.0, eeg_values)

# Use Welch's method to compute the power spectral density on the filtered data
frequencies, psd_values = welch(filtered_eeg_values, fs, window='hamming', nperseg=2000, noverlap=None, average='mean')

# Filter frequencies and PSD values to only include frequencies in the range 0 to 40 Hz
mask = (frequencies >= 0) & (frequencies <= 40)
filtered_frequencies = frequencies[mask]
filtered_psd_values = psd_values[mask]

# Plot the filtered power spectral density
plt.semilogy(filtered_frequencies, filtered_psd_values)
plt.title('Welch Periodogram of Filtered EEG Signal')
plt.xlabel('Frequency [Hz]')
plt.ylabel('PSD [V^2/Hz]')
plt.xlim(0, 40)  # This ensures that the x-axis only shows the range from 0 to 40 Hz
plt.show()
