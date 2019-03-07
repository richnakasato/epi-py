from test_framework import generic_test

import heapq

def sort_approximately_sorted_array(sequence, k):
    # TODO - you fill in here.
    minheap = list()
    # load heap with k+1 elements to make sure we have the smallest
    for i in range(k+1):
        heapq.heappush(minheap, sequence[i])
    result = list()
    for i in range(k+1, len(sequence)):
        heapq.heappush(minheap, sequence[i])
        result.append(heapq.heappop(minheap))
    while minheap:
        result.append(heapq.heappop(minheap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
