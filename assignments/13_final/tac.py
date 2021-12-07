#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-12-01
Purpose: Python clone of tac
"""

import argparse
import sys
from file_read_backwards import FileReadBackwards

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
    
    for fh in filename:
        for line in fh:
            print(FileReadBackwards(line.rstrip()))


# for line in fh:
#   line_rev = reversed(line.rstrip())
#   print(line_rev)
# This gives ['e', 'n', 'o'] / ['o', 'w', 't']

        # for line in reversed(open(fh)):
        #     print(line.rstrip())


            # line_rev= reversed(line.rstrip())
            # print(line_rev)

    # lines = filename.readlines()
    # for line in lines:
    #     print(line)

    # input_file = open(filename)
    # line_count = 0
    # for line in filename:
    #     if line != '\n':
    #         line_count += 1
    # filename.close()

    # print(line_count)

    # for fh in filename:
    #     for line_num, line in enumerate(fh, start=1):
    #         print(line_num)
            # if args.number:
            #     print("{:>6}\t{}".format(line_num, line.rstrip()))
            # else:
            #     print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
