#include <string>
#include <unordered_map>
#include <vector>

#include "test_framework/generic_test.h"

using std::string;

bool IsLetterConstructibleFromMagazine(const string& letter_text,
                                       const string& magazine_text) {
    // TODO - you fill in here.
    std::vector<int> alpha(256,0);
    for (const auto& c : letter_text) {
        int i = c - '0';
        --alpha[i];
    }
    for (const auto& c : magazine_text) {
        int i = c - '0';
        ++alpha[i];
    }
    for (size_t i=0; i<alpha.size(); ++i) {
        if (alpha[i] < 0) {
            return false;
        }
    }
    return true;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"letter_text", "magazine_text"};
  return GenericTestMain(args, "is_anonymous_letter_constructible.cc",
                         "is_anonymous_letter_constructible.tsv",
                         &IsLetterConstructibleFromMagazine,
                         DefaultComparator{}, param_names);
}
