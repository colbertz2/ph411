import matplotlib.pyplot as plt
import numpy as np
import os

# Set up the path to the Data directory
dataPath = os.path.dirname(os.path.abspath(__file__)) + '/../Data'

# Import data for plot
baseCurrent, collectorCurrent = np.genfromtxt((dataPath + '/data.csv'), unpack=True, delimiter=',', skiprows=1, usecols=(0,1))

# Convert to useful units
# baseCurrent *= 10**(-6) # uA to A
# collectorCurrent *= 10**(-3) # mA to A

# Make a theory curve for the data
gain, offset = np.polyfit(baseCurrent, collectorCurrent, 1)
x = np.arange(min(baseCurrent), max(baseCurrent))
y = (gain * x) + offset

# Grab some selective data and make a better theory curve
indices = range(0,14)
selectBase = np.take(baseCurrent, indices)
selectCollector = np.take(collectorCurrent, indices)
selectGain, selectOffset = np.polyfit(selectBase, selectCollector, 1)
u = x
v = (selectGain * u) + selectOffset

# Make another curve based on the gain measured by the DMM
dmmGain = 112
w = x
z = dmmGain * w * 10**(-3)

# Plot Ib on x, Ic on y
plt.figure()
plt.plot(baseCurrent, collectorCurrent, 'ro')   # Original data
plt.plot(x, y)  # Theory curve on original data
plt.plot(u, v, 'r')     # Theory curve on selective data
plt.plot(w, z, 'g')     # Theory curve on DMM gain
plt.xlabel('Base Current ' + r'$\mu A$')
plt.ylabel('Collector Current ' + r'$mA$')
plt.title("2N9304 Transistor Gain")
# plt.tight_layout()

plt.show()