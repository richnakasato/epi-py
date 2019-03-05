from test_framework import generic_test

import heapq


def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    arr_iters = [iter(x) for x in sorted_arrays]
    merged = list()
    for idx,it in enumerate(arr_iters):
        elem = next(it, None)
        if elem is not None:
            heapq.heappush(merged, (elem, idx))
    results = list()
    while merged:
        elem, idx = heapq.heappop(merged)
        results.append(elem)
        elem = next(arr_iters[idx], None)
        if elem is not None:
            heapq.heappush(merged, (elem, idx))
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
