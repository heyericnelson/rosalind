# this script takes an RNA string (of nucleobases) and convert it into a protein string
import argparse as ap

if __name__ == "__main__":
    # set up argument parser
    parser = ap.ArgumentParser(description = "parse a file containing a RNA string, convert to a protein string")
    # add input parsers
    parser.add_argument("-f", help = "the relative path of the input file", type = ap.FileType('r'), required = True)
    # parse arguments and collect variables
    args = parser.parse_args()
    raw_data = args.f

    # create a mapping of codons to amino_acids
    bases = ['U', 'C', 'A', 'G']
    codons = [a + b + c for a in bases for b in bases for c in bases]
    amino_acids = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    codon_amino_map = dict(zip(codons, amino_acids))

    for rna_string in raw_data.read().splitlines():
        amino_repr = ""
        # codons are in triplets, so grab them three at a time
        for i,j,k in zip(rna_string[::3],rna_string[1::3],rna_string[2::3]):
            codon = i + j + k
            amino = codon_amino_map[codon]

            # if it's a stop codon, terminate the loop
            if amino == "*":
                break
            else:
                amino_repr += amino

    print amino_repr
