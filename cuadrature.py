import matplotlib.pyplot as plt
import numpy as np

def funcInt(x):
    """Sine of x^2 (function to integrate)

    Examples:
        >>> funcInt(2,5)
        -0.0331792165475568

    Args:
        x (float): value to square and input to sine

    Returns:
        float: Returns the sine of `x`^2.

    """
    return np.sin(x**2)

def gaussxw(N):
    """Points and Weights for Gaussian Cuadrature

    Examples:
        >>> gaussxw(3)
        array([-0.77459667, 0,  0.77459667]),
        array([[0.55555556, 0.88888889, 0.55555556])

    Args:
        N (int): Degree of the polynomial to use for approximation

    Returns:
        x: A numpy array of floats indicating the points to evaluate
        w: A numpy array of weights necesary for Gaussian Cuadrature
    
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return (x, w)

def gaussxwab(a, b, x, w):
    """Scales Gaussian Cuadrature points and weights to an interval

    Examples:
        >>> gaussxwab(0, 4.0, np.array([-0.77459667, 0,  0.77459667]),
                      np.array([0.55555556, 0.88888889, 0.55555556]))
        array([0.45080666, 2., 3.54919334]),
        array([1.11111112, 1.77777778, 1.11111112])
    Args:
        a (float): Start of the interval to scale to
        b (float): End of the intervarl to scale to
        x (np.array(float)): Gaussian cuadrature points to scale
        w (np.array(float)): Gaussian cuadrature weights to scale

    Returns:
        (np.array(float)): scaled Gaussian cuadrature points
        (np.array(float)): scaled Gaussian cuadrature weights

    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


valN = np.linspace(1, 10, 10, dtype=int)

pwGaussN = [gaussxw(n) for n in valN]
pwGaussEscN = [gaussxwab(0, np.pi, pw[0], pw[1]) for pw in pwGaussN]
intN = [np.sum(funcInt(pwE[0])*pwE[1]) for pwE in pwGaussEscN]

plt.plot(valN, intN)
plt.xlabel("$N$")
plt.ylabel(r"$\int_0^\pi$d$x\,$sin$(x^2)$")
plt.savefig("plot.pdf")

