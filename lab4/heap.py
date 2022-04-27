import math



def _parent(i):
    """
    Return the index of the parent of the element at index i.
    Converted from 1-based indexing.
    """
    return int((i - 1) // 2)

def _left(i):
    """
    Returns the index of the left child of the element at index i.
    Converted from 1-based indexing.
    """
    return 2 * i + 1

def _right(i):
    """
    Returns the index of the right child of the element at index i.
    Converted from 1-based indexing.
    """
    return 2 * i + 2

def _heap_increase_key(A, i, key):
    """
    Amish
    "Bubble" a key up the heap.
    """
    pass

def _max_heapify(A, i):
    """
    Dylan
    Element is in the list but not yet part of the heap. This
    adds i into the heap.
    """
    l = _left(i)
    r = _right(i)
    n = len(A)
    largest = None
    if l <= n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        _max_heapify(A, largest)


    pass

def max_heap_insert(A, key):
    """
    Amish
    Inserts an element into the heap. This method
    should append a None value to the list to make
    room for the new key and call _heap_increase_key.
    """
    pass

def heap_extract_max(A):
    """
    Mikey
    Removes the maximum value from the heap and returns it.
    The list size should be reduced by 1.
    """
    pass

def build_max_heap(A):
    """
    Dylan
    Takes a list A of unordered elements and reorders the elements
    to construct a max binary heap.
    """
    n = len(A)
    i = math.floor(n/2)
    for i in range(i, 0):
        _max_heapify(A, i)
    pass

def heapsort(A):
    """
    Gavin
    Sorts a list of elements by converting the list into a heap
    and then extracting each element from biggest to smallest.
    Note that this is done in place.
    """
    pass
    


    

    

    