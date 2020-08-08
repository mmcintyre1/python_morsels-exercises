import argparse
import csv
import os
from typing import List, Union


def build_parser() -> argparse.ArgumentParser:
    """

    :return:
    """
    parser = argparse.ArgumentParser(description="fixes csvs")
    parser.add_argument("input", help="an input file", type=str)
    parser.add_argument("output", help="an output file", type=str)
    parser.add_argument("--in-quote", help="a character to quote in the input csv", type=str, dest="quotechar")
    parser.add_argument("--in-delimiter", help="the delimiter character in the input csv", type=str, dest="delimiter")

    return parser


def read_csv(args) -> List[List[str]]:
    """
    Reads a csv file into a list of lists.  If not supplied a
    delimiter or quotechar. will attempt to guess one using the
    Sniffer class.
    :input_file: an input csv
    :return: a list of lists of data
    """
    with open(args.input, newline="") as csv_file:
        arguments = {}
        if args.delimiter:
            arguments['delimiter'] = args.delimiter
        if args.quotechar:
            arguments['quotechar'] = args.quotechar
        if not args.delimiter and not args.quotechar:
            arguments['dialect'] = csv.Sniffer().sniff(csv_file.read())
            csv_file.seek(0)
        reader = csv.reader(csv_file, **arguments)
        return [row for row in reader]


def write_csv(
        output_file: Union[str, os.PathLike],
        data: List[List[str]]
) -> None:
    """
    Writes a csv file out.
    :param output_file: an output csv location
    :param data: a list of lists of data to write
    :return: None
    """
    with open(output_file, 'wt', newline="") as csv_outfile:
        csv_writer = csv.writer(csv_outfile)
        csv_writer.writerows(data)


def main():
    arg_parser = build_parser()
    args = arg_parser.parse_args()
    csv_data = read_csv(args)
    write_csv(args.output, csv_data)


if __name__ == '__main__':
    main()
