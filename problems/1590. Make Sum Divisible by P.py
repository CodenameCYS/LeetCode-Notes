'''
=== 1590. Make Sum Divisible by P ===

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
A subarray is defined as a contiguous block of elements in the array.

Example 1:
    Input: nums = [3,1,4,2], p = 6
    Output: 1
    Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:
    Input: nums = [6,3,5,2], p = 9
    Output: 2
    Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:
    Input: nums = [1,2,3], p = 3
    Output: 0
    Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
Example 4:
    Input: nums = [1,2,3], p = 7
    Output: -1
    Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.
Example 5:
    Input: nums = [1000000000,1000000000,1000000000], p = 3
    Output: 0
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
    3. 1 <= p <= 109
'''
import math
import collections
# === 916ms && 58.5MB === #
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:        
        r = 0
        counter = collections.defaultdict(list)
        counter[0] = [0]
        for idx, n in enumerate(nums):
            r = (r + n) % p
            counter[r].append(idx+1)
        if r == 0:
            return 0
        
        @lru_cache(None)
        def get_min(r1, r2):
            s1 = counter.get(r1, [])
            s2 = counter.get(r2, [])
            n1 = len(s1)
            n2 = len(s2)
            i = 0
            j = 0
            ans = math.inf
            while i < n1:
                while j < n2 and s2[j] < s1[i]:
                    j += 1
                if j == n2:
                    break
                while i < n1 and s1[i] < s2[j]:
                    i += 1
                ans = min(ans, s2[j]-s1[i-1])
            return ans
        
        ans = math.inf
        for i in counter.keys():
            tgt = (i + r) % p
            ans = min(ans, get_min(i, tgt))
        return ans if ans != len(nums) else -1
    
# === 584ms && 32.3MB === #  
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:     
        n = len(nums)
        r = sum(nums) % p
        if r == 0:
            return 0
        counter = {0: 0}
        ans = n
        s = 0
        for idx, k in enumerate(nums):
            s = (s + k) % p
            tgt = (s - r + p) % p
            if tgt in counter:
                ans = min(ans, idx+1 - counter[tgt])
            counter[s] = idx+1
            # print(counter, ans)
        # print(counter, ans)
        return ans if ans != n else -1        
            