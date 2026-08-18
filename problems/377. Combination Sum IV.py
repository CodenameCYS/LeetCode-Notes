'''
=== 377. Combination Sum IV ===

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:
    nums = [1, 2, 3]
    target = 4
    The possible combination ways are:
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    - Note that different sequences are counted as different combinations.
    Therefore the output is 7.
 
Follow up:
1. What if negative numbers are allowed in the given array?
2. How does it change the problem?
3. What limitation we need to add to the question to allow negative numbers?

Credits:
- Special thanks to @pbrother for adding this problem and creating all test cases.
'''
# === 60ms(8.85%) && 15.6MB(22.22%) === #
class Solution:
    def __init__(self):
        self.cache = {}
    
    def my_sum_4(self, nums, target):
        if target in self.cache.keys():
            return self.cache[target]
        ans = 0
        for n in nums:
            if n < target:
                ans += self.my_sum_4(nums, target-n)
            elif n == target:
                ans += 1
                break
            else:
                break
        self.cache[target] = ans
        return ans
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = self.my_sum_4(nums, target)
        # print(self.cache)
        return ans