def newton(x_0, epsilon=0.00001):
    x_t = x_0
    h = 0.00001  # small value
    x_prev = 10

    while abs(x_t - x_prev) > epsilon:
        x_prev = x_t

        # f'(x) = (f(x+h) - f(x)) / h
        first_deriv = (f(x_prev + h) - f(x_prev)) / h

        # f''(x) = (f(x+h) - 2f(x) + f(x-h)) / h^2
        second_deriv = (
            f(x_prev + h)
            - 2 * f(x_prev)
            + f(x_prev - h)
        ) / (h ** 2)

        # Newton's optimization step:
        # x_new = x_old - f'(x_old) / f''(x_old)
        x_t = x_prev - (first_deriv / second_deriv)

    return x_t

# testing the function
if __name__ == "__main__":
    print(newton(x**2))

