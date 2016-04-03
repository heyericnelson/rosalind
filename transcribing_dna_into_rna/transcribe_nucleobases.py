# this script takes nucleic acid strings and counts the frequency at which each base appears
import argparse as ap

if __name__ == "__main__":
    # set up argument parser
    parser = ap.ArgumentParser(description = "parse a file of newline-delimited dna strings and make them rna strings")
    # add input parsers
    parser.add_argument('-f', help = "the relative path of the input file", type = ap.FileType('r'), required = True)
    # parse arguments and collect variables
    args = parser.parse_args()
    raw_data = args.f

    # iterate over the file and do the character count
    for line in raw_data:
        # create an empty string to hold the final string
        final_string = ""

        for base in line:
            # swap thymine with uracil
            if base == 'T':
                base = 'U'
            else:
                pass
            # increment the count for the base
            final_string += base

        print final_string
