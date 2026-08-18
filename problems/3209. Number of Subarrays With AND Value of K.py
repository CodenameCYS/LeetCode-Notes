'''
=== 3209. Number of Subarrays With AND Value of K ===

Given an array of integers nums and an integer k, return the number of subarrays of nums where the bitwise AND of the elements of the subarray equals k.

Example 1:
    Input: nums = [1,1,1], k = 1
    Output: 6
    Explanation:
    All subarrays contain only 1's.
Example 2:
    Input: nums = [1,1,2], k = 1
    Output: 3
    Explanation:
    Subarrays having an AND value of 1 are: [1,1,2], [1,1,2], [1,1,2].
Example 3:
    Input: nums = [1,2,3], k = 2
    Output: 2
    Explanation:
    Subarrays having an AND value of 2 are: [1,2,3], [1,2,3].

Constraints:
    1. 1 <= nums.length <= 105
    2. 0 <= nums[i], k <= 109
'''
# === 5223ms && 27.4MB === #
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:    
        kdigits = bin(k)[2:].rjust(32, "0")
        # print(kdigits)
        
        ans = 0
        
        pre_forbidden = -1
        lbound = 0
        num = 2**32-1
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            if x & k != k:
                pre_forbidden = i
                lbound = i+1
                num = 2**32-1
                cnt = defaultdict(int)
                # print(i,x,pre_forbidden,lbound,num)
                continue
            digits = bin(x)[2:].rjust(32, "0")
            for j, d in enumerate(digits):
                if d == "0":
                    cnt[j] += 1
            # print(i, x, num, cnt)
            num = num & x
            if num != k:
                continue
            # print(i, x, num, cnt)
            while all(kdigits[j] == "1" or cnt[j] > 0 for j in range(32)):
                digits = bin(nums[lbound])[2:].rjust(32, "0")
                for j, d in enumerate(digits):
                    if d == "0":
                        cnt[j] -= 1
                lbound += 1
            # print(lbound, pre_forbidden, cnt)
            ans += lbound-1-pre_forbidden
        # print("=" * 10)
        return ans
                
        