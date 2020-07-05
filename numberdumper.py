import os
import sys
import random


def main():
    n = int(input("Highest number: "))
    b = int(input("How many numbers: "))
    f = open('numbers.txt', 'w').close()
    f = open('numbers.txt', 'w')
    for i in range(b):
        f.write(str(random.randrange(0, n)) + ",")
    f.close()
    f = open("numbers.txt", "r")
    k = remove_lastchar("numbers.txt")
    f.close()
    f = open("numbers.txt", "w")
    f.write(''.join(k))
    f.close()


def remove_lastchar(f):
    fl = open(f).readlines()
    return [s.rstrip(",") for s in fl]


main()
