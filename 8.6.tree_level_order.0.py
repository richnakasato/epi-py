from test_framework import generic_test
from collections import deque

def binary_tree_depth_order(tree):
    # TODO - you fill in here.
    if not tree:
        return list()
    levels = list()
    queue = deque()
    curr_node = tree
    curr_lvl = 0
    queue.append((curr_node, curr_lvl))
    while queue:
        curr_node, curr_lvl = queue.popleft()
        if len(levels) == curr_lvl:
            new_lvl = list()
            new_lvl.append(curr_node.data)
            levels.append(new_lvl)
        else:
            levels[curr_lvl].append(curr_node.data)
        if curr_node.left:
            queue.append((curr_node.left, curr_lvl+1))
        if curr_node.right:
            queue.append((curr_node.right, curr_lvl+1))
    return levels


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
