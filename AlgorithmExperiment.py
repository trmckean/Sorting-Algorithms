# Tyler McKean - Empirical Analysis of Sorting Algorithms

# imports
import random
import timeit
import math
import string

# Size of List to sort
size = 1000000
runningTimes = {}


# MAIN
def main():
    # Instantiate list to sort
    unsorted = createInput(size)

    # Run Mergesort on unsorted list and print result
    run(mergeSort, unsorted)

    # Run Radix sort on unsorted list and print result
    run(radixSort, unsorted)

    # Run Quick Sort on unsorted list and print result
    run(quickSort, unsorted)

    # Run Heap Sort on unsorted list and print result
    run(heapSort, unsorted)

    # Run Python List Sort on unsorted list and print result
    run(pythonSort, unsorted)

    # Print each sorting algorithms runtime
    printTime()


# SORT FUNCTION WRAPPER
def run(sort, unsorted):
    copy = list(unsorted)
    start = timeit.default_timer()
    sort(copy)
    stop = timeit.default_timer()
    runtime = stop - start
    runningTimes[sort.__name__] = runtime
    print sort.__name__
    print runtime


# CREATE INPUT
def createInput(size):
    unsorted = []
    for x in range(size):
        unsorted.append(random.randint(-1000000, 1000000))
    return unsorted


# PRINT RUNTIMES
def printTime():
    for x in runningTimes:
        print x, runningTimes[x]


# MERGESORT
def mergeSort(unsorted):
    if len(unsorted) > 1:
        midpoint = len(unsorted) // 2

        lefthalf = unsorted[:midpoint]
        righthalf = unsorted[midpoint:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                unsorted[k] = lefthalf[i]
                i = i + 1
            else:
                unsorted[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            unsorted[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            unsorted[k] = righthalf[j]
            j = j + 1
            k = k + 1


# RADIXSORT
def radixSort(unsorted):
    maximum = max(unsorted)

    exp = 1
    while maximum / exp > 0:
        countingSort(unsorted, exp)
        exp *= 10


# COUNTINGSORT
def countingSort(unsorted, exp):
    length = len(unsorted)

    output = [0] * (length)

    count = [0] * (10)

    for i in range(0, length):
        index = (unsorted[i] / exp)
        count[(index) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = length - 1
    while i >= 0:
        index = (unsorted[i] / exp)
        output[count[(index) % 10] - 1] = unsorted[i]
        count[(index) % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(unsorted)):
        unsorted[i] = output[i]


# QUICKSORT
def quickSort(unsorted):
    quickSortHelper(unsorted, 0, len(unsorted) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        pivot = random.randint(first, last)
        temp = alist[last]
        alist[last] = alist[pivot]
        alist[pivot] = temp

        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivot = random.randint(first, last)
    temp = alist[last]
    alist[last] = alist[pivot]
    alist[pivot] = temp
    newPivotIndex = first - 1
    for index in xrange(first, last):
        if alist[index] < alist[last]:
            newPivotIndex = newPivotIndex + 1
            temp = alist[newPivotIndex]
            alist[newPivotIndex] = alist[index]
            alist[index] = temp
    temp = alist[newPivotIndex + 1]
    alist[newPivotIndex + 1] = alist[last]
    alist[last] = temp

    return newPivotIndex + 1


# HEAPSORT
def heapSort(alist):
    length = len(alist) - 1
    leastParent = length / 2
    for i in range(leastParent, -1, -1):
        moveDown(alist, i, length)

    for i in range(length, 0, -1):
        if alist[0] > alist[i]:
            swap(alist, 0, i)
            moveDown(alist, 0, i - 1)


def moveDown(alist, first, last):
    largest = 2 * first + 1
    while largest <= last:
        if (largest < last) and (alist[largest] < alist[largest + 1]):
            largest += 1

        if alist[largest] > alist[first]:
            swap(alist, largest, first)
            first = largest
            largest = 2 * first + 1
        else:
            return


def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


# PYTHONSORT
def pythonSort(unsorted):
    unsorted.sort()


# EXECUTE
main()
