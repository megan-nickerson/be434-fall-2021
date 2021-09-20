#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-09-19
Purpose: Sing "Do-Re-Mi"
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sing Do-Re-Mi',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        nargs='+',
                        help='input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    singer = {'Do': 'A deer, a female deer', 'Re': 'A drop of golden sun',
              'Mi': 'A name I call myself', 'Fa': 'A long long way to run',
              'Sol': 'A needle pulling thread', 'La': 'A note to follow sol',
              'Ti': 'A drink with jam and bread'}

    for char in args.text:
        if char in singer:
            print('{}, {}'.format(char, singer.get(char)))
        else:
            print("I don't know \"{}\"".format(char))


# --------------------------------------------------
if __name__ == '__main__':
    main()
