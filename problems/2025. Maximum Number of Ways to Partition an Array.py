'''
=== 2025. Maximum Number of Ways to Partition an Array ===

You are given a 0-indexed integer array nums of length n. The number of ways to partition nums is the number of pivot indices that satisfy both conditions:
    - 1 <= pivot < n
    - nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]
You are also given an integer k. You can choose to change the value of one element of nums to k, or to leave the array unchanged.
Return the maximum possible number of ways to partition nums to satisfy both conditions after changing at most one element.

Example 1:
    Input: nums = [2,-1,2], k = 3
    Output: 1
    Explanation: One optimal approach is to change nums[0] to k. The array becomes [3,-1,2].
    There is one way to partition the array:
    - For pivot = 2, we have the partition [3,-1 | 2]: 3 + -1 == 2.
Example 2:
    Input: nums = [0,0,0], k = 1
    Output: 2
    Explanation: The optimal approach is to leave the array unchanged.
    There are two ways to partition the array:
    - For pivot = 1, we have the partition [0 | 0,0]: 0 == 0 + 0.
    - For pivot = 2, we have the partition [0,0 | 0]: 0 + 0 == 0.
Example 3:
    Input: nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
    Output: 4
    Explanation: One optimal approach is to change nums[2] to k. The array becomes [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14].
    There are four ways to partition the array.
 
Constraints:
    1. n == nums.length
    2. 2 <= n <= 105
    3. -105 <= k, nums[i] <= 105
'''
# === 3533ms && 36.5MB === #
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n, s = len(nums), sum(nums)
        res = [0 for _ in range(n)]
        
        cnt = defaultdict(int)
        pre = nums[0]
        cnt[pre] += 1
        for i in range(1, n):
            s_prime = s - nums[i] + k
            res[i] += cnt[s_prime/2]
            pre += nums[i]
            cnt[pre] += 1
        # print(res)
        
        cnt = defaultdict(int)
        post = nums[-1]
        cnt[post] += 1
        for i in range(n-2, -1, -1):
            s_prime = s - nums[i] + k
            res[i] += cnt[s_prime/2]
            post += nums[i]
            cnt[post] += 1
            
        cnt[s] -= 1
        res.append(cnt[s/2])
        
        return max(res)
        