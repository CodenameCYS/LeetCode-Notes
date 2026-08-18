'''
=== 31. Next Permutation ===

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:
    Input: nums = [1,2,3]
    Output: [1,3,2]
Example 2:
    Input: nums = [3,2,1]
    Output: [1,2,3]
Example 3:
    Input: nums = [1,1,5]
    Output: [1,5,1]
Example 4:
    Input: nums = [1]
    Output: [1]
 
Constraints:
    1. 1 <= nums.length <= 100
    2. 0 <= nums[i] <= 100
'''
# === 40ms(70.33%) && 14.1MB(100%) === #
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        status = False
        tmp = deepcopy(nums)
        for i in range(n-2, -1, -1):
            for j in range(n-1, i,-1):
                if tmp[i] < tmp[j]:
                    # print(i, j, tmp)
                    tmp[i], tmp[j] = tmp[j], tmp[i]
                    tmp[i+1:] = sorted(tmp[i+1:])
                    status = True
                    # print(tmp)
                    break
            if status:
                break
        if not status:
            for i in range(n // 2):
                nums[i], nums[n-1-i] = nums[n-1-i], nums[i] 
                # print(nums)
        else:
            for i in range(n):
                nums[i] = tmp[i]
        return