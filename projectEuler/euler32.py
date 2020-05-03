#Project Euler Problem 32
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

        # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

        # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l

def dtn(diglist):
    num = 0
    n=0
    for dig in diglist:
        num += dig*10**(len(diglist)-(n+1))
        n+=1
    return num

data = list("123456789")
permutations = permutation(data)
permutations
for row in range(len(permutations)):
    for col in range(len(permutations[row])):
        permutations[row][col] = int(permutations[row][col])



pandigprodlist = []

for row in range(len(permutations)):
    for n in range(7):
        for c in range(n+1,8):
            r = c+1
            num = permutations[row]
            #print(dtn(num[:n+1]))
            #print(dtn(num[n+1:c+1]))
            #print(dtn(num[c+1:9]))
            if dtn(num[:n+1])*dtn(num[n+1:c+1]) == dtn(num[c+1:9]):
                pandigprodlist.append(dtn(num[c+1:9]))

pandigprodlist = list(dict.fromkeys(pandigprodlist))
print(sum(pandigprodlist))
