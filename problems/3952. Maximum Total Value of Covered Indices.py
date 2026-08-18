'''
=== 3952. Maximum Total Value of Covered Indices ===

You are given an integer array nums of length n and a binary string s of length n, where s[i] == '1' means index i initially contains a token and s[i] == '0' means it does not.
You may perform the following operation any number of times:
    - Choose a token currently located at index i, where i > 0, such that this token has not been moved before.
    - Move this token from index i to index i - 1.
An index is considered covered if it contains a token after all moves.
Return an integer denoting the maximum total value of nums at the covered indices after optimally performing the operations.

Example 1:
    Input: nums = [9,2,6,1], s = "0101"
    Output: 15
    Explanation:
    Initially, indices 1 and 3 contain tokens.
    Move the token from index 3 to index 2.
    Move the token from index 1 to index 0.
    The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 6 = 15.
    Example 2:
    Input: nums = [5,1,4], s = "001"
    Output: 4
    Explanation:
    Initially, only index 2 contains a token.
    It is optimal to leave the token at index 2.
    The covered index is [2], so the total value is nums[2] = 4.
Example 3:
    Input: nums = [9,3,5], s = "011"
    Output: 14
    Explanation:
    Initially, indices 1 and 2 contain tokens.
    Move the token from index 1 to index 0.
    The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 5 = 14.
    
Constraints:
    1. 1 <= n == nums.length == s.length <= 105
    2. 1 <= nums[i] <= 105
    3. ​​​​​​​s[i] is either '0' or '1'
'''
# === 167ms && 32.43MB === #
class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        ans = 0
        i, n = 0, len(nums)
        while i < n:
            j = i
            while j < n and s[j] == '1':
                j += 1
            if s[i] == '1':
                if i == 0:
                    ans += sum(nums[i:j])
                else:
                    ans += sum(nums[i-1:j]) - min(nums[i-1:j])
            i = j+1
        return ans