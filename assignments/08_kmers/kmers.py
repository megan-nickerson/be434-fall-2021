#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-10-25
Purpose: Find common kmers
"""

import argparse
import io
from typing import DefaultDict

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

    kmers1 = count_kmers(args.File1, args.kmer)
    kmers2 = count_kmers(args.File2, args.kmer)

    for common in set(kmers1).intersection(set(kmers2)):
        print('{:10}{:6}{:6}'.format(
            common, kmers1.get(common), kmers2.get(common)))

    # common = sorted(list(set(kmers1).intersection(kmers2)))
    # for kmer in common:
    #     print('{:10}{:6}{:6}'.format(
    #         kmer, kmers1.get(kmer), kmers2.get(kmer)), end='\n')

# --------------------------------------------------


def find_kmers(seq, k):
    """Find kmers in a string"""

    n = len(seq) - k + 1

    return [] if n < 1 else [seq[i:i + k] for i in range(n)]

# --------------------------------------------------


def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []
# --------------------------------------------------


def count_kmers(filename, k):
    """Count kmers in a file to create a dictionary"""

    # words = {}
    # for line in filename:
    #     for word in line.split():
    #         for kmer in find_kmers(word, k):
    #             if kmer in words:
    #                 words[kmer] += 1
    #             else:
    #                 words[kmer] = 1

    kmers = DefaultDict(int)
    for line in filename:
        for word in line.split():
            for kmer in find_kmers(word, k):
                kmers[kmer] += 1

    return kmers
# --------------------------------------------------


def test_count_kmers():
    """Test count kmers"""
    dat = 'foo\nbar\nbaz\n'

    assert count_kmers(io.StringIO(dat), 3) == {'foo': 1, 'bar': 1, 'baz': 1}
    assert count_kmers(io.StringIO(dat), 2) == {
        'fo': 1,
        'oo': 1,
        'ba': 2,
        'ar': 1,
        'az': 1
    }


# --------------------------------------------------
if __name__ == '__main__':
    main()
