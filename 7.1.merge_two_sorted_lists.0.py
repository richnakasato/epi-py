from test_framework import generic_test
from list_node import ListNode


def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    if L1 and L2:
        curr1, curr2 = L1, L2
        merge = dummy = ListNode(None)
        while curr1 and curr2:
            if curr1.data < curr2.data:
                merge.next = curr1
                curr1 = curr1.next
            else:
                merge.next = curr2
                curr2 = curr2.next
            merge = merge.next
        while curr1:
            merge.next = curr1
            curr1 = curr1.next
            merge = merge.next
        while curr2:
            merge.next = curr2
            curr2 = curr2.next
            merge = merge.next
        return dummy.next
    return L1 if L1 else L2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
