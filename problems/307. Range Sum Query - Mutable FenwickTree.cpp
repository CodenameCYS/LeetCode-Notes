#include <vector>

using std::vector;

class NumArray {
private:
    vector<int> nums;
    vector<int> tree;

    void add(int index, int delta) {
        for (int i = index + 1; i < static_cast<int>(tree.size()); i += i & -i) {
            tree[i] += delta;
        }
    }

    int prefixSum(int end) const {
        int sum = 0;
        for (int i = end; i > 0; i -= i & -i) {
            sum += tree[i];
        }
        return sum;
    }

public:
    explicit NumArray(vector<int>& values)
        : nums(values), tree(values.size() + 1, 0) {
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            add(i, nums[i]);
        }
    }

    void update(int index, int value) {
        int delta = value - nums[index];
        nums[index] = value;
        add(index, delta);
    }

    int sumRange(int left, int right) const {
        return prefixSum(right + 1) - prefixSum(left);
    }
};