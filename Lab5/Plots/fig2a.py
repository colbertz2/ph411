import numpy as np
import matplotlib.pyplot as plt
import os

# Set up the path to the Data directory
dataPath = os.path.dirname(os.path.abspath(__file__)) + '/../Data'

# Import data for plot
time, mathFxn = np.genfromtxt((dataPath + '/2a.csv'), unpack=True, delimiter=',', skiprows=1, usecols=(0,1))

# Do some math
f = 100 #Hz
A = .6 / 2 # 600 mVpp / 2 makes wave amplitude
inputSignal = -1 * A * np.sin(2 * np.pi * f * time)

outputSignal = inputSignal - mathFxn

# Plot the stuff
plt.figure()
plt.plot(time, mathFxn, 'r,')
plt.plot(time, inputSignal)
plt.plot(time, outputSignal, 'g')

plt.show()
