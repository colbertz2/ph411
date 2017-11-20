import matplotlib.pyplot as plt
import numpy as np

# Import data from file and skip header rows
time_wave, input_wave, output_wave = np.genfromtxt('../Data/4c_waveform.csv', delimiter=',', usecols=(0,1,3), skiprows=1, unpack=True)

time_fftInput, amplitude_fftInput = np.genfromtxt('../Data/4c_fft1.csv', delimiter=',', usecols=(0,1), skiprows=1, unpack=True)

time_fftOutput, amplitude_fftOutput= np.genfromtxt('../Data/4c_fft2.csv', delimiter=',', usecols=(0,1), skiprows=1, unpack=True)

# Make time more readable
us = 10**6 # Multiply seconds by us to get microseconds
ms = 10**3 # Multiply seconds by ms to get milliseconds

# Plot some stuff
plt.title("RC Circuit with AM Sine Wave Input")
plt.figure(1)
plt.subplot(311)
plt.plot(time_wave * ms, input_wave, 'b', label="Input Waveform")
plt.plot(time_wave * ms, output_wave, 'r', label="Filtered Waveform")
plt.grid(True)
plt.xlabel("Time (ms)")
plt.ylabel("Potential (V)")
plt.legend()

plt.subplot(312)
plt.plot(time_fftInput, amplitude_fftInput, 'b', label="Input Power Distribution")
plt.grid(True)
# plt.xlabel("Time (ms)")
# plt.ylabel("Potential (V)")
plt.legend()

plt.subplot(313)
plt.plot(time_fftOutput, amplitude_fftOutput, 'r', label="Filtered Power Distribution")
plt.grid(True)
# plt.xlabel("Time (ms)")
# plt.ylabel("Potential (V)")
plt.legend()

plt.tight_layout()

# Set plot formatting
# plt.xlim(0.7,0.95)
# plt.ylim(0.,130.)
# plt.grid(True)

# Labels and text
# plt.xlabel("Time (ms)")
# plt.ylabel("Potential (V)")
# plt.title("Voltage of Capacitor with Square Wave Input")
# plt.legend()

# Show the plot
plt.show()