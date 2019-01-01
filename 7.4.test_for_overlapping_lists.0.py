import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from list_node import ListNode


def overlapping_no_cycle_lists(l0, l1):
    # TODO - you fill in here.
    if l0 and l1 and l0.next and l1.next:
        l_head = l_curr = l0
        l_count = 2
        r_head = r_curr = l1
        r_count = 2
        while l_curr and r_curr and l_count and r_count:
            if l_curr is r_curr:
                return l_curr
            l_curr = l_curr.next
            if not l_curr:
                l_count -= 1
                l_head = l_curr = l1 if l_head is l0 else l0
            r_curr = r_curr.next
            if not r_curr:
                r_count -= 1
                r_head = r_curr = l0 if r_head is l1 else l1
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
