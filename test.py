import random


def find_min(k, arr, start, end):
    if len(arr) >= 1:
        if start > end:
            return arr[start]
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
    print(arr)

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


# simple tests
test2 = [5, 4, 3, 2, 1]
test1 = [3, 1, 5, 2, 4]
testK1 = 2
print(find_min(testK1, test1, 0, len(test1) - 1))
