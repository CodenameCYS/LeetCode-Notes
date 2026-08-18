'''
=== 3533. Concatenated Divisibility ===

You are given an array of positive integers nums and a positive integer k.
A permutation of nums is said to form a divisible concatenation if, when you concatenate the decimal representations of the numbers in the order specified by the permutation, the resulting number is divisible by k.
Return the lexicographically smallest permutation (when considered as a list of integers) that forms a divisible concatenation. If no such permutation exists, return an empty list.
A permutation is a rearrangement of all the elements of an array.
An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b.
If the first min(a.length, b.length) elements do not differ, then the shorter array is the lexicographically smaller one.
 
Example 1:
    Input: nums = [3,12,45], k = 5
    Output: [3,12,45]
    Explanation:
    Permutation	Concatenated Value	Divisible by 5
    [3, 12, 45]	31245	Yes
    [3, 45, 12]	34512	No
    [12, 3, 45]	12345	Yes
    [12, 45, 3]	12453	No
    [45, 3, 12]	45312	No
    [45, 12, 3]	45123	No
    The lexicographically smallest permutation that forms a divisible concatenation is [3,12,45].
Example 2:
    Input: nums = [10,5], k = 10
    Output: [5,10]
    Explanation:
    Permutation	Concatenated Value	Divisible by 10
    [5, 10]	510	Yes
    [10, 5]	105	No
    The lexicographically smallest permutation that forms a divisible concatenation is [5,10].
Example 3:
    Input: nums = [1,2,3], k = 5
    Output: []
    Explanation:
    Since no permutation of nums forms a valid divisible concatenation, return an empty list.

Constraints:
    1. 1 <= nums.length <= 13
    2. 1 <= nums[i] <= 105
    3. 1 <= k <= 100
'''
# === 367ms && 38.8MB === #
class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums = sorted(nums)
        
        @lru_cache(None)
        def dp(idx, status, remain):
            if idx == n-1:
                for i in range(n):
                    if status & (1 << i) != 0:
                        continue
                    m = len(str(nums[i]))
                    if (remain * (10**m) + nums[i]) % k == 0:
                        return [nums[i]]
                    else:
                        return []
                    
            for i in range(n):
                if status & (1 << i) != 0:
                    continue
                m = len(str(nums[i]))
                nxt = dp(idx+1, status | (1 << i), (remain * (10**m) + nums[i]) % k )
                if nxt != []:
                    return [nums[i]] + nxt
            return []
        
        return dp(0, 0, 0)