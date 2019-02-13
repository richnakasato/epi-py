from test_framework import generic_test


def is_well_formed(s):
    lookup = {'(' : ')', '{' : '}', '[' : ']'}
    unmatched_parens = list()
    for paren in s:
        if paren in lookup:
            unmatched_parens.append(paren)
        else:
            if unmatched_parens and lookup[unmatched_parens[-1]] == paren:
                unmatched_parens.pop()
            else:
                return False
    return not unmatched_parens


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
