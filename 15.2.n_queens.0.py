from test_framework import generic_test


def valid_pos(n, move):
    row, col = move
    return 0 <= row < n and 0 <= col < n


def rowcol_hit(queen, move):
    queen_row, queen_col = queen
    row, col = move
    return queen_row == row or queen_col == col


def diag_hit(n, queen, move):
    queen_row, queen_col = queen
    row, col = move
    return False


def valid_move(n, queens, move):
    if not len(queens):
        return valid_pos(n, move)
    for queen in queens:
        if rowcol_hit(queen, move) or diag_hit(n, queen, move):
            return False
    return True


def n_queens(n):
    # TODO - you fill in here.
    queens = list()
    for row in range(n):
        for col in range(n):
            if valid_move(n, queens, (row,col)):
                queens.append((row,col))
    return []


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
