"""Entrypoint for running modules."""

import argparse
from datetime import datetime
from importlib import import_module

parser = argparse.ArgumentParser(
    prog="Advent of Code Manager",
)
parser.add_argument("day", type=int, help="Select just one day to run")
parser.add_argument("year", nargs="?", type=int, help="Select just one day to run")
parser.add_argument("-t", "--test", action="store_true", help="Run tests instead of input")
parser.add_argument("-d", "--debug", action="store_true", help="Include error outputs for test cases")

args = parser.parse_args()

if args.year is None:
    args.year = default = datetime.now().year


def run_day(year, day):
    """
    Imports specified days module, opens and reads inputs, then runs part_1 and part_2
    """
    module = import_module(f"{year}.{day}.main")

    with open(f"{year}/{day}/input.txt", encoding="utf-8") as f:
        split_lines = f.read().splitlines()

    print(f"Part 1: {module.part_1(split_lines)}")
    print(f"Part 2: {module.part_2(split_lines)}")


def test_day(year, day):
    """
    Imports specified days module, opens and reads inputs, then runs part_1 and part_2
    """
    module = import_module(f"{year}.{day}.main")

    with open(f"{year}/{day}/test-1.txt", encoding="utf-8") as f:
        split_lines_1 = f.read().splitlines()

    with open(f"{year}/{day}/test-2.txt", encoding="utf-8") as f:
        split_lines_2 = f.read().splitlines()

    print(f"Part 1: {module.part_1(split_lines_1)}")
    print(f"Part 2: {module.part_2(split_lines_2)}")


if args.test:
    test_day(args.year, args.day)
else:
    run_day(args.year, args.day)
