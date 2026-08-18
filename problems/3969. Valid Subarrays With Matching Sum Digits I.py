'''
=== 3969. Valid Subarrays With Matching Sum Digits I ===

You are given an integer array nums and an integer digit x.
A subarray nums[l..r] is considered valid if the sum of its elements satisfies both of the following conditions:
    - The first digit of the sum is equal to x.
    - The last digit of the sum is equal to x.
Return the number of valid subarrays.

Example 1:
    Input: nums = [1,100,1], x = 1
    Output: 4
    Explanation:
    The valid subarrays are:
    nums[0..0]: sum = 1
    nums[0..1]: sum = 1 + 100 = 101
    nums[1..2]: sum = 100 + 1 = 101
    nums[2..2]: sum = 1
    Thus, the answer is 4.
Example 2:
    Input: nums = [1], x = 2
    Output: 0
    Explanation:
    The only subarray is nums[0..0] with a sum of 1, which does not satisfy the conditions.
    Thus, the answer is 0.

Constraints:
    1. 1 <= nums.length <= 1500
    2. 1 <= nums[i] <= 109
    3. 1 <= x <= 9
'''
# === 3689ms && 19.78MB === #
class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)
        
        cumsum = list(accumulate(nums, initial=0))
        # cache = defaultdict(list)
        # for s in cumsum:
        #     cache[s%10].append(s)

        ans = 0
        for i in range(n):
            for j in range(i+1, n+1):
                s = cumsum[j]-cumsum[i]
                if s % 10 == x and int(str(s)[0]) == x:
                    ans += 1
        return ans
        # for i in range(n):
        #     tot = cumsum[n-i]
        #     last_digit = tot % 10
        #     first_digit = int(str(tot)[0])
        #     suffix = (tot%10 + 10 - x) % 10
