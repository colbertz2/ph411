import numpy as np
import matplotlib.pyplot as plt
import os


# Set up the path to the Data directory
dataPath = os.path.dirname(os.path.abspath(__file__)) + '/../Data'

# Import data for plot
time1, outSignal1, inSignal1 = np.genfromtxt((dataPath + '/figA-1.csv'), unpack=True, delimiter=',', skiprows=1, usecols=(0,1,2))

time2, outSignal2, inSignal2 = np.genfromtxt((dataPath + '/figA-2.csv'), unpack=True, delimiter=',', skiprows=1, usecols=(0,1,2))


# Plot the stuff
plt.figure()
plt.title("LM-741 Slew Distortion")
plt.plot(time1 * 10**6, inSignal1, 'b', label="Input")
plt.plot(time1 * 10**6, outSignal1, 'r', label="Output")
plt.xlabel("Time (us)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid(True)

plt.figure()
plt.title("TL-071 Slew Distortion")
plt.plot(time2 * 10**6, inSignal2, 'b', label="Input")
plt.plot(time2 * 10**6, outSignal2, 'r', label="Output")
plt.xlabel("Time (us)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid(True)


plt.show()