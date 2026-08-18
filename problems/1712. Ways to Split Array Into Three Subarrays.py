'''
=== 1712. Ways to Split Array Into Three Subarrays ===

A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.
You can pick any two different foods to make a good meal.
Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.
Note that items with different indices are considered different even if they have the same deliciousness value.

Example 1:
    Input: deliciousness = [1,3,5,7,9]
    Output: 4
    Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
    Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:
    Input: deliciousness = [1,1,1,3,3,3,7]
    Output: 15
    Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
 
Constraints:
    1. 1 <= deliciousness.length <= 105
    2. 0 <= deliciousness[i] <= 220
'''
# === 1048ms && 27.1MB === #
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9+7
        s = [0] + list(accumulate(nums))
        n = len(nums)
        i, j, k = 1, 2, 2
        ans = 0
        while i < n:
            j = max(i+1, j)
            while j < n and s[j] < 2*s[i]:
                j += 1
            if s[i] > s[n] / 3:
                break
            k = max(j, k)
            while k < n and s[k] <= 0.5 * (s[-1]+s[i]):
                k += 1
            if k > j:
                ans = (ans + k-j) % MOD
            i += 1
        return ans