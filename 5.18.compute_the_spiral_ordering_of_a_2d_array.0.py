from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    # TODO - you fill in here.
    n = len(square_matrix)
    top = left = 0
    bot = right = n-1
    direction = 0
    result = list()
    while top <= bot and left <= right:
        if direction%4 == 0:
            for i in range(left, right+1):
                result.append(square_matrix[top][i])
            top += 1
        elif direction%4 == 1:
            for i in range(top, bot+1):
                result.append(square_matrix[i][right])
            right -= 1
        elif direction%4 == 2:
            for i in reversed(range(left, right+1)):
                result.append(square_matrix[bot][i])
            bot -= 1
        else:
            for i in reversed(range(top, bot+1)):
                result.append(square_matrix[i][left])
            left += 1
        direction+=1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
