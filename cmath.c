#include <math.h>
#include <stdint.h>
#include "cmath.h"

/**
 * Returns the nth number from the fibonacci sequence.
 *
 * n int Number of steps into the fibonacci sequence
 *
 * return int The fibonacci number
 */
uint64_t fib(uint64_t n) {
    if ( n < 2 ) {
        return n;
    }
    return fib(n-1) + fib(n-2);
}

/**
 * Returns the sum of all natural numbers lower than `max'.
 *
 * NOTE: With 32 bits signed ints, the highest sum we can produce without
 * overflowing is with max=65536
 *
 * max int The upper bound of numbers to sum.
 *
 * return int The sum of the natural numbers.
 */
uint64_t sum(uint64_t max) {
    uint64_t i, sum = 0;
    for (i = 1; i < max; ++i) {
        sum += i;
    }
    return sum;
}

/**
 * Pythagoras theorem, finds the hypotenuse given two sides.
 *
 * a float One of the sides
 * b float The other side
 *
 * return float The length of the hypotenuse
 */
double hyp(double a, double b) {
    return sqrt(pow(a, 2.0) + pow(b, 2.0));
}

/**
 * Pythagoras theorem, finds the hypotenuse given two sides.
 *
 * a float One of the sides
 * b float The other side
 *
 * return float The length of the hypotenuse
 */
double sine(int angle) {
    double x, sine;

    angle = angle % 360;
    x = (double) (angle % 180);
    sine = (4 * x * (180 - x)) / (40500 - x * (180 - x));

    if (angle > 180) {
        sine *= -1;
    }

    return sine;
}
