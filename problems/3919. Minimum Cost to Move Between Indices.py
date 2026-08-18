'''
=== 3919. Minimum Cost to Move Between Indices ===

You are given an integer array nums where nums is strictly increasing.
For each index x, let closest(x) be the adjacent index such that abs(nums[x] - nums[y]) is minimized. If both adjacent indices exist and give the same difference, choose the smaller index.
From any index x, you can move in two ways:
    - To any index y with cost abs(nums[x] - nums[y]), or
    - To closest(x) with cost 1.
You are also given a 2D integer array queries, where each queries[i] = [li, ri].
For each query, calculate the minimum total cost to move from index li to index ri.
Return an integer array ans, where ans[i] is the answer for the ith query.
The absolute difference between two values x and y is defined as abs(x - y).

Example 1:
    Input: nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]
    Output: [6,2,5]
    Explanation:​​​​​​​​​​​​​​​​​​​​
    The closest indices are [1, 0, 1] respectively.
    For [0, 2], the path 0 → 1 → 2 uses a closest move from index 0 to 1 with cost 1 and a move from index 1 to 2 with cost |-2 - 3| = 5, giving total 1 + 5 = 6.
    For [2, 0], the path 2 → 1 → 0 uses two closest moves from index 2 to 1 and from index 1 to 0, each with cost 1, giving total 2.
    For [1, 2], the direct move from index 1 to index 2 has cost |-2 - 3| = 5, which is optimal.
    Thus, ans = [6, 2, 5].
Example 2:
    Input: nums = [0,2,3,9], queries = [[3,0],[1,2],[2,0]]
    Output: [4,1,3]
    Explanation:
    The closest indices are [1, 2, 1, 2] respectively.
    For [3, 0], the path 3 → 2 → 1 → 0 uses closest moves from index 3 to 2 and from 2 to 1, each with cost 1, and a move from 1 to 0 with cost |2 - 0| = 2, giving total 1 + 1 + 2 = 4.
    For [1, 2], the closest move from index 1 to 2 has cost 1.
    For [2, 0], the path 2 → 1 → 0 uses a closest move from index 2 to 1 with cost 1 and a move from 1 to 0 with cost |2 - 0| = 2, giving total 1 + 2 = 3.
    Thus, ans = [4, 1, 3].

Constraints:
    1. 2 <= nums.length <= 105
    2. -109 <= nums[i] <= 109
    3. nums is strictly increasing
    4. 1 <= queries.length <= 105
    5. queries[i] = [li, ri]​​​​​​​
    6. 0 <= li, ri < nums.length
'''
# === 275ms && 64.41MB === #
class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        l2r_costs = [0 for _ in nums]
        for i in range(1, n):
            if i == 1:
                l2r_costs[i] = 1
            else:
                if abs(nums[i] - nums[i-1]) < abs(nums[i-1] - nums[i-2]):
                    l2r_costs[i] = l2r_costs[i-1] + 1
                else:
                    l2r_costs[i] = l2r_costs[i-1] + nums[i] - nums[i-1]

        r2l_costs = [0 for _ in nums]
        for i in range(n-2, -1, -1):
            if i == n-2:
                r2l_costs[i] = 1
            else:
                if abs(nums[i+1] - nums[i]) <= abs(nums[i+1] - nums[i+2]):
                    r2l_costs[i] = r2l_costs[i+1] + 1
                else:
                    r2l_costs[i] = r2l_costs[i+1] + nums[i+1] - nums[i]
        
        def query(i, j):
            if j >= i:
                return l2r_costs[j] - l2r_costs[i]
            else:
                return r2l_costs[j] - r2l_costs[i]

        return [query(i, j) for i, j in queries]


        