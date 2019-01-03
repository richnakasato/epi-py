from test_framework import generic_test


def even_odd_merge(L):
    # TODO - you fill in here.
    if L and L.next:
        odd_head = odd = L
        even_head = even = L.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head
        L = odd_head
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
