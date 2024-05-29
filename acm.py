import argparse
import sys
from datetime import datetime
from importlib import import_module

"""
    Setting up the cli parser
"""

parser = argparse.ArgumentParser(description="Advent of Code runner")
now = datetime.now()

parser.add_argument(
    "day",
    type=int,
    choices=range(1, 25),
    metavar="day",
    help="Select the day of advent to run",
)

parser.add_argument(
    "year",
    nargs="?",
    type=int,
    choices=range(2021, now.year),
    metavar="year",
    help="Optional, select the year of advent to run. The current year is the default.",
)

parser.add_argument(
    "-t",
    "--test",
    action="store_true",
    help="Run tests instead of input",
)

# TODO: add debugger runs
# parser.add_argument(
#     "-d",
#     "--debug",
#     action="store_true",
#     help="Include error outputs for test cases",
# )

args = parser.parse_args()

"""
    Init vars
"""

day = args.day

# if no year is supplied select the correct default year
if args.year is None:
    if now.month == 12:
        year = now.year
    else:
        year = now.year - 1
else:
    year = args.year


def _get_module(year, day):
    """
    Fetches module from directory structure
    """
    try:
        module = import_module(f"{year}.{day}.main")
        return module

    except ModuleNotFoundError:
        print(f"No module found at: {year}/{day}")
        print("Exiting")
        sys.exit(1)
        return None


def run_day(year, day):
    """
    Imports specified days module, opens and reads inputs, then runs part_1 and part_2
    """
    module = _get_module(year, day)

    with open(f"{year}/{day}/input.txt", encoding="utf-8") as f:
        split_lines = f.read().splitlines()

    print(f"Part 1: {module.part_1(split_lines)}")
    print(f"Part 2: {module.part_2(split_lines)}")


def test_day(year, day):
    """
    Imports specified days module, opens and reads inputs, then runs part_1 and part_2
    """
    module = _get_module(year, day)

    with open(f"{year}/{day}/test-1.txt", encoding="utf-8") as f:
        split_lines_1 = f.read().splitlines()

    with open(f"{year}/{day}/test-2.txt", encoding="utf-8") as f:
        split_lines_2 = f.read().splitlines()

    print(f"Part 1: {module.part_1(split_lines_1)}")
    print(f"Part 2: {module.part_2(split_lines_2)}")


if args.test:
    test_day(year, day)
else:
    run_day(year, day)
