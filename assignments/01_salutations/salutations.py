#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-09-08
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='A greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='Print bang',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    ending = '!' if args.excited else '.'
    print(args.greeting + ', ' + args.name + ending)


# --------------------------------------------------
if __name__ == '__main__':
    main()
