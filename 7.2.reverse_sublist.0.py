from test_framework import generic_test
from list_node import ListNode


def reverse_helper(head, sz):
    if head and head.next:
        prev = None
        new_tail = curr = head
        count = 0
        while curr and count <= sz:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        new_tail.next = curr
        head = prev
    return head


def reverse_sublist(L, start, finish):
    # TODO - you fill in here.
    if L and L.next and start != finish:
        curr = dummy = ListNode(None)
        dummy.next = L
        count = 1
        while curr.next:
            if count == start:
                curr.next = reverse_helper(curr.next, finish-start)
                break
            else:
                curr = curr.next
            count += 1
        L = dummy.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
