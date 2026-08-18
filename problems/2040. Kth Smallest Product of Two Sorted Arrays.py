'''
=== 2040. Kth Smallest Product of Two Sorted Arrays ===

Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.

Example 1:
    Input: nums1 = [2,5], nums2 = [3,4], k = 2
    Output: 8
    Explanation: The 2 smallest products are:
    - nums1[0] * nums2[0] = 2 * 3 = 6
    - nums1[0] * nums2[1] = 2 * 4 = 8
    The 2nd smallest product is 8.
Example 2:
    Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
    Output: 0
    Explanation: The 6 smallest products are:
    - nums1[0] * nums2[1] = (-4) * 4 = -16
    - nums1[0] * nums2[0] = (-4) * 2 = -8
    - nums1[1] * nums2[1] = (-2) * 4 = -8
    - nums1[1] * nums2[0] = (-2) * 2 = -4
    - nums1[2] * nums2[0] = 0 * 2 = 0
    - nums1[2] * nums2[1] = 0 * 4 = 0
    The 6th smallest product is 0.
Example 3:
    Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
    Output: -6
    Explanation: The 3 smallest products are:
    - nums1[0] * nums2[4] = (-2) * 5 = -10
    - nums1[0] * nums2[3] = (-2) * 4 = -8
    - nums1[4] * nums2[0] = 2 * (-3) = -6
    The 3rd smallest product is -6.
 
Constraints:
    1. 1 <= nums1.length, nums2.length <= 5 * 104
    2. -105 <= nums1[i], nums2[j] <= 105
    3. 1 <= k <= nums1.length * nums2.length
    4. nums1 and nums2 are sorted.
'''
# === 6955ms && 23.6MB === #
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)

        if n > m:
            return self.kthSmallestProduct(nums2, nums1, k)

        def get_interval():
            s = [nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1]]
            return min(s), max(s)

        def is_kth(val):
            cnt = 0
            for x in nums1:
                if x == 0:
                    cnt = cnt if val < 0 else cnt + m
                elif x < 0:
                    tgt = math.ceil(val / x)
                    cnt += m - bisect.bisect_left(nums2, tgt)
                else:
                    tgt = val // x
                    cnt += bisect.bisect_right(nums2, tgt)
                if cnt >= k:
                    # print(val, cnt)
                    return 1
            # print(val, cnt)
            return -1


        i, j = get_interval()
        # print(i, j)
        if is_kth(i) >= 0:
            return i
        while i < j-1:
            val = (i+j) // 2
            status = is_kth(val)
            if status == 1:
                j = val
            else:
                i = val
        return j