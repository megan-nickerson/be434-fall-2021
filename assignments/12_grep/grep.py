#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-11-17
Purpose: Print all the lines from files that match provided regex
"""

import argparse
import sys
import re

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        help='Search pattern')

    # parser.add_argument('file',
    #                     help='Input file(s)',
    #                     nargs='+',
    #                     metavar='FILE',
    #                     type=argparse.FileType('rt'),
    #                     default='')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true',
                        default=False)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('file',
                        help='Input file(s)',
                        nargs='+',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='')
# putting file at the end gives the right order of outputs from the second hint

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # print(args)
    motif = args.pattern
    input_file = args.file
    case_insensitive = args.insensitive

    for filename in input_file:
        for line in filename:
            search = re.search(motif, line,
                               re.I) if case_insensitive else re.search(
                motif, line)
            if search:
                if len(input_file) > 1:
                    print(filename.name + ':' + line,
                          file=args.outfile, end='')
                else:
                    print(line, file=args.outfile, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
    # for filename in input_file:
    #     if case_insensitive:
    #         search = re.search(motif, line, re.I)
    #     else:
    #         search = re.search(motif, line)
    #     if search:
    #         if len(input_file) > 1:
    #             print(filename.name + ':' + line, file=args.outfile, end='')
    #         else:
    #             print(line, file=args.outfile, end='')
    # search = re.search(motif, input_file)
    # print(search)
