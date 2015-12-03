import random
import heapq
import numpy as np

def identity(x):
    return x

def quicksort(arr, threshold=1, smallsort=identity):
    # Can pass in a threshold and alternate sort for small data using the parameters
    # default is traditional quicksort

    if len(arr) <= threshold:
        return smallsort(arr)
    pivot = arr[random.randint(0, len(arr) - 1)] # Randomized partitioning
    l = []
    m = []
    r = []
    for x in arr:
        if x < pivot:
            l.append(x)
        elif x > pivot:
            r.append(x)
        else:
            m.append(x)
    return quicksort(l) + m + quicksort(r)


def mergesort(arr, threshhold=1, smallsort=identity):
    # Can pass in a threshold and alternate sort for small data using the parameters
    # default is traditional mergesort
    el = len(arr)
    if el > threshhold:
        return merge(mergesort(arr[:el//2]), mergesort(arr[el//2:]))
    else:
        return smallsort(arr)

def merge(a1, a2):
    # this code seems bad but whatever
    i = j = 0
    out = []
    while i < len(a1) or j < len(a2):
        if a1[i] < a2[j]:
            out.append(a1[i])
            i+=1
        else:
            out.append(a2[j])
            j+=1
        if i >= len(a1):
            out.extend(a2[j:])
            return out
        if j >= len(a2):
            out.extend(a1[i:])
            return out
    return out

# def radixsort(a):
#     # Does not support sorting with negative numbers in the array
#     n = len(a)
#     max = np.max(a)
#
#     for x in range(max+1):
#         bins = [[] for i in range(n)]
#         for y in a:
#             bins[(y/10**x)%n].append(y)
#         a=[]
#         for section in bins:
#             a.extend(section)
#     return a

def radixsort(random_list):
    len_random_list = len(random_list)
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in random_list:
            least_digit = value % modulus
            least_digit /= div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(new_list[0]) == len_random_list:
            return new_list[0]

        random_list = []
        rd_list_append = random_list.append
        for x in new_list:
            for y in x:
                rd_list_append(y)


def insertionsort(arr):
    for i in range(len(arr)):
        x = arr[i]
        j = i
        while j > 0 and arr[j-1] > x:
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = x
    return arr


def heapsort(arr):
    # using library for heap. Oh well.
    heapq.heapify(arr)
    out = []
    while arr:
        out.append(heapq.heappop(arr))
    return out

if __name__ == "__main__":
    print(quicksort([3,2,1,4,5]))
    print(insertionsort([3,2,1,4,5]))
    print(heapsort([3,2,1,4,5]))
    print(mergesort([3,2,1,4,5]))
    print(merge([1,2,3,4], [2, 2, 3, 5]))

    print(radixsort([1,4,6,4,1,5,7,49,10,11,42,9,2]))

