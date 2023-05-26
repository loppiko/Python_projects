import sys
import random
from timeit import default_timer as timer
sys.setrecursionlimit(10000)

def randomArray(lenght):
    A = []
    for i in range(lenght):
        A.append(random.randint(1,1000))
    return A

def notRandomArray(lenght):
    A = []
    A.append(random.randint(1,1000))
    for i in range(1, lenght):
        A.append(random.randint(A[i - 1], 1000 + A[i - 1]))
    return A

def quickSort(A, p, r):
    c = 5
    # print("r: ",r," p:",p)
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q)
        quickSort(A, q+1, r)
    return A

def partition(A, p, r):
    x = A[r] # element wyznaczajacy podział
    i = p-1
    for j in range (p, r+1):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    if i < r:
        return i
    else:
        return i-1


lenght = 1000
listArraysRandom = [randomArray(lenght), randomArray(lenght * 2), randomArray(lenght * 4)]
listArraysNotRandom = [notRandomArray(lenght), notRandomArray(lenght * 2), notRandomArray(lenght * 4)]

print("Random lists")
for A in listArraysRandom:
    start = timer()
    quickSort(A, 0, len(A) - 1)
    stop = timer()
    time = stop - start
    print(len(A), "          |           ",time)
    # print(quickSort(A, 0, len(A) - 1))
# print(bubbleSort(A))

print()
print()
print("Sorted lists")
print("Rozmiar:         |           Czas:")
for A in listArraysNotRandom:
    start = timer()
    quickSort(A, 0, len(A) - 1)
    stop = timer()
    time = stop - start
    print(len(A), "          |           ",time)
    # print(quickSort(A, 0, len(A) - 1))

         ### Wyniki dla QuickSort ### 
# Random lists
# 1000           |            0.005503599997609854
# 2000           |            0.018568600004073232
# 4000           |            0.04720430000452325


# Sorted lists
# Rozmiar:         |           Czas:
# 1000           |            0.10894990002270788
# 2000           |            0.469457000028342
# 4000           |            1.0451957999612205


    ### Wyniki dla QuickSort + BubbleSort ### 
# Random lists
# 1000           |            0.008341999957337976
# 2000           |            0.01999699999578297
# 4000           |            0.04186299996217713


# Sorted lists
# Rozmiar:         |           Czas:
# 1000           |            0.12952279997989535
# 2000           |            0.46824080002261326
# 4000           |            1.3798202999751084