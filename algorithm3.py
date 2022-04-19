import random
import time
import numpy as np


def find_min(k, arr, start, end):
    if len(arr) >= 1:
        if start > end:
            start, end = end, start
        pickRand(arr, start, end)

        pivot = sort_around_pivot(arr[0], arr)
        if pivot == k - 1:
            return arr[pivot]

        if k - 1 < pivot:
            return find_min(k, arr, 0, pivot - 1)

        else:
            return find_min(k, arr, pivot + 1, end - 1)


'''
function chooses a random pivot position and swaps index 0 with it
'''


def pickRand(arr, start, end):
    randomIndex = random.randint(start, end)
    arr[0], arr[randomIndex] = arr[randomIndex], arr[0]
    # print(arr)

    return


'''
function will sort around the pivot position putting elements less than pivot
to the left and elements greater than on the right
code from 
https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
'''


def sort_around_pivot(pivot, arr):
    start = 0
    stop = len(arr) - 1
    pivot = start  # pivot

    # a variable to memorize where the
    i = start + 1

    # partition in the array starts from.
    for j in range(start + 1, stop + 1):

        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = \
        arr[i - 1], arr[pivot]
    pivot = i - 1
    return pivot


def boringWay(arr, k):
    quick_sort(arr, 0, len(arr) - 1)
    # print(arr)
    return arr[k - 1]

'''
the following two methods are an implementation of classical(right most pivot)
quickSort.
Code From:
https://www.geeksforgeeks.org/quick-sort/
'''
def quick_sort(array, low, high):
  if low < high:
 
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
 
    # Recursive call on the left of pivot
    quick_sort(array, low, pi - 1)
 
    # Recursive call on the right of pivot
    quick_sort(array, pi + 1, high)

def partition(array, low, high):
 
  # Choose the rightmost element as pivot
  pivot = array[high]
 
  # Pointer for greater element
  i = low - 1
 
  # Traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
 
      # Swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
 
  # Swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
 
  # Return the position from where partition is done
  return i + 1


# simple tests
test1 = [5, 4, 3, 2, 1]
testK1 = 2
test2 = [9, 3, 5, 2, 8]
testK2 = 1


# make benchmarks
def create_reverse(n):
    arr = []
    index = 0
    for x in range(n, 0, -1):
        arr[index] = x
        index += 1
    return arr


def create_sorted(n):
    arr = []
    for x in range(0, n):
        arr[x] = x
    return arr


def create_random(n):
    arr = random.sample(range(0, n), n)
    # arr = []
    # for x in range(0, n):
    #     arr[x] = random.randint(0, n)
    return arr


def benchmark(arr, k, method):
    if method:
        start_time = time.perf_counter()
        boringWay(arr, k)
        end_time = time.perf_counter()
        return end_time - start_time
    else:
        start_time = time.perf_counter()
        print(find_min(k, arr, 0, len(arr) - 1))
        end_time = time.perf_counter()
        return end_time - start_time

for i in range(100):
    arr = create_random(10000)
    benchmark(arr, 15, False)
