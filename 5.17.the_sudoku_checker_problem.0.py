from test_framework import generic_test


def dupe_check(A):
    L = list()
    S = set()
    for num in A:
        if num != 0:
            L.append(num)
            S.add(num)
    return len(L) != len(S)


def convert_submatrix(M, i, j):
    return M[i][j:j+3] + M[i+1][j:j+3] + M[i+2][j:j+3]


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    # TODO - you fill in here.
    for i in range(9):
        row = partial_assignment[i]
        col = [row[i] for row in partial_assignment]
        if dupe_check(row) or dupe_check(col):
            return False
    subs = [0,3,6]
    for row in subs:
        for col in subs:
            sub = convert_submatrix(partial_assignment, row, col)
            if dupe_check(sub):
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
