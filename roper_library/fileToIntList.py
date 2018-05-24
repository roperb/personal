"""
Reads File assuming a list of numbers, strips off the '\n' character and
changes the strings to integers.
"""
def fileToIntList(filename):
    lines = [line.rstrip('\n') for line in open(filename)]

    return lines
