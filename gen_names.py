#! /usr/bin/env python

import sys
import names_and_lastnames
import argparse

parser = argparse.ArgumentParser(description="Generate a list of random names.")
parser.add_argument(
    "name_structure",
    nargs="?", # Makes the argument optional
    default="fl",
    help="Name structure to generate (e.g., 'fl' for first and last name, 'f' for first name, 'f2l' for first and two last names). Defaults to 'fl'.",
)

args = parser.parse_args()

names = [names_and_lastnames.get_random(args.name_structure) for _ in range(100)]
for name in names:
    print(name)
