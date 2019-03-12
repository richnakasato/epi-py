#include "test_framework/generic_test.h"

int SquareRoot(int k) {
  // TODO - you fill in here.
  if (k < 2) return k;
  int lo = 0;
  int hi = k;
  int last;
  int mid;
  while (lo <= hi) {
      mid = lo + (hi-lo)/2;
      long long square = std::pow(mid,2);
      if (square == k) {
          return mid;
      }
      else if (square < k) {
          last = mid;
          lo = mid + 1;
      }
      else {
          hi = mid - 1;
      }
  }
  return last;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"k"};
  return GenericTestMain(args, "int_square_root.cc", "int_square_root.tsv",
                         &SquareRoot, DefaultComparator{}, param_names);
}
