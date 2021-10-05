#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-10-05
Purpose: Translate DNA or RNA
"""

import argparse
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA or RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA or RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='codon table',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-o',
                        '--output',
                        help='Name a file to write the output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    codon_table = {}
    for line in args.codons:
        key, value = line.rstrip().split()
        codon_table[key] = value

    k = 3
    seq = args.sequence
    protein = []
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        print(codon)
    # pprint(codon_table)
    # print('seq =', args.sequence)
    # print('codons =', args.codons)
    # print('output =', args.output)

    from pprint import PrettyPrinter

# --------------------------------------------------
if __name__ == '__main__':
    main()
