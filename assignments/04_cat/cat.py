#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-09-27
Purpose: To concatenate files
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Concatenate files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file_name',
                        metavar='FILE',
                        nargs='+',
                        help='file names to concatenate',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='number the lines',
                        action='store_true',)

    # parser.add_argument('-h',
    #                     '--help',
    #                     help='show this help message and exit',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file_name:
        for line_num, line in enumerate(fh, start=1):
            if args.number is True:
                print("     {}\t{}".format(line_num, line), end='')
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
