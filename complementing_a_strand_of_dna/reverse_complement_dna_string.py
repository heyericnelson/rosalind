# take in a string of nucleobases and print the reverse complement
import argparse as ap

# store the complements of each base
COMPLEMENTS = {
          'A': 'T'
        , 'T': 'A'
        , 'C': 'G'
        , 'G': 'C'
}

if __name__ == "__main__":
    # set up argument parser
    parser = ap.ArgumentParser(description = "parse a file containing a dna string and return the reverse complement of it")
    # add input parsers
    parser.add_argument('-f', help = "the relative path of the input file", type = ap.FileType('r'), required = True)
    # parse arguments and collect variables
    args = parser.parse_args()
    raw_data = args.f

    for line in raw_data.read().splitlines():
        # use some list slicing to reverse the list
        reversed_dna = line[::-1]
        swapped_dna = ""

        for i in range(len(reversed_dna)):
            swapped_dna += COMPLEMENTS[reversed_dna[i]]

    print swapped_dna
