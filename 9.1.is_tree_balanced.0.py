from test_framework import generic_test

def helper(root):
    if not root:
        return True, 0
    l_bal, l_hgt = helper(root.left)
    r_bal, r_hgt = helper(root.right)
    c_bal = l_bal and r_bal and abs(l_hgt - r_hgt) <= 1
    height = 1 + max(l_hgt, r_hgt)
    return c_bal, height

def is_balanced_binary_tree(tree):
    # TODO - you fill in here.
    if not tree:
        return True
    l_bal, l_hgt = helper(tree.left)
    r_bal, r_hgt = helper(tree.right)
    return l_bal and r_bal and abs(l_hgt - r_hgt) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
