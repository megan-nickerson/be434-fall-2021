#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-12-01
Purpose: Python clone of tac
"""

import argparse
import sys


# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python clone of tac',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

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
    filename = args.file

    for fh in filename:
        list_of_lines = []
        for line in fh:
            list_of_lines.append(line.rstrip())
        for next_line in reversed(list_of_lines):
            print(next_line, file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
