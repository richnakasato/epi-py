from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    # TODO - you fill in here.
    if not tree:
        return None
    inorder = list()
    res = list()
    temp = tree
    done = False
    while not done:
        if temp:
            inorder.append(temp)
            temp = temp.left
        else:
            if len(inorder):
                temp = inorder.pop()
                res.append(temp.data)
                temp = temp.right
            else:
                done = True
    largest = len(res) - k
    return res[largest:] if len(res) >= k else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
