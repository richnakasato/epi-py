#include <vector>
#include "test_framework/generic_test.h"
using std::vector;

int SearchFirstOfK(const vector<int>& A, int k) {
  // TODO - you fill in here.
  if (A.empty()) return -1;
  int lhs = 0;
  int rhs = A.size()-1;
  int mid;
  int last = -1;
  while (lhs <= rhs) {
      mid = lhs + (rhs-lhs)/2;
      if (A[mid] == k) {
          last = mid;
          rhs = mid-1;
      }
      else if (A[mid] < k) {
          lhs = mid+1;
      }
      else {
          rhs = mid-1;
      }
  }
  return last;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"A", "k"};
  return GenericTestMain(args, "search_first_key.cc", "search_first_key.tsv",
                         &SearchFirstOfK, DefaultComparator{}, param_names);
}
