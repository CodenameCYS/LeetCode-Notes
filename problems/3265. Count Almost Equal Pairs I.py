'''
=== 3265. Count Almost Equal Pairs I ===

You are given an array nums consisting of positive integers.
We call two integers x and y in this problem almost equal if both integers can become equal after performing the following operation at most once:  
    - Choose either x or y and swap any two digits within the chosen number.
Return the number of indices i and j in nums where i < j such that nums[i] and nums[j] are almost equal.
Note that it is allowed for an integer to have leading zeros after performing an operation.

Example 1:
    Input: nums = [3,12,30,17,21]
    Output: 2
    Explanation:
    The almost equal pairs of elements are:
    3 and 30. By swapping 3 and 0 in 30, you get 3.
    12 and 21. By swapping 1 and 2 in 12, you get 21.
Example 2:
    Input: nums = [1,1,1,1,1]
    Output: 10
    Explanation:
    Every two elements in the array are almost equal.
Example 3:
    Input: nums = [123,231]
    Output: 0
    Explanation:
    We cannot swap any two digits of 123 or 231 to reach the other.

Constraints:
    1. 2 <= nums.length <= 100
    2. 1 <= nums[i] <= 106
'''
# === 798ms && 16.6MB === #
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        
        def is_almost_equal(x, y):
            if x == y:
                return True
            x, y = str(x), str(y)
            n = max(len(x), len(y))
            x = x.rjust(n, "0")
            y = y.rjust(n, "0")
            cntx, cnty = defaultdict(int), defaultdict(int)
            diff = 0
            for dx, dy in zip(x, y):
                if dx != dy:
                    diff += 1
                    cntx[dx] += 1
                    cnty[dy] += 1
            return diff == 0 or (diff == 2 and all(cntx[d] == cnty[d] for d in "0123456789"))
        
        n = len(nums)
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if is_almost_equal(nums[i], nums[j]):
                    ans += 1
        return ans