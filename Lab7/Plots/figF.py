import numpy as np
import matplotlib.pyplot as plt
import os


# Set up the path to the Data directory
dataPath = os.path.dirname(os.path.abspath(__file__)) + '/../Data'

# Import data for plot
time, inSignal, outSignal = np.genfromtxt((dataPath + '/figF.csv'), unpack=True, delimiter=',', skiprows=1, usecols=(0,1,3))

# Make a theory curve, to see what would happen if the capacitor didn't stop charging at 7.5 V
R = 100 * 10**3
C = 0.1 * 10**(-6)
V_0 = 15 #V
V_theory = V_0 * (1 - np.exp(-1 * time / (R * C))

plt.figure()
plt.plot(time, inSignal)
plt.plot(time, outSignal)

plt.show()