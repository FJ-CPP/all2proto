#!/usr/bin/env python3
import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from all2proto import All2Proto


def main():
    # python3 scripts/all2proto_tool.py -t OneClass.h::OneClass -s sources -o outputs
    arg_parser = argparse.ArgumentParser(
        description="Convert all data structures to proto files")
    arg_parser.add_argument(
        "-t",
        "--target",
        nargs='+',
        required=True,
        help="Target data structure names and its location, use `::` to separate "
        "package and class name, like `OneClass.h::OneClass` for C++, or "
        "`RootPkg.OneClassPkg::OneClass` for Python. For nested class, or "
        "class inside a namespace, use `::` to separate class names, like "
        "`RootPkg.OneClassPkg::OneClass::NestedClass`")
    arg_parser.add_argument(
        "-s",
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
    print(vars(args))

    protos = All2Proto(args.target, args.search_path.split(':')).convert2proto()
    for ds, proto in protos:
        print(f"Writing {ds}.proto: {proto}")
        with open(f"{args.output_path}/{ds}.proto", "w") as f:
            f.write(proto)


if __name__ == '__main__':
    main()
