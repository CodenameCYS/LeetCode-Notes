'''
=== 2411. Smallest Subarrays With Maximum Bitwise OR ===

You are given a 0-indexed array nums of length n, consisting of non-negative integers. For each index i from 0 to n - 1, you must determine the size of the minimum sized non-empty subarray of nums starting at i (inclusive) that has the maximum possible bitwise OR.
    - In other words, let Bij be the bitwise OR of the subarray nums[i...j]. You need to find the smallest subarray starting at i, such that bitwise OR of this subarray is equal to max(Bik) where i <= k <= n - 1.
The bitwise OR of an array is the bitwise OR of all the numbers in it.
Return an integer array answer of size n where answer[i] is the length of the minimum sized subarray starting at i with maximum bitwise OR.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [1,0,2,1,3]
    Output: [3,3,2,2,1]
    Explanation:
    The maximum possible bitwise OR starting at any index is 3. 
    - Starting at index 0, the shortest subarray that yields it is [1,0,2].
    - Starting at index 1, the shortest subarray that yields the maximum bitwise OR is [0,2,1].
    - Starting at index 2, the shortest subarray that yields the maximum bitwise OR is [2,1].
    - Starting at index 3, the shortest subarray that yields the maximum bitwise OR is [1,3].
    - Starting at index 4, the shortest subarray that yields the maximum bitwise OR is [3].
    Therefore, we return [3,3,2,2,1]. 
Example 2:
    Input: nums = [1,2]
    Output: [2,1]
    Explanation:
    Starting at index 0, the shortest subarray that yields the maximum bitwise OR is of length 2.
    Starting at index 1, the shortest subarray that yields the maximum bitwise OR is of length 1.
    Therefore, we return [2,1].
 
Constraints:
    1. n == nums.length
    2. 1 <= n <= 105
    3. 0 <= nums[i] <= 109
'''
# === 3063ms && 28.9MB === #
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        def get_digits(x):
            return [int(d) for d in bin(x)[2:][::-1]]
        
        res = [0 for _ in nums]
        
        digits = [0 for _ in range(32)]
        n = len(nums)
        i, j = n-1, n-1
        while i >= 0:
            d = get_digits(nums[i])
            for k, x in enumerate(d):
                digits[k] += x
            # print(digits)
            while j > i:
                d = get_digits(nums[j])
                if any(x == y == 1 for x, y in zip(digits, d)):
                    break
                for k, x in enumerate(d):
                    digits[k] -= x
                j -= 1
            # print(i, j-i+1, digits)
            res[i] = j-i+1
            i -= 1
        return res
        