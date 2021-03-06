import numpy as np
import matplotlib.pyplot as plt
import os

# Set up the path to the Data directory
dataPath = os.path.dirname(os.path.abspath(__file__)) + '/../Data'

# Import data for plot
time, mathFxn = np.genfromtxt((dataPath + '/2a.csv'), unpack=True, delimiter=',', skiprows=1, usecols=(0,1))

# Do some math
# f = 100 #Hz
# A = .6 / 2 # 600 mVpp / 2 makes wave amplitude
# inputSignal = -1 * A * np.sin(2 * np.pi * f * time)

# outputSignal = inputSignal - mathFxn

# Smoothed line for plot?
smoothFxn = np.poly1d(np.polyfit(time, mathFxn, 30))

# Plot the stuff
plt.figure()
plt.plot(time * 10**3, mathFxn, 'r,')
# plt.plot(time, smoothFxn(time))
# plt.plot(time, inputSignal)
# plt.plot(time, outputSignal, 'g')
plt.ylim(-2.5, 2.5)
plt.grid(True)
plt.title("Input/Output Signal Difference")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude (V)")

plt.show()
