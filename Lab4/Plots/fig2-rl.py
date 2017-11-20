import numpy as np
import matplotlib.pyplot as plt

################################################################################
############################       RL CIRCUIT       ############################
################################################################################

# Import the data
frequency_kHz, inputPkPk, outputPkPk, phase_us = np.genfromtxt("Lab4/Data/rl.csv",delimiter=',', skiprows=2, usecols=(0,1,2,3), unpack=True)

# Some other numbers that don't get imported
resistor = 10**3 #Ohms
inductor = 10**(-2) #Henries

# Convert frequency and phase to other units
frequency = frequency_kHz * 1000 #Hz
frequency_angular = frequency * 2 * np.pi
phase_s = phase_us * 10**(-6)

# Find the transmission function
Av = outputPkPk / inputPkPk
Av_theory = (frequency_angular * inductor / resistor) / np.sqrt(1 + (frequency_angular * inductor / resistor)**2)

# Find the phase difference
Phi = 2 * 180 * phase_s * frequency
Phi_theoretical = ((np.pi / 2) - np.arctan(frequency_angular * inductor / resistor)) * 180 / np.pi

# Make a Bode plot
plt.figure()
plt.subplot(211)
plt.plot(np.log10(frequency), 20 * np.log10(Av), 'ro')
plt.plot(np.log10(frequency), 20 * np.log10(Av_theory), 'bo')
plt.xlabel("Input Frequency " + r'$log(\nu)$' + " (Hz)")
plt.ylabel("Transmission Ratio " + r'$20*log(A(\nu))$' + " (dB)")
plt.title("Amplitude")
plt.grid(True)

plt.subplot(212)
plt.plot(np.log10(frequency), Phi, 'ro')
plt.plot(np.log10(frequency), Phi_theoretical, 'bo')
plt.xlabel("Input Frequency " + r'$log(\nu)$' + " (Hz)")
plt.ylabel("Phase Difference " + r'$\phi(\nu)$' + " (deg)")
plt.title("Phase")

plt.tight_layout()
plt.grid(True)

# Show plots
plt.show()