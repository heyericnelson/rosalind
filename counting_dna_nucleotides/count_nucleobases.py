# this script takes DNA strings and counts the frequency at which each base appears

import argparse as ap

def get_nucleobase_counts(dna_string):
    """ get the counts of each nucleobase in a dna string

    Keyword arguments:
    dna_string -- a string of text representing a DNA strand
    """
    # set the count values
    counts = {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0
            }

    try:
        for base in dna_string:
            # increment the count for the base
            counts[base] += 1
    except KeyError as e:
        print "There is an invalid key in {0}, skipping...".format(dna_string)

    return counts
            

if __name__ == "__main__":
    # set up argument parser
    parser = ap.ArgumentParser(description = "parse a file of newline-delimited nucleotide strings")
    # add input parsers
    parser.add_argument('-f', help = "the relative path of the input file", type = ap.FileType('r'), required = True)
    # parse arguments and collect variables
    args = parser.parse_args()
    raw_data = args.f

    # iterate over the file and do the character count
    for line in raw_data:
        # get the nucleobase counts and clean the line of excess whitespace
        counts = get_nucleobase_counts(line.strip())
        # print the counts in desired format
        print counts['A'], counts['C'], counts['G'], counts['T']
