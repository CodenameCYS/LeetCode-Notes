'''
=== 15. 3Sum ===

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
    - The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
# === Time Limit Exceeded === #
class Solution:
    def find(self, nums, st, ed, target):
        if nums[st] == target or nums[ed] == target:
            return True
        if nums[st] > target or nums[ed] < target:
            return False
        while ed - st > 1:
            tmp = int((st + ed)/2)
            if nums[tmp] == target:
                return True
            elif nums[tmp] < target:
                st = tmp
            else:
                ed = tmp
        return False
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        n = len(nums)
        have_seen = set()
        for i, a in enumerate(nums[:-2]):
            if a > 0:
                break
            for j, b in enumerate(nums[i+1:-1]):
                c = -(a+b)
                if c < b:
                    break
                if (a,b) in have_seen:
                    continue
                have_seen.add((a,b))
                if self.find(nums, i+j+2, n-1, c):
                    ans.append([a,b,c])
        return ans
# === 1180ms(35.99%) && 16.2MB(100%) === #            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums = sorted(nums)
        i = 0
        while i < n-2 and nums[i] <= 0:
            a = nums[i]
            j = i+1
            k = n-1
            while j<k:
                b = nums[j]
                c = nums[k]
                if b + c == -a:
                    ans.append([a, b, c])
                    while j<k and nums[j] == b:
                        j += 1 
                    while j<k and nums[k] == c:
                        k -= 1
                elif b + c < -a:
                    while j<k and nums[j] == b:
                        j += 1
                else:
                    while j<k and nums[k] == c:
                        k -= 1
            while i<n-2 and nums[i] == a:
                i += 1
        return ans