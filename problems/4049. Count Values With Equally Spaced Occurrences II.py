'''
=== 4049. Count Values With Equally Spaced Occurrences II ===

You are given an integer array nums.
An integer x is called special if:
    - x appears at least three times in nums.
    - All occurrences of x are equally spaced in nums. In other words, if all occurrences of x are at indices i1 < i2 < ... < im, then i2 - i1 = i3 - i2 = ... = im - im-1.
Return the number of distinct special integers in nums.

Example 1:
    Input: nums = [1,8,1,5,1,5,8,5]
    Output: 2
    Explanation:
    1 is special because it occurs at equally spaced indices 0, 2, and 4.
    5 is special because it occurs at equally spaced indices 3, 5, and 7.
    8 is not special because it occurs only twice.
    Therefore, the answer is 2.
Example 2:
    Input: nums = [8,8,8,8]
    Output: 1
    Explanation:
    8 is special because it occurs at equally spaced indices 0, 1, 2, and 3. Therefore, the answer is 1.
Example 3:
    Input: nums = [8,6,6,8,8]
    Output: 0
    Explanation:
    8 occurs at indices 0, 3, and 4, which are not equally spaced. 6 occurs only twice. Therefore, no integer is special.

Constraints:
    1. 3 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
'''
# === 328ms && 50.31MB === #
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        cache = defaultdict(list)
        for i, num in enumerate(nums):
            cache[num].append(i)

        def is_special(locs):
            if len(locs) < 3:
                return False
            n = len(locs)
            d = locs[1] - locs[0]
            return all(locs[i+1]-locs[i] == d for i in range(n-1))

        ans = 0
        for k, v in cache.items():
            if is_special(v):
                ans += 1
        return ans