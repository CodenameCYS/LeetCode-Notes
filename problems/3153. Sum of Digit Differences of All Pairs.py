'''
=== 3153. Sum of Digit Differences of All Pairs ===

You are given an array nums consisting of positive integers where all integers have the same number of digits.
The digit difference between two integers is the count of different digits that are in the same position in the two integers.
Return the sum of the digit differences between all pairs of integers in nums.

Example 1:
    Input: nums = [13,23,12]
    Output: 4
    Explanation:
    We have the following:
    - The digit difference between 13 and 23 is 1.
    - The digit difference between 13 and 12 is 1.
    - The digit difference between 23 and 12 is 2.
    So the total sum of digit differences between all pairs of integers is 1 + 1 + 2 = 4.
Example 2:
    Input: nums = [10,10,10,10]
    Output: 0
    Explanation:
    All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0.

Constraints:
    1. 2 <= nums.length <= 105
    2. 1 <= nums[i] < 109
    3. All integers in nums have the same number of digits.
'''
# === 978ms && 30.3MB === #
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        cnt = defaultdict(lambda : defaultdict(int))
        for num in nums:
            idx = 0
            while num != 0:
                digit = num % 10
                cnt[idx][digit] += 1
                idx += 1
                num = num // 10
        ans = 0
        for idx in cnt:
            digits = cnt[idx].values()
            s = sum(digits)
            i2 = sum(x*x for x in digits)
            ans += (s**2 - i2) // 2
        return ans