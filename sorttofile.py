import sys
import time


def main():
    f = open("numbers.txt", "r")
    i = 0
    lines = f.read().split(',')
    for i in range(0, len(lines)):
        print(lines[i], end=", ")
        lines[i] = int(lines[i])
    n = len(lines)
    print("\n\n")
    qsort(lines, 0, n - 1)
    print("[", end="")
    for i in range(n):
        print("%s" % lines[i], end=", ")
    sys.stdout.write('\b]\n')


def qsort(arr, low, high):
    if(low < high):
        pi = partition(arr, low, high)
        qsort(arr, low, pi - 1)
        qsort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    j = low
    while (j <= high - 1):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            print(arr, end="\r")
            time.sleep(0.1)
        j = j + 1

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i + 1)


main()
