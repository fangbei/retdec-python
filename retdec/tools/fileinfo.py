#
# Project:   retdec-python
# Copyright: (c) 2015 by Petr Zemek <s3rvac@gmail.com> and contributors
# License:   MIT, see the LICENSE file for more details
#

"""A tool for analysis of binary files. It uses the library."""

import argparse
import sys

from retdec.fileinfo import Fileinfo
from retdec.tools import _add_arguments_shared_by_all_tools


def parse_args(argv):
    """Parses the given list of arguments."""
    parser = argparse.ArgumentParser(
        description=('Analyzes the given file through the retdec.com '
                     'decompilation service by using their public REST API.')
    )
    _add_arguments_shared_by_all_tools(parser)
    parser.add_argument(
        'file',
        metavar='FILE',
        help='file to analyze'
    )
    parser.add_argument(
        '-v', '--verbose',
        dest='verbose',
        action='store_true',
        help='print all available information about the file'
    )
    return parser.parse_args(argv[1:])


def main():
    args = parse_args(sys.argv)
    fileinfo = Fileinfo(
        api_url=args.api_url,
        api_key=args.api_key
    )
    analysis = fileinfo.run_analysis(
        input_file=args.file,
        verbose=args.verbose
    )
    analysis.wait_until_finished()
    sys.stdout.write(analysis.get_output())
    return 0


if __name__ == '__main__':
    sys.exit(main())
