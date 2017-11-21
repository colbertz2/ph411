import numpy as np
import matplotlib.pyplot as plt
import os

# Set up the path to the Data directory
dataPath = os.path.dirname(os.path.abspath(__file__)) + '/../Data'

# Import data for plot
time, inSignal, outSignal = np.genfromtxt((dataPath + '/2b.csv'), unpack=True, delimiter=',', skiprows=1, usecols=(0,1,2))

# Plot some stuff
plt.figure()
plt.plot(time * 10**6, inSignal, 'r', label='Input Signal')
plt.plot(time * 10**6, outSignal, 'b', label='Output Signal')
plt.xlabel("Time " + r'($\mu s$)')
plt.ylabel("Amplitude (V)")
plt.ylim(-2, 2)
plt.grid(True)
plt.legend()

plt.show()