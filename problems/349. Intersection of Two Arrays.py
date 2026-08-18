'''
=== 349. Intersection of Two Arrays ===

Given two arrays, write a function to compute their intersection.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]
Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]

Note:
    1. Each element in the result must be unique.
    2. The result can be in any order.
'''
# === 44ms(51.35%) & 13.3MB(5.34%) === #
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))