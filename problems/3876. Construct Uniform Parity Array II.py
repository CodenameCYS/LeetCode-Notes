'''
=== 3876. Construct Uniform Parity Array II ===

You are given an array nums1 of n distinct integers.
You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.
For each index i, you must choose exactly one of the following (in any order):
    - nums2[i] = nums1[i]​​​​​​​
    - nums2[i] = nums1[i] - nums1[j], for an index j != i, such that nums1[i] - nums1[j] >= 1
Return true if it is possible to construct such an array, otherwise return false.

Example 1:
    Input: nums1 = [1,4,7]
    Output: true
    Explanation:​​​​​​​​​​​​​​
    Set nums2[0] = nums1[0] = 1.
    Set nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3.
    Set nums2[2] = nums1[2] = 7.
    nums2 = [1, 3, 7], and all elements are odd. Thus, the answer is true.
Example 2:
    Input: nums1 = [2,3]
    Output: false
    Explanation:
    It is not possible to construct nums2 such that all elements have the same parity. Thus, the answer is false.
Example 3:
    Input: nums1 = [4,6]
    Output: true
    Explanation:
    Set nums2[0] = nums1[0] = 4.
    Set nums2[1] = nums1[1] = 6.
    nums2 = [4, 6], and all elements are even. Thus, the answer is true.
 
Constraints:
    1. 1 <= n == nums1.length <= 105
    2. 1 <= nums1[i] <= 109
    3. nums1 consists of distinct integers.
'''
# === 203ms && 40.97MB === #
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums = sorted([(num, i) for i, num in enumerate(nums1)])
        flag = nums[0][0] % 2
        cnt = defaultdict(int)
        for num, idx in nums:
            if num % 2 != flag and cnt[1] == 0:
                return False
            cnt[num%2] += 1
            if cnt[1] > 0:
                break
        return True
        