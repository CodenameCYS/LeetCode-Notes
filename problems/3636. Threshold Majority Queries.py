'''
=== 3636. Threshold Majority Queries ===

You are given an integer array nums of length n and an array queries, where queries[i] = [li, ri, thresholdi].
Return an array of integers ans where ans[i] is equal to the element in the subarray nums[li...ri] that appears at least thresholdi times, selecting the element with the highest frequency (choosing the smallest in case of a tie), or -1 if no such element exists.

Example 1:
    Input: nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]
    Output: [1,-1,2]
    Explanation:
    Query	Sub-array	Threshold	Frequency table	Answer
    [0, 5, 4]	[1, 1, 2, 2, 1, 1]	4	1 → 4, 2 → 2	1
    [0, 3, 3]	[1, 1, 2, 2]	3	1 → 2, 2 → 2	-1
    [2, 3, 2]	[2, 2]	2	2 → 2	2
Example 2:
    Input: nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]
    Output: [3,2,3,2]
    Explanation:
    Query	Sub-array	Threshold	Frequency table	Answer
    [0, 6, 4]	[3, 2, 3, 2, 3, 2, 3]	4	3 → 4, 2 → 3	3
    [1, 5, 2]	[2, 3, 2, 3, 2]	2	2 → 3, 3 → 2	2
    [2, 4, 1]	[3, 2, 3]	1	3 → 2, 2 → 1	3
    [3, 3, 1]	[2]	1	2 → 1	2
 
Constraints:
    1. 1 <= nums.length == n <= 104
    2. 1 <= nums[i] <= 109
    3. 1 <= queries.length <= 5 * 104
    4. queries[i] = [li, ri, thresholdi]
    5. 0 <= li <= ri < n
    6. 1 <= thresholdi <= ri - li + 1
'''
class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = self.build(arr)

    def feature_func(self, *args):
        cnt = defaultdict(int)
        for _cnt in args:
            for k, v in _cnt.items():
                cnt[k] += v
        return cnt

    def build(self, arr):
        n = len(arr)
        tree = [0 for _ in range(2*n)]
        for i in range(n):
            tree[i+n] = {arr[i]: 1}
            # tree[i+n] = defaultdict(int)
            # tree[i+n][arr[i]] += 1
        for i in range(n-1, 0, -1):
            tree[i] = self.feature_func(tree[i<<1], tree[(i<<1) | 1])
        return tree

    def update(self, idx, val):
        idx = idx + self.length
        self.tree[idx] = defaultdict(int)
        self.tree[idx][val] += 1
        while idx > 1:
            self.tree[idx>>1] = self.feature_func(self.tree[idx], self.tree[idx ^ 1])
            idx = idx>>1
        return

    def query(self, lb, rb):
        lb += self.length 
        rb += self.length
        nodes = []
        while lb < rb:
            if lb & 1 == 1:
                nodes.append(self.tree[lb])
                lb += 1
            if rb & 1 == 0:
                nodes.append(self.tree[rb])
                rb -= 1
            lb = lb >> 1
            rb = rb >> 1
        if lb == rb:
            nodes.append(self.tree[rb])
        return self.feature_func(*nodes)
# === 9933ms && 42.30MB === #
class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        segment_tree = SegmentTree(nums)
        # return [-1 for _ in queries]

        def query(l, r, thres):
            cnt = segment_tree.query(l, r)
            valid = [(k, v) for k, v in cnt.items() if v >= thres]
            if valid == []:
                return -1
            max_freq = max(v for k, v in valid)
            return min(k for k, v in valid if v == max_freq)
        
        return [query(l, r, thres) for l, r, thres in queries]
