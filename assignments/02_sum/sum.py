#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-09-14
Purpose: Add Numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add Numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('number',
                        metavar='int',
                        nargs='+',
                        type=int,
                        help='Numbers to add')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numbers = args.number

    line = ''
    if len(numbers) == 1:
        line = str(numbers[0])
    else:
        string_ints = [str(int) for int in numbers]
        line = ' + '.join(string_ints)
    
    print('{} = {}'.format(line,str(sum(numbers))))

# --------------------------------------------------
if __name__ == '__main__':
    main()
