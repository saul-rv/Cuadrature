import matplotlib.pyplot as plt
import numpy as np

def funcInt(x):
    return np.sin(x**2)

def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)
    return (x, w)

def gaussxwab(a, b, x, w):
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

valN = np.linspace(1, 50, 50, dtype=int)

pwGaussN = [gaussxw(n) for n in valN]
pwGaussEscN = [gaussxwab(0, np.pi, pw[0], pw[1]) for pw in pwGaussN]
intN = [np.sum(funcInt(pwE[0])*pwE[1]) for pwE in pwGaussEscN]

plt.plot(valN, intN)
plt.savefig("plot.pdf")

