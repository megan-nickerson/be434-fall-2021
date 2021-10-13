#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-10-12
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find words in common',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        help='Input file 2',
                        type=argparse.FileType('rt'),
                        metavar='FILE2')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    filename1 = args.FILE1
    filename2 = args.FILE2
    output = args.outfile

    FILE1 = filename1.read().split()
    FILE2 = filename2.read().split()

    common = sorted(list(set(FILE1).intersection(FILE2)))

    if output:
        output.write('\n'.join(common))
        output.close()
    else:
        print('\n'.join(common))


# --------------------------------------------------
if __name__ == '__main__':
    main()
