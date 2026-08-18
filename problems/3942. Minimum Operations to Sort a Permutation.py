'''
=== 3942. Minimum Operations to Sort a Permutation ===

You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].
You may perform only the following operations:
    - Reverse the entire array.
    - Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.
Return the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.
A permutation is a rearrangement of all the elements of an array.

Example 1:
    Input: nums = [0,2,1]
    Output: 2
    Explanation:
    Rotate Left by one: [2, 1, 0]
    Reverse the array: [0, 1, 2]
    The array becomes sorted in 2 operations, which is minimal
Example 2:
    Input: nums = [1,0,2]
    Output: 2
    Explanation:
    Reverse the array: [2, 0, 1]
    Rotate Left by one: [0, 1, 2]
    The array becomes sorted in 2 operations, which is minimal.
Example 3:
    Input: nums = [2,0,1,3]
    Output: -1
    Explanation:
    It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.

Constraints:
    1. 1 <= n == nums.length <= 105
    2. 0 <= nums[i] <= n - 1
    3. nums is a permutation of integers from 0 to n - 1.
'''
# === 87ms && 37.50MB === #
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, idx = len(nums), -1
        dnums = nums + nums
        for i in range(n):
            if nums[i] == 0 and all(dnums[i+j] == j for j in range(n)):
                idx = i
                reverse = False
                break
            elif nums[i] == n-1 and all(dnums[i+j] == n-1-j for j in range(n)):
                idx = i
                reverse = True
                break
        if idx == -1:
            return -1
        if reverse:
            return min(1 + idx, 1 + n-idx)
        else:
            return min(idx, 2 + n-idx)