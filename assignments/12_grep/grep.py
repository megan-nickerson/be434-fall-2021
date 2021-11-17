#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-11-17
Purpose: Print all the lines from files that match provided regex
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        metavar='',
                        default=False)

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
    print(args)

# --------------------------------------------------
if __name__ == '__main__':
    main()
