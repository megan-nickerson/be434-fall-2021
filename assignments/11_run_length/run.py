#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-11-16
Purpose: Run-length encoding data compression
"""

import argparse
import os

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()
    if os.path.isfile(args.str):
        with open(args.str, 'rt', encoding='utf-8') as in_f:
            args.str = in_f.read()
    return args

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()

    for dna_input in args.str.splitlines():
        rle(dna_input)
# --------------------------------------------------


def rle(dna_input: str) -> str:  # take one string and return one string
    """Run-length input DNA"""

    counts = []  # a list to store all the characters seen
    dna_input = dna_input + "."
    prev = None
    count = 1
    for letter in dna_input:
        if prev is None:
            # beginning of sequence
            prev = letter
        elif letter == prev:
            # this letter is same as before
            count += 1
        elif letter == ".":
            # this letter is different
            counts.append([prev, count])
        else:
            # this is the end of the sequence to end the loop
            counts.append([prev, count])
            prev = letter
            count = 1
    prev = ''
    count = 1

    rle_printer(counts)

# --------------------------------------------------


def rle_printer(counts):
    """Compare pairs and print"""

    pair_counts = []
    for pair in counts:
        if pair[1] == 1:
            pair[1] = ''
        pair_counts.append(''.join(map(str, pair)))
    print(''.join(map(str, pair_counts)))
# --------------------------------------------------


# def test_rle():
#     """ Test rle """

#     assert rle('A') == 'A'
#     assert rle('ACGT') == 'ACGT'
#     assert rle('AA') == 'A2'
#     assert rle('AAAAA') == 'A5'
#     assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()
