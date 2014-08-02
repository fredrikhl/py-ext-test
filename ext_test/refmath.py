""" Python implementations of the functions in `cmath.so'. """


def fib(n):
    """ Return fibonacci number `n'. """
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def sum(max):
    """ Return the sum of all natural numbers lower than `max'. """
    sum = 0
    for i in range(1, max):
        sum += i
    return sum


def hyp(a, b):
    """ Return length of hypotenuse, using Pythagoras theorem. """
    return (a**2 + b**2)**.5


def sin(angle):
    """ Return an approximation of sine.

    This function uses the Bhaskara I sine approximation formula:
      http://en.wikipedia.org/wiki/Bhaskara_I's_sine_approximation_formula

    """
    angle = int(angle) % 360  # Angle within the four quadrants [0, 360)
    x = float(angle % 180)  # Angle within the formula range [0, 180)
    sine = (4 * x * (180 - x)) / (40500 - x * (180 - x))

    if angle > 180:
        sine *= -1.0
    return sine
