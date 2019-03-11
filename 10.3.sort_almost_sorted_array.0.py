from test_framework import generic_test

import heapq

def sort_approximately_sorted_array(sequence, k):
    # TODO - you fill in here.
    minheap = list()
    for item in sequence:
        heapq.heappush(minheap, item)
        if len(minheap) == k:
            break
    result = list()
    for item in sequence:
        heapq.heappush(minheap, item)
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
