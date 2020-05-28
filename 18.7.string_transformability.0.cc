#include <string>
#include <unordered_set>

#include <queue>
#include <tuple>
#include <vector>

#include "test_framework/generic_test.h"

using std::string;
using std::unordered_set;

// assume all strings are same length
int StringDiff(const string& lhs, const string& rhs) {
    if (lhs.size() != rhs.size()) return -1;
    auto count = 0;
    for (auto i=0; i<lhs.size(); ++i) {
        if (lhs[i] != rhs[i]) ++count;
    }
    return count;
}

// finds all words in dict with exactly 1 char diff
std::vector<string> StringNeighbors(const unordered_set<string>& D, const string& s) {
    auto results = std::vector<string>();
    for (string entry : D) {
        if (StringDiff(s, entry) == 1) results.push_back(entry);
    }
    return results;
}

// Uses BFS to find the least steps of transformation.
int TransformString(unordered_set<string> D, const string& s, const string& t) {
    // TODO - you fill in here.
    auto to_visit = std::queue<std::tuple<string,int>>();
    auto visited = unordered_set<string>();
    auto node = std::tuple<string,int>{s,0};
    to_visit.push(node);
    while(!to_visit.empty()) {
        auto temp = to_visit.front();
        auto word = std::get<0>(temp);
        auto distance = std::get<1>(temp);
        to_visit.pop();
        visited.insert(word);
        D.erase(word);
        auto neighbors = StringNeighbors(D, word);
        for (auto n : neighbors) {
            if (n == t) return distance + 1;
            if (visited.find(n) == visited.end()) {
                auto node = std::tuple<string,int>{n, distance + 1};
                to_visit.push(node);
            }
        }
    }
    return -1;
}

int main(int argc, char* argv[]) {
    std::vector<std::string> args{argv + 1, argv + argc};
    std::vector<std::string> param_names{"D", "s", "t"};
    return GenericTestMain(args, "string_transformability.cc",
            "string_transformability.tsv", &TransformString,
            DefaultComparator{}, param_names);
}
