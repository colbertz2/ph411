import matplotlib.pyplot as plt
import numpy as np

# Import data from file and skip header row
# potential, current_mA, current_A = np.loadtxt('fig_PowerSupply.csv', delimiter=',', unpack=True, skiprows=1)

# Import data from the alternate data file
potential_alt, current_mA_alt, current_A_alt = np.loadtxt('fig_PowerSupply_alt.csv', delimiter=',', unpack=True, skiprows=1)

# Linear fit
m, b = np.polyfit(potential_alt,current_A_alt,1)
x_fit = np.arange(-1,3)
y_fit = (m * x_fit + b) * (10**3)

# Theory curve from our first method
# v_theory = 2.00
# i_theory = 25.8 * (10**-3)
# r_theory = 77.5
# y_theory = (v_theory / r_theory) - ((1 / r_theory) * x_fit)

# Some math for the paper
R_th = -1. / m
V_th = b * R_th

print "Thevenin Resistance:"
print R_th
print "\nThevenin Potential:"
print V_th

# Plot some stuff
# plt.plot(potential,current_mA,'ro', label="Power Supply")
plt.plot(potential_alt,current_mA_alt,'ro', label="Power Supply")
plt.plot(x_fit,y_fit, label="Linear Fit")
# plt.plot(x_fit,y_theory*(10**3), label="Circuit without load")

# Set plot formatting
plt.xlim(0.7,0.95)
plt.ylim(0.,130.)
plt.grid(True)

# Labels and text
plt.xlabel("Load Potential Difference (V)")
plt.ylabel("Load Current (mA)")
plt.title("Current-Potential Characteristic of DC Power Supply\nwith Variable Resistor Load")
plt.legend()

# Show the plot
plt.show()