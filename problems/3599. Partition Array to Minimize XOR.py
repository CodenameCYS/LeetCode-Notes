'''
=== 3599. Partition Array to Minimize XOR ===

You are given an integer array nums and an integer k.
Your task is to partition nums into k non-empty subarrays. For each subarray, compute the bitwise XOR of all its elements.
Return the minimum possible value of the maximum XOR among these k subarrays.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,2,3], k = 2
    Output: 1
    Explanation:
    The optimal partition is [1] and [2, 3].
    XOR of the first subarray is 1.
    XOR of the second subarray is 2 XOR 3 = 1.
    The maximum XOR among the subarrays is 1, which is the minimum possible.
Example 2:
    Input: nums = [2,3,3,2], k = 3
    Output: 2
    Explanation:
    The optimal partition is [2], [3, 3], and [2].
    XOR of the first subarray is 2.
    XOR of the second subarray is 3 XOR 3 = 0.
    XOR of the third subarray is 2.
    The maximum XOR among the subarrays is 2, which is the minimum possible.
Example 3:
    Input: nums = [1,1,2,3,1], k = 2
    Output: 0
    Explanation:
    The optimal partition is [1, 1] and [2, 3, 1].
    XOR of the first subarray is 1 XOR 1 = 0.
    XOR of the second subarray is 2 XOR 3 XOR 1 = 0.
    The maximum XOR among the subarrays is 0, which is the minimum possible.

Constraints:
    1. 1 <= nums.length <= 250
    2. 1 <= nums[i] <= 109
    3. 1 <= k <= n
'''
# === 8373ms && 61.97MB === #
class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(idx, k):
            if n-idx == k:
                return max(nums[idx:])
            elif k == 1:
                ans = 0
                for num in nums[idx:]:
                    ans = ans ^ num
                return ans
            
            ans, post = math.inf, 0
            i, s = idx, 0
            while i < n-k+1:
                s = s ^ nums[i]
                post = max(s, dp(i+1, k-1))
                ans = min(ans, post) 
                i += 1
            # print(idx, ans)
            return ans
        
        return dp(0, k)