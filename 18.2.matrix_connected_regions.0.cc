#include <deque>
#include <vector>
#include "test_framework/generic_test.h"
#include "test_framework/timed_executor.h"
using std::deque;
using std::vector;

bool IsValid(const vector<deque<bool>>& img, const int x, const int y) {
    if (x < 0 || img.size() <= x || y < 0 || img[0].size() <= y) return false;
    return true;
}

bool CanMove(const vector<deque<bool>>& image,
             const int x,
             const int y,
             const bool target_color) {
    if (!IsValid(image, x, y)) return false;
    return image[x][y] == target_color;
}

void FlipHelper(vector<deque<bool>>& image,
               const int x,
               const int y,
               const bool target_color) {
    image[x][y] = !target_color;
    auto moves = vector<std::tuple<int,int>>{{x-1,y}, {x+1,y}, {x,y-1}, {x,y+1}};
    for (auto move : moves) {
        auto next_x = std::get<0>(move);
        auto next_y = std::get<1>(move);
        if (CanMove(image, next_x, next_y, target_color))
            FlipHelper(image, next_x, next_y, target_color);
    }
    return;
}

void FlipColor(int x, int y, vector<deque<bool>>* image_ptr) {
  // TODO - you fill in here.
  vector<deque<bool>>& image = *image_ptr;
  const auto target_color = image[x][y];
  FlipHelper(image, x, y, target_color);
  return;
}
vector<vector<int>> FlipColorWrapper(TimedExecutor& executor, int x, int y,
                                     vector<vector<int>> image) {
  vector<deque<bool>> b;
  b.reserve(image.size());
  for (const vector<int>& row : image) {
    deque<bool> tmp;
    tmp.resize(row.size());
    for (int i = 0; i < row.size(); ++i) {
      tmp[i] = static_cast<bool>(row[i]);
    }
    b.push_back(tmp);
  }

  executor.Run([&] { FlipColor(x, y, &b); });

  image.resize(b.size());

  for (int i = 0; i < image.size(); ++i) {
    image[i].resize(b.size());
    for (int j = 0; j < image[i].size(); ++j) {
      image[i][j] = b[i][j];
    }
  }
  return image;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "x", "y", "image"};
  return GenericTestMain(args, "matrix_connected_regions.cc", "painting.tsv",
                         &FlipColorWrapper, DefaultComparator{}, param_names);
}
