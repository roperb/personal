import random

def boxmethod():
    num_hit = 0

    n = 1000000000
    ntot = 1
    for i in range(n):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        ntot += 1
        if x ** 2 + y ** 2 < 1:
            num_hit += 1
        if (i % 1000000 == 0):
            print("pi is about" + str(4 * num_hit / ntot))



def main():
    boxmethod()

if __name__ == "__main__":
    main()