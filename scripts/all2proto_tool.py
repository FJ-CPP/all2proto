#!/usr/bin/env python3
import argparse


def main():
    arg_parser = argparse.ArgumentParser(
        description="Convert all data structures to proto files")
    arg_parser.add_argument("-s",
                            "--target_ds",
                            nargs='+',
                            required=True,
                            help="Target data structure names")
    arg_parser.add_argument(
        "-p",
        "--search_path",
        type=str,
        default='.',
        help="Path to search for all files, use `:` to separate multiple paths")
    arg_parser.add_argument("-o",
                            "--output_path",
                            type=str,
                            required=True,
                            help="Output path to store proto files")

    args = arg_parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
