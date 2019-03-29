#include <algorithm>
#include <limits>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"

using std::string;
using std::unordered_map;
using std::unordered_set;
using std::vector;

struct Subarray {
    int start, end;
};

Subarray FindSmallestSubarrayCoveringSet(const vector<string> &paragraph,
                                         const unordered_set<string> &keywords)
{
    // TODO - you fill in here.
    unordered_map<string,int> counts;
    int min = std::numeric_limits<int>::max();
    int start = 0;
    int end = 0;
    int lhs = 0;
    int rhs = 0;
    while (lhs < paragraph.size()) {
        if (keywords.find(paragraph[lhs]) != keywords.end()) {
            ++counts[paragraph[lhs]];
        }
        if (counts.size() == keywords.size()) {
            while (rhs < paragraph.size()
                    && counts.size() == keywords.size()) {
                if (keywords.find(paragraph[rhs]) != keywords.end()) {
                    --counts[paragraph[rhs]];
                    if (!counts[paragraph[rhs]]) {
                        counts.erase[paragraph[rhs]];
                    }
                }
                if (counts.size() != keywords.size()) {
                    min = std::min(min, lhs-rhs);
                    if (min == lhs-rhs) {
                        start = rhs;
                        end = lhs;
                    }
                    break;
                }
                ++rhs;
            }
        }
        ++lhs;
    return {start, end};
}

int FindSmallestSubarrayCoveringSetWrapper(TimedExecutor &executor,
                                           const vector<string> &paragraph,
                                           const unordered_set<string> &keywords)
{
    unordered_set<string> copy = keywords;

    auto result = executor.Run(
            [&] { return FindSmallestSubarrayCoveringSet(paragraph, keywords); });

    if (result.start < 0 || result.start >= paragraph.size() || result.end < 0 ||
            result.end >= paragraph.size() || result.start > result.end) {
        throw TestFailure("Index out of range");
    }

    for (int i = result.start; i <= result.end; i++) {
        copy.erase(paragraph[i]);
    }

    if (!copy.empty()) {
        throw TestFailure("Not all keywords are in the range");
    }

    return result.end - result.start + 1;
}

int main(int argc, char *argv[])
{
    std::vector<std::string> args{argv + 1, argv + argc};
    std::vector<std::string> param_names{"executor", "paragraph", "keywords"};
    return GenericTestMain(args, "smallest_subarray_covering_set.cc",
            "smallest_subarray_covering_set.tsv",
            &FindSmallestSubarrayCoveringSetWrapper,
            DefaultComparator{}, param_names);
}
