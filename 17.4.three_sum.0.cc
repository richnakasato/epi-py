#include <algorithm>
#include <unordered_set>
#include <vector>
#include "test_framework/generic_test.h"
using std::unordered_set;
using std::vector;

// Plan: Store sum of all pairs in set. Iterate through nums and search for
// target - num in set. If found return true, else return false;
// Time: O(N^2)
// Space: O(N^2)

void BuildSet(unordered_set<int>& memo, const vector<int>& nums) {
    for (auto num_a : nums) {
        for (auto num_b : nums) {
            memo.insert(num_a + num_b);
        }
    }
    return;
}

bool HasThreeSumV1(vector<int> A, int t) {
    auto sums = unordered_set<int>{};
    BuildSet(sums, A);
    for (auto num : A) {
        if (sums.find(t-num) != sums.end()) return true;
    }
    return false;
}

bool TwoSumSorted(const vector<int>& sorted_A, int target) {
    int lhs = 0;
    int rhs = sorted_A.size() - 1;
    while (lhs <= rhs) {
        auto sum = sorted_A[lhs] + sorted_A[rhs];
        if (sum == target) return true;
        else if (sum < target) ++lhs;
        else --rhs;
    }
    return false;
}

bool HasThreeSumV2(vector<int> A, int t) {
    std::sort(begin(A), end(A)); // N lg N
    return std::any_of(begin(A), end(A), [&](const int& a){ return TwoSumSorted(A, t-a); }); // N^2
}

bool HasThreeSum(vector<int> A, int t) {
    // TODO - you fill in here.
    //return HasThreeSumV1(A, t);
    return HasThreeSumV2(A, t);
}

int main(int argc, char* argv[]) {
    std::vector<std::string> args{argv + 1, argv + argc};
    std::vector<std::string> param_names{"A", "t"};
    return GenericTestMain(args, "three_sum.cc", "three_sum.tsv", &HasThreeSum,
            DefaultComparator{}, param_names);
}
