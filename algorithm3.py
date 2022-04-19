import random


def find_min(k, arr, tally):
    pickRand(arr)


    pivot = sort_around_pivot(arr[0], arr)

    if pivot == k - 1 - tally:
        return arr[pivot]

    if k - 1 < pivot:
        find_min(k, arr[0 : pivot], tally)

    else:
        tally += pivot + 1
        find_min(k, arr[pivot + 1 : ], tally)


'''
function chooses a random pivot position and swaps index 0 with it
'''
def pickRand(arr):
    randomIndex = random.randint(0, len(arr) - 1)
    arr[0], arr[randomIndex] = arr[randomIndex], arr[0]

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
    pivot = start # pivot
     
    # a variable to memorize where the
    i = start + 1
     
    # partition in the array starts from.
    for j in range(start + 1, stop + 1):
         
        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)


def boringWay(arr, k):
    quickSort(arr)
    return arr[k - 1]


def quickSort(arr, low, high):
    if(low < high):
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high - 1):
        if(arr[j] < pivot):
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


#simple tests
test1 = [5,4,3,2,1]
testK1 = 2
test2 = [9,3,5,2,8]
testK2 = 1


