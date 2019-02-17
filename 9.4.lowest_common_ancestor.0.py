import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import deque

def lca(tree, node0, node1):
    # TODO - you fill in here.
    curr = tree
    level_order = deque()
    level_order.append((curr, None))
    parents = dict()
    # T: O(nodes)
    # S: O(2^n)
    while level_order:
        curr, parent = level_order.popleft()
        parents[curr] = parent
        if curr.left:
            level_order.append((curr.left, curr))
        if curr.right:
            level_order.append((curr.right, curr))
    # T: O(nodes)
    # S: O(nodes)
    trace0 = list()
    while node0:
        trace0.append(node0)
        node0 = parents[node0]
    trace0.reverse()
    trace1 = list()
    # T: O(nodes)
    # S: O(nodes)
    while node1:
        trace1.append(node1)
        node1 = parents[node1]
    trace1.reverse()
    parent = None
    # T: O(nodes)
    # S: O(1)
    for i in range(min(len(trace0), len(trace1))):
        if trace0[i] == trace1[i]:
            parent = trace0[i]
        else:
            break
    return parent



@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
