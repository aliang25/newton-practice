import numpy as np


def gradient(f, x, eps=1e-5):
    """Approximate the first derivative."""
    grad = np.zeros(len(x))

    for i in range(len(x)):
        x1 = x.copy()
        x1[i] += eps
        grad[i] = (f(x1) - f(x)) / eps

    return grad


def hessian(f, x, eps=1e-5):
    """Approximate the second derivative."""
    n = len(x)
    H = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            x1 = x.copy()
            x2 = x.copy()
            x3 = x.copy()

            x1[i] += eps
            x1[j] += eps
            x2[i] += eps
            x3[j] += eps

            H[i, j] = (f(x1) - f(x2) - f(x3) + f(x)) / eps**2

    return H


def optimize(x0, f, tol=1e-4):
    x = np.array(x0, dtype=float)

    x_new = x - np.linalg.solve(
        hessian(f, x),
        gradient(f, x)
    )

    while np.linalg.norm(x_new - x) > tol:
        x = x_new

        x_new = x - np.linalg.solve(
            hessian(f, x),
            gradient(f, x)
        )

    return {
        "x": x_new,
        "value": f(x_new)
    }