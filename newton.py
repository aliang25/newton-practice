def f(x):
    """Return the value of f(x) = x^2."""
    return x**2


def first_deriv(x):
    """Approximate the first derivative of f at x."""
    h = 0.00001
    return (f(x + h) - f(x)) / h


def second_deriv(x):
    """Approximate the second derivative of f at x."""
    h = 0.00001
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)


def optimize(x_0, epsilon=0.00001):
    """Find a minimum of f using Newton's optimization method."""
    x_t = x_0
    x_prev = 10

    while abs(x_t - x_prev) > epsilon:
        x_prev = x_t
        x_t = x_prev - (first_deriv(x_prev) / second_deriv(x_prev))

    return x_t


if __name__ == "__main__":
    print(optimize(10))
