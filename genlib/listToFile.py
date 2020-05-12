"""
Takes a list of numbers and writes them to a file
"""
def listToFile(numberList, filename):
    out_file = open(filename, 'w')
    for item in numberList:
        out_file.write(str(item))
        out_file.write("\n")
    out_file.close()
