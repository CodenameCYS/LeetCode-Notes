'''
=== 3514. Number of Unique XOR Triplets II ===

You are given an integer array nums.
A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.
Return the number of unique XOR triplet values from all possible triplets (i, j, k).

Example 1:
    Input: nums = [1,3]
    Output: 2
    Explanation:
    The possible XOR triplet values are:
    (0, 0, 0) → 1 XOR 1 XOR 1 = 1
    (0, 0, 1) → 1 XOR 1 XOR 3 = 3
    (0, 1, 1) → 1 XOR 3 XOR 3 = 1
    (1, 1, 1) → 3 XOR 3 XOR 3 = 3
    The unique XOR values are {1, 3}. Thus, the output is 2.
Example 2:
    Input: nums = [6,7,8,9]
    Output: 4
    Explanation:
    The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.

Constraints:
    1. 1 <= nums.length <= 1500
    2. 1 <= nums[i] <= 1500
'''
# === 4838ms && 18.2MB === #
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        cache = defaultdict(set)
        cache[1] = set(nums)
        for x in nums:
            for y in nums:
                cache[2].add(x ^ y)
        for x in nums:
            for y in list(cache[2]):
                cache[3].add(x ^ y)
                if len(cache[3]) == 2048:
                    return len(cache[3])
        return len(cache[3])

# === 3279ms && 18.4MB === # 
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        cache = defaultdict(set)
        cache[1] = set(nums)
        cache[2].add(0)
        for i in range(n-1):
            x = nums[i]
            for j in range(i+1, n):
                y = nums[j]
                cache[2].add(x ^ y)
        for x in nums:
            for y in list(cache[2]):
                cache[3].add(x ^ y)
                if len(cache[3]) == 2048:
                    return len(cache[3])
        return len(cache[3])