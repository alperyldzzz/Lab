import numpy as np
import matplotlib.pyplot as plt
import math

def taylor_sin(x, n):
    s = 0
    for i in range(n):
        s += ((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1)
    return s

def taylor_cos(x, n):
    c = 0
    for i in range(n):
        c += ((-1)**i)*(x**(2*i))/math.factorial(2*i)
    return c

x = np.linspace(-3, 3, 200)
n = 5

sin_taylor = [taylor_sin(i, n) for i in x]
cos_taylor = [taylor_cos(i, n) for i in x]

sin_numpy = np.sin(x)
cos_numpy = np.cos(x)

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.plot(x, sin_numpy, label="numpy sin")
plt.plot(x, sin_taylor, '--', label="taylor sin")
plt.legend()
plt.title("sin comparison")

plt.subplot(2,2,2)
plt.plot(x, cos_numpy, label="numpy cos")
plt.plot(x, cos_taylor, '--', label="taylor cos")
plt.legend()
plt.title("cos comparison")

plt.subplot(2,2,3)
plt.plot(x, sin_numpy - sin_taylor)
plt.title("sin difference")

plt.subplot(2,2,4)
plt.plot(x, cos_numpy - cos_taylor)
plt.title("cos difference")

plt.tight_layout()
plt.show()

check = np.array(sin_taylor)**2 + np.array(cos_taylor)**2

plt.plot(x, check)
plt.title("sin^2 + cos^2")
plt.show()