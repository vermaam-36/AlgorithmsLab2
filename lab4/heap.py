import math

from numpy import Inf



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
    if (key<A[i]):
        raise Exception("New Key is smaller than previous key")
    A[i] = key
    while i > 0 and A[_parent(i)]<A[i]:
        temp=A[i]
        A[i] = A[_parent(i)]
        A[_parent(i)] = temp
        i =_parent(i)
    pass

def _max_heapify(A, i):
    """
    Dylan
    Element is in the list but not yet part of the heap. This
    adds i into the heap.
    """
    n = len(A) - 1
    l = _left(i)
    r = _right(i)
    if (l <= n and A[l] > A[i]):
        largest = l
    else:
        largest = i
    if (r <= n and A[r] > A[largest]):
        largest = r
    if (largest != i):
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
    A.append(-Inf)
    _heap_increase_key(A, len(A)-1, key)
    _max_heapify(A, len(A) - 1)
    pass

def heap_extract_max(A):
    """
    Mikey
    Removes the maximum value from the heap and returns it.
    The list size should be reduced by 1.
    """
    n = len(A) - 1
    if n < 0:
        raise Exception("heap underflow")
    max = A[0]
    A[0] = A[n]
    A.pop(n)
    _max_heapify(A, 0)
    return max

    

def build_max_heap(A):
    """
    Dylan
    Takes a list A of unordered elements and reorders the elements
    to construct a max binary heap.
    """
    n = len(A) - 1
    start = n // 2
    for i in range(start, -1, -1):
        _max_heapify(A, i)    
    pass

def heapsort(A):
    """
    Gavin
    Sorts a list of elements by converting the list into a heap
    and then extracting each element from biggest to smallest.
    Note that this is done in place.
    """
    build_max_heap(A)
    n = len(A) - 1
    sorted = [None] * len(A)
    for i in range(n, -1, -1):
        sorted[i] = heap_extract_max(A)
    A += sorted
    pass

    


a = [5,2,7,1,10]
heapsort(a)
print(a)
    

    

    
