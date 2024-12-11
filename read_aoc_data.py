import os


def read_aoc_data():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    input_path = os.path.join(script_dir, 'input.txt')
    with open(input_path, "r") as file:
        data = file.read()
    return data
