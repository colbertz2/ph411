import matplotlib.pyplot as plt
import numpy as np

# Import data from file and skip header rows
time, inputVoltage, capacitorVoltage = np.genfromtxt('../Data/1b_waveform.csv', delimiter=',', usecols=(6,7,10), skiprows=1, unpack=True)

# Fix the time offset
time = time - min(time)

# Make time more readable
us = 10**6 # Multiply seconds by us to get microseconds

# Plot some stuff
plt.plot(time * us, inputVoltage, label="Input Voltage")
plt.plot(time * us, capacitorVoltage, label="$10 nF$ Capacitor")

# # Set plot formatting
# plt.xlim(0.7,0.95)
# plt.ylim(0.,130.)
plt.grid(True)

# # Labels and text
plt.xlabel("Time ($\mu s$)")
plt.ylabel("Potential (V)")
plt.title("Voltage of Capacitor with Square Wave Input")
plt.legend(loc=3)

# Show the plot
plt.show()