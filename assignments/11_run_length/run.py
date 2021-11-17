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


def rle(dna_input):
    """Run-length input DNA"""

    line_ls = []
    dna_input = dna_input + "."
    prev = "none"
    count = 1
    for letter in dna_input:
        if prev == "none":
            prev = letter
        elif letter == prev:
            count += 1
        elif letter == ".":
            line_ls.append([prev, count])
        else:
            line_ls.append([prev, count])
            prev = letter
            count = 1

    rle_printer(line_ls)

# --------------------------------------------------


def rle_printer(line_ls):
    """Compare pairs and print"""

    pair_ls = []
    for pair in line_ls:
        if pair[1] == 1:
            pair[1] = ''
        pair_ls.append(''.join(map(str, pair)))
    print(''.join(map(str, pair_ls)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
