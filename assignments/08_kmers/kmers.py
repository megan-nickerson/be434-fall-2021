#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-10-25
Purpose: Find common kmers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('File1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('File2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default='3')

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    filename1 = args.File1
    filename2 = args.File2
    kmers = args.kmer

    kmers1 = count_kmers(filename1, kmers)
    kmers2 = count_kmers(filename2, kmers)

    common = sorted(list(set(kmers1).intersection(kmers2)))
    for kmer in common:
        print('{:10}{:6}{:6}'.format(
            kmer, kmers1.get(kmer), kmers2.get(kmer)), end='\n')
# --------------------------------------------------


def count_kmers(filename, k):
    """Count kmers in a file to create a dictionary"""

    words = {}
    for line in filename:
        for word in line.split():
            for kmer in find_kmers(word, k):
                if kmer in words:
                    words[kmer] += 1
                else:
                    words[kmer] = 1

    return words

# --------------------------------------------------


def find_kmers(seq, k):
    """Find kmers in a string"""

    n = len(seq) - k + 1

    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
