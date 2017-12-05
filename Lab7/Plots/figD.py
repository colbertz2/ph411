import numpy as np
import matplotlib.pyplot as plt
import os


# Set up the path to the Data directory
dataPath = os.path.dirname(os.path.abspath(__file__)) + '/../Data'

# Import data for plot
time, inSignal, outSignal = np.genfromtxt((dataPath + '/figD.csv'), unpack=True, delimiter=',', skiprows=1, usecols=(0,1,2))

# Plot some stuff
plt.figure()
plt.plot(time, inSignal, 'b', label="Input")
plt.plot(time, outSignal, 'r', label="Output")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Op-Amp Differentiator Circuit")


plt.show()