# determine the probability of producing a dominant phenotype

import math
import argparse as ap

def nCr(n,r):
    """
    Return the number of combinations from two numbers

    :param n: the number of objects from which to choose
    :param r: the number chosen at any given time

    :return: the number of distinct combinations
    :rtype: int
    """
    f = math.factorial

    if n >= r:
        result = f(n) / f(r) / f(n-r)
    else:
        result = 0

    return result


if __name__ == "__main__":
    # set up argument parser
    parser = ap.ArgumentParser()

    # add input parsers
    parser.add_argument('-d', help = "the number of individuals that are homozygous dominant", type = int, required = True)
    parser.add_argument('-z', help = "the number of individuals that are heterozygous", type = int, required = True)
    parser.add_argument('-r', help = "the number of individuals that are homozygous recessive", type = int, required = True)

    # parse arguments and collect variables
    args = parser.parse_args()
    d = args.d
    z = args.z
    r = args.r

    # get the number of possible pairings
    possible_options = nCr(d + z + r, 2) * 4

    # multiply by punnett square number
    double_recessive = nCr(r,2) * 4.0
    hetero_recessive = (z * r) * 2.0
    double_hetero = nCr(z,2) * 1.0

    print 1 - (double_recessive + hetero_recessive + double_hetero) / possible_options
