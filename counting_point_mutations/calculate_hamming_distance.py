# calculate the Hamming distance between two DNA strings
import argparse as ap

if __name__ == "__main__":
    # set up argparser
    parser = ap.ArgumentParser()

    parser.add_argument(
            '-s'
            , help = "the first DNA string"
            , type = str
            , required = True)
    parser.add_argument(
            '-t'
            , help = "the second DNA string"
            , type = str
            , required = True)

    # parse the arguments + assign variables
    args = parser.parse_args()
    s = args.s
    t = args.t

    counter = 0

    for i in zip(s, t):
        if i[0] != i[1]:
            counter += 1

    print "The Hamming distance between the DNA strings is", str(counter) + "."
