from test_framework import generic_test

from list_node import ListNode


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    # TODO - you fill in here.
    if L:
        count = 0
        front = back = dummy = ListNode(None)
        dummy.next = L
        while front.next:
            front = front.next
            if count == k:
                back = back.next
            else:
                count += 1
        back.next = back.next.next
        L = dummy.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
