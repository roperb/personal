"""
Reads File assuming a list of numbers, strips off the '\n' character and
changes the strings to integers.
"""
def fileToIntList(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    for i in range(len(lines)):
        lines[i]=int(lines[i])
    return lines

def fileToList(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    finalList = []
    for i in range(len(lines)):
        tempList = []
        for entry in lines[i]:
            tempList.append(entry)
        j = 0
        finalTempList = []
        while j <= len(tempList):
            finalTempList.append(int(tempList[j]+tempList[j+1]))
            j+=3
        finalList.append(finalTempList)
    return finalList

"""
def fileToIntList(filename):
    lines = [line.rstrip('\n') for line in open(filename)]

    for i in range(len(lines)):
        lines[i]=int(lines[i])
    return lines
"""
