#include <limits>
#include <memory>
#include "binary_tree_node.h"
#include "test_framework/generic_test.h"
using std::unique_ptr;

bool is_bst_helper(int min,
                   const unique_ptr<BinaryTreeNode<int>>& tree,
                   int max)
{
    if (!tree) return true;
    bool left = is_bst_helper(min, tree->left, tree->data);
    bool curr = (min <= tree->data) && (tree->data <= max);
    bool right = is_bst_helper(tree->data, tree->right, max);
    return left && curr && right;
}

bool IsBinaryTreeBST(const unique_ptr<BinaryTreeNode<int>>& tree) {
  // TODO - you fill in here.
  return is_bst_helper(std::numeric_limits<int>::min(),
                       tree,
                       std::numeric_limits<int>::max());
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"tree"};
  return GenericTestMain(args, "is_tree_a_bst.cc", "is_tree_a_bst.tsv",
                         &IsBinaryTreeBST, DefaultComparator{}, param_names);
}
