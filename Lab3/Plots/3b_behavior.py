import matplotlib.pyplot as plt
import numpy as np

# Import data from file and skip header rows
time_1khz, inputWave_1khz, output_1khz = np.genfromtxt('../Data/3b_1khz.csv', delimiter=',', usecols=(0,1,3), skiprows=1, unpack=True)

time_10hz, inputWave_10hz, output_10hz = np.genfromtxt('../Data/3b_10hz.csv', delimiter=',', usecols=(0,1,3), skiprows=1, unpack=True)

time_10khz, inputWave_10khz, output_10khz = np.genfromtxt('../Data/3b_10khz.csv', delimiter=',', usecols=(0,1,3), skiprows=1, unpack=True)

time_100hz, inputWave_100hz, output_100hz = np.genfromtxt('../Data/3b_100hz.csv', delimiter=',', usecols=(0,1,3), skiprows=1, unpack=True)

time_100khz, inputWave_100khz, output_100khz = np.genfromtxt('../Data/3b_100khz.csv', delimiter=',', usecols=(0,1,3), skiprows=1, unpack=True)

# # Fix the time offset
# time = time - min(time)

# # Make time more readable
us = 10**6 # Multiply seconds by us to get microseconds
ms = 10**3 # Multiply seconds by ms to get milliseconds

# # Plot some stuff
# plt.figure(3)
plt.subplot(223)
plt.plot(time_1khz * ms, inputWave_1khz, 'b--', label="Input Voltage")
plt.plot(time_1khz * ms, output_1khz, 'r', label="Capacitor Voltage")
plt.title("1 kHz Input")
plt.grid(True)
plt.xlabel("Time (ms)")
plt.ylabel("Potential (V)")

# plt.figure(1)
plt.subplot(221)
plt.plot(time_10hz * ms, inputWave_10hz, 'b--', label="Input Voltage")
plt.plot(time_10hz * ms, output_10hz, 'r', label="Capacitor Voltage")
plt.title("10 Hz Input")
plt.grid(True)
plt.xlabel("Time (ms)")
plt.ylabel("Potential (V)")

# plt.figure(4)
plt.subplot(224)
plt.plot(time_10khz * ms, inputWave_10khz, 'b--', label="Input Voltage")
plt.plot(time_10khz * ms, output_10khz, 'r', label="Capacitor Voltage")
plt.title("10 kHz Input")
plt.grid(True)
plt.xlabel("Time (ms)")
plt.ylabel("Potential (V)")

# plt.figure(2)
plt.subplot(222)
plt.plot(time_100hz * ms, inputWave_100hz, 'b--', label="Input Voltage")
plt.plot(time_100hz * ms, output_100hz, 'r', label="Capacitor Voltage")
plt.title("100 Hz Input")
plt.grid(True)
plt.xlabel("Time (ms)")
plt.ylabel("Potential (V)")

# plt.figure(5)
# plt.subplot(225)
# plt.plot(time_100khz * ms, inputWave_100khz, 'b--', label="Input Voltage")
# plt.plot(time_100khz * ms, output_100khz, 'r', label="Capacitor Voltage")
# plt.title("100 kHz")

plt.tight_layout()

# # # Set plot formatting
# # plt.xlim(0.7,0.95)
# # plt.ylim(0.,130.)
# plt.grid(True)

# # # Labels and text
# plt.xlabel("Time (ms)")
# plt.ylabel("Potential (V)")
# plt.title("Voltage of Capacitor with Square Wave Input")
# plt.legend()

# # Show the plot
plt.show()