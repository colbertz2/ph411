import numpy as np
import matplotlib.pyplot as plt

################################################################################
############################       LR CIRCUIT       ############################
################################################################################

# Import data
data = np.genfromtxt("Lab4/Data/1_lr.csv", unpack=True, delimiter=',', skiprows=1)

time_abs = data[0]
Vout = data[1]

time = time_abs[np.where(time_abs > 4.87e-5)]
Vout = Vout[np.where(time_abs > 4.87e-5)]
time = time - time[np.argmin(Vout)]
Vout = Vout - Vout[np.argmin(Vout)]

V_o = 4
Tau = 10**(-6)
V_theory = V_o * (1 - np.exp(-1 * time / Tau))

V_o2 = 3.986052299
Tau2 = 0.0000113951372687442
V_theory2 = V_o2 * (1 - np.exp(-1 * time / Tau2))

plt.figure()
plt.plot(time, Vout, 'r.', label="Experimental")
plt.plot(time, V_theory, 'b--', label="Original Theory")
plt.plot(time, V_theory2, 'g', label=("$\chi ^2$" + " Theory"))
# plt.ylim(-0.5,4)
plt.legend(loc=4)
plt.xlabel("Time (s)")
plt.ylabel("Inductor Voltage " + r'$V_L(t)$' + " (V)")
plt.title("LR Circuit")

plt.show()