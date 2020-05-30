#include <stdexcept>
#include <string>
#include <vector>
#include "test_framework/generic_test.h"
#include "test_framework/timed_executor.h"
using std::string;
using std::vector;

// Plan: Copy board. Flood fill all border pieces in copy. Iterate through
// original board and flip 'W' to 'B' if copy is also 'W'.
// Time: O(NxM)
// Space: O(NxM) - copy of board and call stack space

bool CanMove(const vector<vector<char>>& board,
             const int& x,
             const int& y) {
    if (x < 0 || board.size() <= x
            || y < 0 || board[x].size() <= y) return false;
    return board[x][y] == 'W';
}

void FillHelper(vector<vector<char>>& board,
                const int& x,
                const int& y) {
    if (!CanMove(board, x, y)) return;
    board[x][y] = 'B';
    auto moves = vector<std::tuple<int,int>>{{x-1, y}, {x+1, y}, {x, y-1}, {x, y+1}};
    for (auto move : moves) {
        auto next_x = std::get<0>(move);
        auto next_y = std::get<1>(move);
        FillHelper(board, next_x, next_y);
    }
    return;
}

void FillSurroundedRegions(vector<vector<char>>* board_ptr) {
    // TODO - you fill in here.
    vector<vector<char>>& board = *board_ptr;
    vector<vector<char>> board_copy = board;
    auto max_x = board.size() - 1;
    auto max_y = board[0].size() - 1;
    for (auto i=0; i<board_copy.size(); ++i) {
        FillHelper(board_copy, i, 0);
        FillHelper(board_copy, i, board_copy[0].size()-1);
    }
    for (auto i=0; i<board_copy[0].size(); ++i) {
        FillHelper(board_copy, 0, i);
        FillHelper(board_copy, board_copy.size()-1, i);
    }
    for (auto row=0; row<board.size(); ++row) {
        for (auto col=0; col<board[0].size(); ++col) {
            if (board_copy[row][col] == 'W') board[row][col] = 'B';
        }
    }
    return;
}

vector<vector<string>> FillSurroundedRegionsWrapper(
        TimedExecutor& executor, vector<vector<string>> board) {
    vector<vector<char>> char_vector;
    char_vector.resize(board.size());
    for (int i = 0; i < board.size(); i++) {
        for (const string& s : board[i]) {
            if (s.size() != 1) {
                throw std::runtime_error("String size is not 1");
            }
            char_vector[i].push_back(s[0]);
        }
    }

    executor.Run([&] { FillSurroundedRegions(&char_vector); });

    board.clear();
    board.resize(char_vector.size(), {});
    for (int i = 0; i < board.size(); i++) {
        for (char c : char_vector[i]) {
            board[i].emplace_back(1, c);
        }
    }

    return board;
}

int main(int argc, char* argv[]) {
    std::vector<std::string> args{argv + 1, argv + argc};
    std::vector<std::string> param_names{"executor", "board"};
    return GenericTestMain(
            args, "matrix_enclosed_regions.cc", "matrix_enclosed_regions.tsv",
            &FillSurroundedRegionsWrapper, DefaultComparator{}, param_names);
}
