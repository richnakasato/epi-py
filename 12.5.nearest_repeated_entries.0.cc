#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

#include "test_framework/generic_test.h"

using std::min;
using std::string;
using std::unordered_map;
using std::vector;

int FindNearestRepetition(const vector<string>& paragraph) {
  // TODO - you fill in here.
  if (paragraph.empty()) return -1;
  unordered_map<string,int> memo;
  int closest = paragraph.size()+1;
  for (int i=0; i<paragraph.size(); ++i) {
      string word = paragraph[i];
      if (memo.find(word) != memo.end()) {
          closest = min(closest, i - memo[word]);
      }
      memo[word] = i;
  }
  return closest > paragraph.size() ? -1 : closest;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"paragraph"};
  return GenericTestMain(args, "nearest_repeated_entries.cc",
                         "nearest_repeated_entries.tsv", &FindNearestRepetition,
                         DefaultComparator{}, param_names);
}
