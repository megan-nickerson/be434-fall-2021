#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-11-09
Purpose: Show the conserved bases
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    align_lines = [line.rstrip() for line in args.file]
    length_lines = len(align_lines)
    positions = len(align_lines[0])

    positions_match = compare_seq(align_lines, length_lines, positions)

    for lines in align_lines:
        print(lines.rstrip())

    for pos in range(positions):
        print(positions_match[pos], end='')


# --------------------------------------------------
def compare_seq(lines, align_lines, positions):
    """"Compare sequences and determine what matches"""
    bp_match = {}
    for bp in range(positions):
        compare = [lines[line][bp] for line in range(align_lines)]
        if len(set(compare)) != 1:
            bp_match[bp] = 'X'
        else:
            bp_match[bp] = '|'

    return bp_match


# --------------------------------------------------
if __name__ == '__main__':
    main()
