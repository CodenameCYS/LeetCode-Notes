'''
=== 3362. Zero Array Transformation III ===

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].
Each queries[i] represents the following action on nums:
    - Decrement the value at each index in the range [li, ri] in nums by at most 1.
    - The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.
Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.

Example 1:
    Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]
    Output: 1
    Explanation:
    After removing queries[2], nums can still be converted to a zero array.
    Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
    Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Example 2:
    Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]
    Output: 2
    Explanation:
    We can remove queries[2] and queries[3].
Example 3:
    Input: nums = [1,2,3,4], queries = [[0,3]]
    Output: -1
    Explanation:
    nums cannot be converted to a zero array even after using all the queries.

Constraints:
    1. 1 <= nums.length <= 105
    2. 0 <= nums[i] <= 105
    3. 1 <= queries.length <= 105
    4. queries[i].length == 2
    5. 0 <= li <= ri < nums.length
'''
class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def build(self, cap, node, l, r):
        if l == r:
            self.tree[node] = cap[l]
            return
        mid = (l + r) // 2
        self.build(cap, 2 * node, l, mid)
        self.build(cap, 2 * node + 1, mid + 1, r)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def down(self, node, l, r):
        if self.lazy[node] != 0:
            mid = (l + r) // 2
            self.tree[2 * node] += self.lazy[node]
            self.lazy[2 * node] += self.lazy[node]
            self.tree[2 * node + 1] += self.lazy[node]
            self.lazy[2 * node + 1] += self.lazy[node]
            # Reset lazy value
            self.lazy[node] = 0

    def update_range(self, node, l, r, ul, ur, delta):
        if ul > r or ur < l:
            return
        if ul <= l and r <= ur:
            self.tree[node] += delta
            self.lazy[node] += delta
            return
        self.down(node, l, r)
        mid = (l + r) // 2
        self.update_range(2 * node, l, mid, ul, ur, delta)
        self.update_range(2 * node + 1, mid + 1, r, ul, ur, delta)
        self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return float('inf')
        if ql <= l and r <= qr:
            return self.tree[node]
        self.down(node, l, r)
        mid = (l + r) // 2
        return min(self.query(2 * node, l, mid, ql, qr),
                   self.query(2 * node + 1, mid + 1, r, ql, qr))

# === 5501ms && 60.3MB === #
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        
        queries = sorted(queries, key=lambda x: (x[1], x[0]))
        
        n = len(nums)
        cnt = [0 for _ in range(n+1)]
        for l, r in queries:
            cnt[l] += 1
            cnt[r+1] -= 1
        cnt = list(accumulate(cnt))
        if any(cnt[i] < nums[i] for i in range(n)):
            return -1
        
        cap = [cnt[i] - nums[i] for i in range(n)]

        st = SegmentTree(n)
        st.build(cap, 1, 0, n - 1)

        k = 0
        for l, r in queries:
            curr = st.query(1, 0, n - 1, l, r)
            if curr >= 1:
                k += 1
                st.update_range(1, 0, n - 1, l, r, -1)

        return k
        
        