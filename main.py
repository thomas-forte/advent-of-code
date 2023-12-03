import argparse
from datetime import datetime
from importlib import import_module

parser = argparse.ArgumentParser(
    prog="Advent of Code Manager",
)
parser.add_argument("day", type=int, help="Select just one day to run")
parser.add_argument("year", nargs="?", type=int, help="Select just one day to run")
parser.add_argument("-t", "--test", action="store_true", help="Run tests instead of input")

args = parser.parse_args()

if args.year is None:
    args.year = default = datetime.now().year


def run_day(year, day, filename="input.txt"):
    module = import_module(f"{year}.{day}.main")

    with open(f"{year}/{day}/{filename}") as f:
        input = f.read().splitlines()

    print(f"Part 1: {module.part_1(input)}")
    print(f"Part 2: {module.part_2(input)}")


if args.test:
    run_day(args.year, args.day, "test.txt")
else:
    run_day(args.year, args.day)
