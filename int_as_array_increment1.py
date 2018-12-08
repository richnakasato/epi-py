from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.
    carry = 1
    for i in reversed(range(len(A))):
        temp = A[i] + carry
        carry = temp//10
        A[i] = temp%10
    if carry:
        return [carry] + A
    else:
        return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
