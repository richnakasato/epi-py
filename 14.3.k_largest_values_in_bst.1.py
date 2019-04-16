from test_framework import generic_test, test_utils


'''
Brute force is inorder traversal, return last k nodes, this is bad because
we don't need the items up to k, just k onwards

Optimal solution is to do a **reverse** inorder traversal so we only get the
last k nodes, when our results list hits len k, we're done
'''
def find_k_largest_in_bst(tree, k):
    # TODO - you fill in here.
    if not tree:
        return None
    done = False
    temp = tree
    reverse_inorder = list()
    results = list()
    while not done:
        if temp:
            reverse_inorder.append(temp)
            temp = temp.right
        else:
            if len(reverse_inorder):
                temp = reverse_inorder.pop()
                results.append(temp.data)
                if len(results == k):
                    done = True
                temp = temp.left
            else:
                done = True
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
