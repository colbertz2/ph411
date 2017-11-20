import matplotlib.pyplot as plt
import numpy as np

# Import data from file and skip header rows
frequency, input_v, output_v, phase_time = np.genfromtxt('../Data/Part5_crCircuit.csv', delimiter=',', usecols=(0,1,2,3), skiprows=2, unpack=True) # FREQUENCY IN KHZ

# Make time more readable
us = 10**6 # Multiply seconds by us to get microseconds
ms = 10**3 # Multiply seconds by ms to get milliseconds

Hz = 10**(3) # Multiply kHz by Hz to get Hz

# Circuit elements
R = 10 * 10**3
C = 10 * 10**(-9)

# Theoretical amplitude
theory_frequency = np.arange(1.0,10**6,1.0)
theory_Av = (2 * np.pi * theory_frequency * R * C) / np.sqrt((2 * np.pi * theory_frequency * R * C)**2 + 1)

# Theoretical phase difference
theory_phase = (-1 * np.arctan(2 * np.pi * theory_frequency * R * C) * 180 / np.pi) + 90

# Amplitude plot
plt.subplot(211)
plt.title("CR Circuit with Sine Wave Input \nAmplitude")
plt.plot(np.log10(frequency * Hz), 20 * np.log10(output_v / input_v), 'bo', label="Experimental")
plt.plot(np.log10(theory_frequency), 20 * np.log10(theory_Av), 'r', label="Theoretical")
plt.grid(True)
plt.xlabel("Input Frequency " + r'$log(\nu)$' + " (Hz)")
plt.ylabel("Transmission Ratio " + r'$20*log(A(\nu))$' + " (dB)")
plt.legend(loc=4)

# Phase plot
plt.subplot(212)
plt.title("Phase Difference")
plt.plot(np.log10(frequency * Hz), (2 * np.pi * phase_time * frequency * Hz / us) * (180 / np.pi), 'bo', label="Experimental")
plt.plot(np.log10(theory_frequency), theory_phase, 'r', label="Theoretical")
plt.grid(True)
plt.xlabel("Input Frequency " + r'$log(\nu)$' + " (Hz)")
plt.ylabel("Phase Difference " + r'$\phi(\nu)$' + " (deg)")
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