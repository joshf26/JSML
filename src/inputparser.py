import json

from sys import stdout
from argparse import ArgumentParser, FileType


def parse_input(default_output_filename='index.html'):
    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        'input',
        type=FileType('r'),
        help='specify the input json file name',
    )
    argument_parser.add_argument(
        '-o',
        '--output',
        type=FileType('w'),
        help='specify the output html file name (default is "index.html")',
    )
    argument_parser.add_argument(
        '-p',
        '--print',
        action='store_true',
        help='print to stdout and skip writing to file',
    )

    args = argument_parser.parse_args()
    data = json.load(args.input)

    if args.print:
        output_file = stdout
    elif args.output is not None:
        output_file = args.output
    else:
        output_file = open(default_output_filename, 'w')

    return (
        data,
        output_file,
    )
