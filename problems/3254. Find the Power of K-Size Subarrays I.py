'''
=== 3254. Find the Power of K-Size Subarrays I ===

You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
    - Its maximum element if all of its elements are consecutive and sorted in ascending order.
    - -1 otherwise.
You need to find the power of all subarrays of nums of size k.
Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

Example 1:
    Input: nums = [1,2,3,4,3,2,5], k = 3
    Output: [3,4,-1,-1,-1]
    Explanation:
    There are 5 subarrays of nums of size 3:
    [1, 2, 3] with the maximum element 3.
    [2, 3, 4] with the maximum element 4.
    [3, 4, 3] whose elements are not consecutive.
    [4, 3, 2] whose elements are not sorted.
    [3, 2, 5] whose elements are not consecutive.
Example 2:
    Input: nums = [2,2,2,2,2], k = 4
    Output: [-1,-1]
    Example 3:
    Input: nums = [3,2,3,2,3,2], k = 2
    Output: [-1,3,-1,3,-1]

Constraints:
    1. 1 <= n == nums.length <= 500
    2. 1 <= nums[i] <= 105
    3. 1 <= k <= n
'''
# === 89ms && 16.8MB === #
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            j = i
            while j < n-1 and nums[j+1] == nums[j]+1:
                j += 1
            m = j-i+1
            if m >= k:
                ans += [-1] * (k-1) + nums[i+k-1:j+1]
            else:
                ans += [-1] * m
            i = j+1
        #     print(ans)
        # print("=" * 10)
        return ans[k-1:]