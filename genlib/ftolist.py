
def csvtolist(filename):
    """
    takes in a filename and outputs a list
    :param filename: input csv file
    :return: list of entries from the csv file
    """
    file = open(filename, "r")
    filestring = file.readline()
    file.close()
    list = ((''.join(c for c in filestring if c not in '"')).split(","))
    list.sort()
    return list

def fileToIntList(filename):
    lines = [line.rstrip('\n') for line in open(filename)]

    return lines