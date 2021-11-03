#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-11-03
Purpose: Split interleaved/paired reads in fasta files
"""

import argparse
import os
from Bio import SeqIO
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        nargs='+',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    args = parser.parse_args()

    check_dir = os.path.join(os.getcwd(), args.outdir)
    if not os.path.isdir(check_dir):
        os.mkdir(check_dir)

    return args

# --------------------------------------------------


def r_split(in_fasta, R1, R2):
    """takes interleaved file and splits"""

    reader = SeqIO.parse(in_fasta, 'fasta')
    rec_num = 0
    with open(R1, 'a', encoding='utf-8') as R1_out, \
            open(R2, 'a', encoding='utf-8') as R2_out:
        for rec in reader:
            rec_num += 1
            if rec_num % 2 == 0:
                print(f'>{rec.description}', file=R2_out)
                print(rec.seq, file=R2_out)
            else:
                print(f'>{rec.description}', file=R1_out)
                print(rec.seq, file=R1_out)

# --------------------------------------------------


def fasta_io(fasta_list, outdir):
    """Creates outfile names"""

    io_dict = defaultdict()
    for fasta in fasta_list:
        basename = os.path.basename(fasta)
        root, ext = os.path.splitext(basename)
        R1 = os.path.join(outdir, root + '_1' + ext)
        R2 = os.path.join(outdir, root + '_2' + ext)
        io_dict[fasta] = {'R1': R1, 'R2': R2}
    return io_dict


# --------------------------------------------------

def main():
    """Print final named and split files"""

    args = get_args()
    files_split = [fasta.name for fasta in args.file]
    files_io_dict = fasta_io(files_split, args.outdir)

    for fasta in files_split:
        R1 = files_io_dict[fasta]['R1']
        R2 = files_io_dict[fasta]['R2']
        r_split(fasta, R1, R2)

    print(f'Done, see output in "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
