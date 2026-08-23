'''
=== 4033. Valid K-Unique Subarrays I ===

You are given an integer array nums and an integer k.
You are also given a 2D integer array queries, where queries[i] = [li, ri] represents the subarray nums[li..ri].
For each query, the subarray nums[li..ri] is considered valid if:
    - It contains exactly k distinct numbers, and
    - The frequency of every number in the subarray is even.
Return a boolean array ans, where ans[i] is true if nums[li..ri] is valid, and false otherwise.

Example 1:
    Input: nums = [1,2,2,1], k = 2, queries = [[0,1],[0,3],[1,2]]
    Output: [false,true,false]
    Explanation:
    i	[li, ri]	Subarray	Unique numbers	Frequency	Validity check
    0	[0, 1]	[1, 2]	{1, 2} → 2	{1: 1, 2: 1}	false: Element counts are not even.
    1	[0, 3]	[1, 2, 2, 1]	{1, 2} → 2	{1: 2, 2: 2}	true: Exactly k = 2 distinct elements, all appear an even number of times.
    2	[1, 2]	[2, 2]	{2} → 1	{2: 2}	false: Number of distinct elements is less than k = 2.
    Thus, ans = [false, true, false].
Example 2:
    Input: nums = [3,3,3], k = 1, queries = [[1,2],[0,2]]
    Output: [true,false]
    Explanation:
    i	[li, ri]	Subarray	Unique numbers	Frequency	Validity check
    0	[1, 2]	[3, 3]	{3} → 1	{3: 2}	true: Exactly k = 1 distinct element, appears an even number of times.
    1	[0, 2]	[3, 3, 3]	{3} → 1	{3: 3}	false: 3 does not appear an even number of times.
    Thus, ans = [true, false].

Constraints:
    1. 2 <= n == nums.length <= 105
    2. 1 <= nums[i] <= 105
    3. 1 <= k <= n
    4. 1 <= queries.length <= 105
    5. queries[i] == [li, ri]
    6. 0 <= li < ri <= n - 1
'''
# === 4612ms && 130.79MB === #
class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = self.build(arr)

    def feature_func(self, *args, limit=None):
        ans = defaultdict(int)
        for arg in args:
            for k, v in arg.items():
                ans[k] += v
                if limit is not None and len(ans) > limit:
                    return ans
        return ans

    def build(self, arr):
        n = len(arr)
        tree = [{} for _ in range(2*n)]
        for i in range(n):
            tree[i+n] = {arr[i]:1}
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

    def query(self, lb, rb, limit=None):
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
        return self.feature_func(*nodes, limit=limit)

class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n = len(nums)

        segment_tree = SegmentTree(nums)

        @lru_cache(None)
        def query(l, r, k):
            if (r-l+1) % 2 != 0:
                return False
            cnt = segment_tree.query(l, r, limit=k)
            return len(cnt) == k and all(x % 2 == 0 for x in cnt.values())

        return [query(l, r, k) for l, r in queries]
