'''
=== 3695. Maximize Alternating Sum Using Swaps === 

You are given an integer array nums.
You want to maximize the alternating sum of nums, which is defined as the value obtained by adding elements at even indices and subtracting elements at odd indices. That is, nums[0] - nums[1] + nums[2] - nums[3]...
You are also given a 2D integer array swaps where swaps[i] = [pi, qi]. For each pair [pi, qi] in swaps, you are allowed to swap the elements at indices pi and qi. These swaps can be performed any number of times and in any order.
Return the maximum possible alternating sum of nums.

Example 1:
    Input: nums = [1,2,3], swaps = [[0,2],[1,2]]
    Output: 4
    Explanation:
    The maximum alternating sum is achieved when nums is [2, 1, 3] or [3, 1, 2]. As an example, you can obtain nums = [2, 1, 3] as follows.
    Swap nums[0] and nums[2]. nums is now [3, 2, 1].
    Swap nums[1] and nums[2]. nums is now [3, 1, 2].
    Swap nums[0] and nums[2]. nums is now [2, 1, 3].
Example 2:
    Input: nums = [1,2,3], swaps = [[1,2]]
    Output: 2
    Explanation:
    The maximum alternating sum is achieved by not performing any swaps.
Example 3:
    Input: nums = [1,1000000000,1,1000000000,1,1000000000], swaps = []
    Output: -2999999997
    Explanation:
    Since we cannot perform any swaps, the maximum alternating sum is achieved by not performing any swaps.

Constraints:
    1. 2 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
    3. 0 <= swaps.length <= 105
    4. swaps[i] = [pi, qi]
    5. 0 <= pi < qi <= nums.length - 1
    6. [pi, qi] != [pj, qj]
'''
class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        
    def find(self, k):
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
        return
# === 439ms && 64.76MB === #
class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        
        dsu = DSU(n)
        for i, j in swaps:
            dsu.union(i, j)
        groups = defaultdict(list)
        for i in range(n):
            key = dsu.find(i)
            groups[key].append((nums[i], i))
        ans = 0
        for elems in groups.values():
            vals, even = [], 0
            for num, idx in elems:
                vals.append(num)
                if idx % 2 == 0:
                    even += 1
            m = len(vals)
            s = sum(vals)
            if m == even:
                ans += s
            elif even == 0:
                ans -= s
            else:
                vals = sorted(vals, reverse=True)
                d = sum(vals[even:])
                ans += s - d*2
        return ans