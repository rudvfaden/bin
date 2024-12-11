import os
import sys


def read_aoc_data():
    # Get the directory of the main executing script
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Construct the path to 'input.txt' assuming it is in the same directory
    input_path = os.path.join(script_dir, 'input.txt')

    # Open and read the file
    with open(input_path, "r") as file:
        data = file.read()

    return data
