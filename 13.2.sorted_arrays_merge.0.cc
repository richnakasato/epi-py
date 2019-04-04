#include <limits>
#include <vector>
#include "test_framework/generic_test.h"
using std::vector;
vector<int> MergeSortedArrays(const vector<vector<int>>& sorted_arrays) {
  // TODO - you fill in here.
  if (sorted_arrays.empty()) return {};
  std::vector<int> curr_idxs(sorted_arrays.size(),0);
  int done_count = 0;
  std::tuple<int,int> min;
  while (done_count < sorted_arrays.size()) {


  }

  return {};
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"sorted_arrays"};
  return GenericTestMain(args, "sorted_arrays_merge.cc",
                         "sorted_arrays_merge.tsv", &MergeSortedArrays,
                         DefaultComparator{}, param_names);
}
