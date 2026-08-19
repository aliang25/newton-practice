def newton(x_0, epsilon = 0.00001):
    x_t = x_0
    h = 0.00001 # define a "small value"
    x_prev = 10
    
    while abs(x_t - x_prev) > epsilon:
        x_prev = x_t
        
        first_deriv = (f(x_prev + h) - f(x_prev - h)) / (2 * h)

        # 
        second_deriv = (f(x_prev + h) - 2 * f(x_prev) + f(x_prev - h)) / (h ** 2)

        # Newton step x_t = x_t-1 - f'(x_t-1)/f''(x_t-1)
        x_t = x_prev - (first_deriv / second_deriv)

    return x_t


if __name__ == "__main__":
    print
        
    