import numpy as np
import matplotlib.pyplot as plt

def trajectory():
    v0 = 5
    g = 9.81
    t = np.linspace(0, 1, 1001)

    y = v0 * t - g * t**2 / 2

    plt.plot(t, y)
    plt.xlabel('t (s)')
    plt.ylabel('y (m)')
    plt.show()

if __name__ == "__main__":
    trajectory()
