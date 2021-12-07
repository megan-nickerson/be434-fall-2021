#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-12-01
Purpose: Python clone of tac
"""

import argparse
import sys
# from file_read_backwards import FileReadBackwards

# from typing import Counter

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
    # line_of_list = []

    # for fh in filename:
    #     for line in fh:
    #         line_of_list = list.reverse([line.rstrip()])
    #         print(line_of_list)
    #  prints None over and over

    # for fh in filename:
    #     for line in fh:
    #         line_of_list = [line.rstrip()]
    #         line_of_list.reverse()
    #         print(line_of_list)
    #  prints the lines in normal order ['one'] / ['two']

    # for fh in filename:
    #     for line in fh:
    #         line_of_list = [line.rstrip()]
    #         print(reversed(line_of_list))
    #  prints <list_reverseiterator object at 0x100bf78b0>

    # for fh in filename:
    #     for line in fh:
    #         line_of_list = [line.rstrip()]
    #         print(list(reversed(line_of_list)))
        #  prints the lines in normal order ['one'] / ['two']
    
    # for fh in filename:
    #     for line in fh:
    #         line_rev = reversed(line.rstrip())
    #         print(list(line_rev))
    # This gives ['e', 'n', 'o'] / ['o', 'w', 't']

    # for fh in filename:
    #     for line in fh:
    #         print(FileReadBackwards(line.rstrip()))


# --------------------------------------------------
if __name__ == '__main__':
    main()
