from test_framework import generic_test

def helper(left, right):
    if not left and not right:
        return True
    if not left and right:
        return False
    if left and not right:
        return False
    vals = left.data == right.data
    l_bool = helper(left.left, right.right)
    r_bool = helper(left.right, right.left)
    return l_bool and r_bool and vals

def is_symmetric(tree):
    # TODO - you fill in here.
    if not tree:
        return True
    return helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
