from test_framework import generic_test, test_utils


def helper(A, chosen, curr, res):
    if all(chosen):
        res.append(curr[:])
        return
    for i in range(len(A)):
        if not chosen[i]:
            curr.append(A[i])
            chosen[i] = True
            helper(A, chosen, curr, res)
            chosen[i] = False
            curr.pop()
    return


def permutations(A):
    # TODO - you fill in here.
    chosen = [False] * len(A)
    result = list()
    if len(A):
        helper(A, chosen, list(), result)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
