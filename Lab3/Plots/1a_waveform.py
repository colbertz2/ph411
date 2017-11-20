import matplotlib.pyplot as plt
import numpy as np

# Import data from file and skip header rows
time, amplitude = np.loadtxt('../Data/1a_waveform.csv', delimiter=',', usecols=(4,5), skiprows=2, unpack=True)

# Fix the time offset
time = time - min(time)

# Make time more readable
us = 10**6 # Multiply seconds by us to get microseconds

# Plot some stuff
plt.plot(time * us, amplitude, label="$10 nF$ Capacitor")

# # Set plot formatting
# plt.xlim(0.7,0.95)
# plt.ylim(0.,130.)
plt.grid(True)

# # Labels and text
plt.xlabel("Time ($\mu s$)")
plt.ylabel("Capacitor Voltage $V_c$")
plt.title("Voltage of Charging Capacitor in RC Circuit")
# plt.legend()

# Show the plot
plt.show()