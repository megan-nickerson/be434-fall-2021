#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-10-18
Purpose: Translate IUPAC-encoded DNA
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input_sequence = args.seq
    iupac = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T', 'U': 'U',
             'R': 'AG', 'Y': 'CT', 'S': 'GC', 'W': 'AT', 'K': 'GT',
             'M': 'AC', 'B': 'CGT', 'D': 'AGT', 'H': 'ACT',
             'V': 'ACG', 'N': 'ACGT'}
    for seq in input_sequence:
        output_re = ""

        for item in seq:
            if len(iupac.get(item)) > 1:
                output_re = output_re + '[{}]'.format(iupac.get(item))
            else:
                output_re = output_re + iupac.get(item)
        print('{} {}'.format(seq, output_re), file=args.outfile)

    # iupac = [('A', 'A'),
    #          ('C', 'C'),
    #          ('G', 'G'),
    #          ('T', 'T'),
    #          ('U', 'U'),
    #          ('R', '[AG]'),
    #          ('Y', '[CT]'),
    #          ('S', '[GC]'),
    #          ('W', '[AT]'),
    #          ('K', '[GT]'),
    #          ('M', '[AC]'),
    #          ('B', '[CGT]'),
    #          ('D', '[AGT]'),
    #          ('H', '[ACT]'),
    #          ('V', '[ACG]'),
    #          ('N', '[ACGT]')]

    # for seq in args.SEQ:
    #     regex = str()
    #     for char in seq:
    #         for value, pattern in iupac:
    #             if re.search(value, char):
    #                 regex = regex + pattern
    #     print(seq, regex, file= args.outfile)

    if args.outfile is not sys.stdout:
        print('Done, see output in "{}"'.format(args.outfile.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()
