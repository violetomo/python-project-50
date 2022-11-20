#!/usr/bin/env python3
from gendiff.modules.parser import args
from gendiff.modules.generate_diff import generate_diff


def main():
    diff = generate_diff(args.first_file, args.second_file)
    return print(diff)


if __name__ == '__main__':
    main()
