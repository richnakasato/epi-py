from test_framework import generic_test


def can_form_palindrome(s):
    # TODO - you fill in here.
    counts = dict()
    for c in s:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    odd_count = 0
    for c,v in counts.items():
        if not c % 2:
            odd_count += 1
    return odd_count < 2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
