import numpy as np
import matplotlib.pyplot as plt

N = np.arange(1, 10)
X = np.cumsum(9 * np.power(10., -N))

plt.axhline(1.0, color="grey", linestyle="dotted")
plt.plot(N, X, marker="x")

