'''
=== 2963. Count the Number of Good Partitions ===

You are given a 0-indexed array nums consisting of positive integers.
A partition of an array into one or more contiguous subarrays is called good if no two subarrays contain the same number.
Return the total number of good partitions of nums.
Since the answer may be large, return it modulo 109 + 7.

Example 1:
    Input: nums = [1,2,3,4]
    Output: 8
    Explanation: The 8 possible good partitions are: ([1], [2], [3], [4]), ([1], [2], [3,4]), ([1], [2,3], [4]), ([1], [2,3,4]), ([1,2], [3], [4]), ([1,2], [3,4]), ([1,2,3], [4]), and ([1,2,3,4]).
Example 2:
    Input: nums = [1,1,1,1]
    Output: 1
    Explanation: The only possible good partition is: ([1,1,1,1]).
Example 3:
    Input: nums = [1,2,1,3]
    Output: 2
    Explanation: The 2 possible good partitions are: ([1,2,1], [3]) and ([1,2,1,3]).
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
'''
# === 938ms && 45.2MB === #
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10**9+7
        
        @lru_cache(None)
        def power(a, b):
            if b == 0:
                return 1
            if b == 1:
                return a % MOD
            return power(a, b//2) * power(a, b-b//2) % MOD
        
        locs = defaultdict(list)
        for i, x in enumerate(nums):
            locs[x].append(i)
        cnt = 0
        max_loc = 0
        for i, x in enumerate(nums):
            if i > max_loc:
                cnt += 1
                max_loc = locs[x][-1]
            else:
                max_loc = max(max_loc, locs[x][-1])
        cnt += 1
        ans = power(2, cnt-1)
        return ans

# === 912ms && 45.1MB === # 
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10**9+7
        
        locs = defaultdict(list)
        for i, x in enumerate(nums):
            locs[x].append(i)
        cnt = 0
        max_loc = 0
        for i, x in enumerate(nums):
            if i > max_loc:
                cnt += 1
                max_loc = locs[x][-1]
            else:
                max_loc = max(max_loc, locs[x][-1])
        cnt += 1
        ans = pow(2, cnt-1, mod=MOD)
        return ans

# === 904ms && 43.4MB === #
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        MOD = 10**9+7
        
        locs = {}
        for i, x in enumerate(nums):
            if x in locs:
                locs[x][1] = i
            else:
                locs[x] = [i, i]
        cnt = 0
        max_loc = 0
        for i, x in enumerate(nums):
            if i > max_loc:
                cnt += 1
                max_loc = locs[x][-1]
            else:
                max_loc = max(max_loc, locs[x][-1])
        cnt += 1
        ans = pow(2, cnt-1, mod=MOD)
        return ans
        