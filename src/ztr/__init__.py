"""Transpose a CSV file"""

import csv
import sys
import argparse as ap
from itertools import zip_longest


def main():
    """The main function"""

    parser = ap.ArgumentParser()
    parser.add_argument('file', help='CSV files')
    parser.add_argument('--output', '-o', help='output file')
    args = parser.parse_args()

    with open(args.file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_ll = list(csv_reader)
        csv_ll_transposed = list(map(list, zip_longest(*csv_ll)))

    if args.output is None:
        csv_writer = csv.writer(sys.stdout)
        csv_writer.writerows(csv_ll_transposed)
    else:
        with open(args.output, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(csv_ll_transposed)



if __name__ == '__main__':
    main()
