#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-10-12
Purpose: Find words in common
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find words in common',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('file2',
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
    output = args.outfile

    # words1 = {}
    # for line in args.file1:
    #     for word in line.split():
    #         words1[word] = 1

    # words2 = {}
    # for line in args.file2:
    #     for word in line.split():
    #         words2[word] = 1

    # for word in words1:
    #     if word in words2:
    #         print(word, file=args.outfile)

    filename1 = args.file1.read().split()
    filename2 = args.file2.read().split()

    common = list(set(filename1).intersection(filename2))

    if output:
        output.write('\n'.join(common))
        output.close()
    else:
        print('\n'.join(common))


# --------------------------------------------------
if __name__ == '__main__':
    main()
