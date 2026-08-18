'''
=== 2527. Find Xor-Beauty of Array ===

You are given a 0-indexed integer array nums.
The effective value of three indices i, j, and k is defined as ((nums[i] | nums[j]) & nums[k]).
The xor-beauty of the array is the XORing of the effective values of all the possible triplets of indices (i, j, k) where 0 <= i, j, k < n.
Return the xor-beauty of nums.
Note that:
    - val1 | val2 is bitwise OR of val1 and val2.
    - val1 & val2 is bitwise AND of val1 and val2.
 
Example 1:
    Input: nums = [1,4]
    Output: 5
    Explanation: 
    The triplets and their corresponding effective values are listed below:
    - (0,0,0) with effective value ((1 | 1) & 1) = 1
    - (0,0,1) with effective value ((1 | 1) & 4) = 0
    - (0,1,0) with effective value ((1 | 4) & 1) = 1
    - (0,1,1) with effective value ((1 | 4) & 4) = 4
    - (1,0,0) with effective value ((4 | 1) & 1) = 1
    - (1,0,1) with effective value ((4 | 1) & 4) = 4
    - (1,1,0) with effective value ((4 | 4) & 1) = 0
    - (1,1,1) with effective value ((4 | 4) & 4) = 4 
    Xor-beauty of array will be bitwise XOR of all beauties = 1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4 = 5.
Example 2:
    Input: nums = [15,45,20,2,34,35,5,44,32,30]
    Output: 34
    Explanation: The xor-beauty of the given array is 34.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
'''
# === 2242ms && 27.8MB === #
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        N = 32
        def num2digits(num):
            digits = [0 for _ in range(N)]
            idx = N-1
            while num != 0:
                digits[idx] = num % 2
                num = num // 2
                idx -= 1
            return digits
        
        def digits2num(digits):
            res = 0
            for d in digits:
                res = res * 2 + d
            return res
        
        cnt = [0 for _ in range(N)]
        for i, num in enumerate(nums):
            digits = num2digits(num)
            for j, d in enumerate(digits):
                cnt[j] += d
        # print(cnt)
            
        n = len(nums)   
        res = [0 for _ in range(N)]
        for i, d in enumerate(cnt):
            res[i] = (d * (n*n - (n-d)*(n-d))) % 2
        # print(res)
        # print("="*10)
        return digits2num(res)
                
        