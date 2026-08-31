'''
=== 4035. Maximum Valid Split Positions I ===

You are given an integer array nums.
You may remove at most one element from nums. Let arr be the array of remaining elements in their original order, and let m be its length.
A split position i of arr is valid if:
    - 0 <= i < m - 1, and
    - gcd(arr[0..i]) == gcd(arr[i + 1..m - 1]).
An array of length 1 has no valid split positions.
The score of arr is the number of valid split positions in it.
Return the maximum possible score of arr.
Here, gcd(a) denotes the greatest common divisor of all elements in the array a.

Example 1:
    Input: nums = [10,30,15,10]
    Output: 2
    Explanation:
    One optimal solution is to remove nums[2] = 15. Then arr = [10, 30, 10].
    The split positions are:
    Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
    0	10	10
    1	10	10
    All split positions are valid. Thus, the answer is 2.
Example 2:
    Input: nums = [2,10,14]
    Output: 1
    Explanation:
    One optimal solution is to not remove any element. Then arr = [2, 10, 14].
    The split positions are:
    Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
    0	2	2
    1	2	14
    Only the split position at index 0 is valid. Thus, the answer is 1.
Example 3:
    Input: nums = [2,4]
    Output: 0
    Explanation:
    The only remaining array that has a split position is arr = [2, 4].
    The split positions are:
    Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
    0	2	4
    There are no valid split positions. Thus, the answer is 0.

Constraints:
    1. 2 <= nums.length <= 1000
    2. 1 <= nums[i] <= 109​​​​​​​
'''
# === 9855ms && 19.64MB === #
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        arr = deepcopy(nums)
        l2r, r2l = deepcopy(arr), deepcopy(arr)
        for j in range(n-1):
            l2r[j+1] = gcd(l2r[j], arr[j+1])
            r2l[n-2-j] = gcd(r2l[n-1-j], arr[n-2-j])
        cnt = 0
        for j in range(n-1):
            if l2r[j] == r2l[j+1]:
                cnt += 1
        ans = max(ans, cnt)

        for i in range(n):
            arr = [x for j, x in enumerate(nums) if j != i]
            l2r, r2l = deepcopy(arr), deepcopy(arr)
            for j in range(n-2):
                l2r[j+1] = gcd(l2r[j], arr[j+1])
                r2l[n-3-j] = gcd(r2l[n-2-j], arr[n-3-j])
            cnt = 0
            for j in range(n-2):
                if l2r[j] == r2l[j+1]:
                    cnt += 1
            ans = max(ans, cnt)
        return ans


class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = self.build(arr)

    def feature_func(self, *args):
        if len(args) == 0:
            return 1
        ans = args[0]
        for num in args[1:]:
            ans = gcd(ans, num)
        return ans

    def build(self, arr):
        n = len(arr)
        tree = [0 for _ in range(2*n)]
        for i in range(n):
            tree[i+n] = arr[i]
        for i in range(n-1, 0, -1):
            tree[i] = self.feature_func(tree[2*i], tree[2*i+1])
        return tree

    def update(self, idx, val):
        idx = idx + self.length
        self.tree[idx] = val
        while idx > 1:
            self.tree[idx // 2] = self.feature_func(self.tree[idx], self.tree[idx ^ 1])
            idx = idx // 2
        return

    def query(self, lb, rb):
        lb += self.length 
        rb += self.length
        nodes = []
        while lb < rb:
            if lb % 2 == 1:
                nodes.append(self.tree[lb])
                lb += 1
            if rb % 2 == 0:
                nodes.append(self.tree[rb])
                rb -= 1
            lb = lb // 2
            rb = rb // 2
        if lb == rb:
            nodes.append(self.tree[rb])
        return self.feature_func(*nodes)
# === 2468ms && 20.02MB === #
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)
        segment_tree = SegmentTree(nums)

        def _query(idx):
            left = segment_tree.query(0, idx)
            right = segment_tree.query(idx+1, n-1)
            return left - right

        def query(ban=None):
            # if n == 2 and ban is not None:
            #     return 0
            if _query(0) < 0:
                return 0
            elif _query(n-2) > 0:
                return 0

            if _query(0) == 0:
                lb = 0
            else:
                i, j = 0, n-2
                while j-i>1:
                    m = (i+j) // 2
                    if _query(m) > 0:
                        i = m
                    else:
                        j = m
                lb = j

            if _query(n-2) == 0:
                rb = n-2
            else:
                i, j = 0, n-1
                while j-i>1:
                    m = (i+j) // 2
                    if _query(m) < 0:
                        j = m
                    else:
                        i = m
                rb = i
            # print(ban, lb, rb, _query(lb), _query(lb+1),_query(rb))
            return rb-lb+1 if ban is None or ban < lb or ban > rb else rb-lb

        ans = query()
        _lcm = 10**9+7
        for num in nums:
            _lcm = lcm(_lcm, num)

        for i in range(n):
            segment_tree.update(i, _lcm)
            if i > 0:
                segment_tree.update(i-1, nums[i-1])
            ans = max(ans, query(ban=i))
        return ans

# === 31ms && 19.53MB === #
class Solution:
    def countValidSplit(self, nums: list[int], skip: int) -> int:
        n = len(nums)
        # suf[i] 是后缀 [i,n-1]（除去 skip）的 GCD
        suf = [0] * (n + 1)
        for j in range(n - 1, -1, -1):
            if j != skip:
                suf[j] = gcd(suf[j + 1], nums[j])
            else:
                suf[j] = suf[j + 1]

        cnt = pre = 0
        for j, x in enumerate(nums):
            if j != skip:
                pre = gcd(pre, x)
                # 现在 pre 是前缀 [0,j]（除去 skip）的 GCD
                if pre == suf[j + 1]:
                    cnt += 1
        return cnt

    def maxValidSplits(self, nums: list[int]) -> int:
        ans = self.countValidSplit(nums, -1)  # 不删除元素

        # countValidSplit 只会调用 O(log max(nums)) 次
        g = 0
        for i, x in enumerate(nums):
            if g > 0 and x % g == 0:  # x 不改变前缀 GCD
                continue
            g = gcd(g, x)
            ans = max(ans, self.countValidSplit(nums, i))

        return ans
