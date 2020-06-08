#include <algorithm>
#include <string>
#include <vector>
#include "test_framework/generic_test.h"
using std::sort;
using std::string;
using std::vector;

// Plan: 1) sort, then return middle element.
// Time: 1) n log n
// Space: 1) n
string MajoritySearchV1(vector<string>::const_iterator stream_begin,
        const vector<string>::const_iterator stream_end) {
    auto strings = vector<string>{};
    auto it = stream_begin;
    while (it != stream_end) {
        strings.push_back(*it);
        it = next(it);
    }
    sort(begin(strings), end(strings), [](const string& lhs,
                const string& rhs){
            return lhs < rhs;
            });
    return strings[size(strings)/2];
}

string MajoritySearchV2(vector<string>::const_iterator stream_begin,
        const vector<string>::const_iterator stream_end) {
    auto max_count = 0;
    auto max_str = string{};
    auto cur_count = 0;
    auto cur_str = string{};
    auto it = stream_begin;
    while (it != stream_end) {
        if (*it == cur_str) ++cur_count;
        else {
            max_count = std::max(max_count, cur_count);
            if (max_count == cur_count) {
                max_str = cur_str;
            }
            cur_count = 1;
            cur_str = *it;
        }
        it = next(it);
    }
    max_count = std::max(max_count, cur_count);
    if (max_count == cur_count) {
        max_str = cur_str;
    }
    return max_str == "" ? cur_str : max_str;
}

string MajoritySearch(vector<string>::const_iterator stream_begin,
        const vector<string>::const_iterator stream_end) {
    // TODO - you fill in here.
    //return MajoritySearchV1(stream_begin, stream_end);
    return MajoritySearchV2(stream_begin, stream_end);
}
string MajoritySearchWrapper(const vector<string>& stream) {
    return MajoritySearch(cbegin(stream), cend(stream));
}

int main(int argc, char* argv[]) {
    std::vector<std::string> args{argv + 1, argv + argc};
    std::vector<std::string> param_names{"stream"};
    return GenericTestMain(args, "majority_element.cc", "majority_element.tsv",
            &MajoritySearchWrapper, DefaultComparator{},
            param_names);
}
