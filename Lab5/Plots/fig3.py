import matplotlib.pyplot as plt
import numpy as np

f = [100, 10**3, 10**6, 10**7, 12.5 * 10**6, 10, 100 * 10**3]
V = [600., 600., 700., 2200., 2900., 600., 600.]

V = np.array(V)

plt.semilogx(f, V * 10**(-3), 'ro')
plt.show()