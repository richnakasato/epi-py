import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A):
    # TODO - you fill in here.
    dst_idx = 0
    last_seen = None
    for src_idx in range(len(A)):
        if A[src_idx] != last_seen:
            A[dst_idx] = A[src_idx]
            dst_idx+=1
        last_seen = A[src_idx]
    return dst_idx



@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
