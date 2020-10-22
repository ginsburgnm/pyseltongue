# -*- coding: utf-8 -*-
"""
    Secret Sharing
    ~~~~~

    :copyright: (c) 2014 by Halfmoon Labs
    :license: MIT, see LICENSE for more details.
"""
from utilitybelt import secure_randint as randint

def extended_gcd(int_a, int_b):
    """Find the gcd as a linear combination of 2 numbers"""
    if int_a == 0:
        return (int_b, 0, 1)
    int_g, int_y, int_x = extended_gcd(int_b % int_a, int_a)
    return (int_g, int_x - (int_b // int_a) * int_y, int_y)

def mod_inverse(int_a, modular):
    """Find inverse of int with a given mod"""
    int_a = int_a % modular
    ret = extended_gcd(modular, abs(int_a))[2]
    return (modular + ret) % modular

def random_polynomial(degree, intercept, upper_bound):
    """ Generates a random polynomial with positive coefficients.
    """
    if degree < 0:
        raise ValueError('Degree must be a non-negative number.')
    coefficients = [randint(0, upper_bound-1) for x in range(degree)]
    coefficients.insert(0, intercept)
    return coefficients

def get_polynomial_points(coefficients, num_points, prime):
    """ Calculates the first n polynomial points.
        [ (1, f(1)), (2, f(2)), ... (n, f(n)) ]
    """
    points = []
    for x_coeff in range(1, num_points+1):
        # start with x=1 and calculate the value of y
        y_coeff = coefficients[0]
        # calculate each term and add it to y, using modular math
        for i in range(1, len(coefficients)):
            exponentiation = (x_coeff**i) % prime
            term = (coefficients[i] * exponentiation) % prime
            y_coeff = (y_coeff + term) % prime
        # add the point to the list of points
        points.append((x_coeff, y_coeff))
    return points

def modular_lagrange_interpolation(x_coor, points, prime):
    """Calculate lowest degree of polynomials"""
    # break the points up into lists of x and y values
    x_values, y_values = zip(*points)
    # initialize f(x) and begin the calculation: f(x) = SUM( y_i * l_i(x) )
    f_x = 0
    for i in range(len(points)):
        # evaluate the lagrange basis polynomial l_i(x)
        numerator, denominator = 1, 1
        for j in range(len(points)):
            # don't compute a polynomial fraction if i equals j
            if i == j:
                continue
            # compute a fraction & update the existing numerator + denominator
            numerator = (numerator * (x_coor - x_values[j])) % prime
            denominator = (denominator * (x_values[i] - x_values[j])) % prime
        # get the polynomial from the numerator + denominator mod inverse
        lagrange_polynomial = numerator * mod_inverse(denominator, prime)
        # multiply the current y & the evaluated polynomial & add it to f(x)
        f_x = (prime + f_x + (y_values[i] * lagrange_polynomial)) % prime
    return f_x
