# cython: language_level=3
def sum_squares_cython(list arr):
    cdef double total = 0
    cdef int i
    cdef int n = len(arr)
    for i in range(n):
        total += arr[i] * arr[i]
    return total