import matplotlib.pyplot as plt
import numpy as np

# Import data from file and skip header row
x, y, y_actual = np.loadtxt('fig_TheveninWithLoad.csv', delimiter=',', unpack=True, skiprows=1)

# Linear fit
m, b = np.polyfit(x,y_actual,1)
x_fit = np.arange(-1,3)
y_fit = (m * x_fit + b) * (10**3)

# Theory curve from our first method
v_theory = 2.00
i_theory = 25.8 * (10**-3)
r_theory = 77.5
y_theory = (v_theory / r_theory) - ((1 / r_theory) * x_fit)

# Some math for the paper
R_th = -1. / m
V_th = b * R_th

print "Thevenin Resistance:"
print R_th
print "\nThevenin Potential:"
print V_th

# Plot some stuff
plt.plot(x,y_actual*(10**3),'ro', label="$100 k\Omega$ variable load")
plt.plot(x_fit,y_fit, label="Linear Fit")
plt.plot(x_fit,y_theory*(10**3), label="Circuit without load")

# Set plot formatting
plt.xlim(0.,2.2)
plt.ylim(-1.,25.)
plt.grid(True)

# Labels and text
plt.xlabel("Load Potential Difference (V)")
plt.ylabel("Load Current (mA)")
plt.title("Current-Potential Characteristic of Thevenin Circuit\nwith Variable Resistor Load")
plt.legend()

# Show the plot
plt.show()