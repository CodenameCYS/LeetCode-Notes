'''
=== 3187. Peaks in Array ===

A peak in an array arr is an element that is greater than its previous and next element in arr.
You are given an integer array nums and a 2D integer array queries.
You have to process queries of two types:
    - queries[i] = [1, li, ri], determine the count of peak elements in the subarray nums[li..ri].
    - queries[i] = [2, indexi, vali], change nums[indexi] to vali.
Return an array answer containing the results of the queries of the first type in order.
Notes:
    - The first and the last element of an array or a subarray cannot be a peak.
 
Example 1:
    Input: nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]
    Output: [0]
    Explanation:
    First query: We change nums[3] to 4 and nums becomes [3,1,4,4,5].
    Second query: The number of peaks in the [3,1,4,4,5] is 0.
Example 2:
    Input: nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]]
    Output: [0,1]
    Explanation:
    First query: nums[2] should become 4, but it is already set to 4.
    Second query: The number of peaks in the [4,1,4] is 0.
    Third query: The second 4 is a peak in the [4,1,4,2,1].

Constraints:
    1. 3 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
    3. 1 <= queries.length <= 105
    4. queries[i][0] == 1 or queries[i][0] == 2
    5. For all i that:
        - queries[i][0] == 1: 0 <= queries[i][1] <= queries[i][2] <= nums.length - 1
        - queries[i][0] == 2: 0 <= queries[i][1] <= nums.length - 1, 1 <= queries[i][2] <= 105
'''
# === 4598ms && 77.4MB === #
class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = self.build(arr)

    def feature_func(self, *args):
        # get the target feature, such as sum, min or max.
        return sum(args)

    def build(self, arr):
        n = len(arr)
        tree = [0 for _ in range(2*n)]
        for i in range(n):
            tree[i+n] = arr[i]
        for i in range(n-1, 0, -1):
            tree[i] = self.feature_func(tree[i<<1], tree[(i<<1) | 1])
        return tree

    def update(self, idx, val):
        idx = idx + self.length
        self.tree[idx] = val
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

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        peaks = [0 for _ in nums]
        for i in range(1, n-1):
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                peaks[i] = 1
        segment_tree = SegmentTree(peaks)
        
        def query_fn(l, r):
            if l >= r-1:
                return 0
            return segment_tree.query(l+1, r-1)
        
        def update_fn(idx, value):
            if idx-1 >= 0 and idx+1 < n:
                if nums[idx-1] < value and nums[idx+1] < value:
                    segment_tree.update(idx, 1)
                else:
                    segment_tree.update(idx, 0)
            if idx-2 >= 0:
                if nums[idx-2] < nums[idx-1] and value < nums[idx-1]:
                    segment_tree.update(idx-1, 1)
                else:
                    segment_tree.update(idx-1, 0)
            if idx+2 < n:
                if nums[idx+2] < nums[idx+1] and value < nums[idx+1]:
                    segment_tree.update(idx+1, 1)
                else:
                    segment_tree.update(idx+1, 0)
            nums[idx] = value
            return
        
        ans = []
        for query in queries:
            if query[0] == 1:
                ans.append(query_fn(query[1], query[2]))
            else:
                update_fn(query[1], query[2])
        return ans
        