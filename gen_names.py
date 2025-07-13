#! /usr/bin/env python

import sys
import names_and_lastnames
import argparse

parser = argparse.ArgumentParser(description="Generate a list of random names.")

# Add required positional argument for the number of names
parser.add_argument("num_names", type=int, help="The number of names to generate.")

parser.add_argument(
    "name_structure",
    help="Name structure to generate (e.g., 'fl' for first and last name, 'f' for first name, 'f2l' for first and two last names).",
)

args = parser.parse_args()

names = [
    names_and_lastnames.get_random(args.name_structure) for _ in range(args.num_names)
]
for name in names:
    print(name)
