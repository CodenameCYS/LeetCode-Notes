'''
=== 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers ===

Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:
    - Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
    - Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.
 
Example 1:
    Input: nums1 = [7,4], nums2 = [5,2,8,9]
    Output: 1
    Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8). 
Example 2:
    Input: nums1 = [1,1], nums2 = [1,1,1]
    Output: 9
    Explanation: All Triplets are valid, because 1^2 = 1 * 1.
    Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 = nums2[j] * nums2[k].
    Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].
Example 3:
    Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
    Output: 2
    Explanation: There are 2 valid triplets.
    Type 1: (3,0,2).  nums1[3]^2 = nums2[0] * nums2[2].
    Type 2: (3,0,1).  nums2[3]^2 = nums1[0] * nums1[1].
Example 4:
    Input: nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
    Output: 0
    Explanation: There are no valid triplets.
 
Constraints:
    1. 1 <= nums1.length, nums2.length <= 1000
    2. 1 <= nums1[i], nums2[i] <= 10^5
'''
# === 172ms && 14MB === #
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        @lru_cache(None)
        def count_valid(tgt, arr):
            arr = nums1 if arr == 1 else nums2
            n = len(arr)
            st = 0
            ed = n-1
            ans = 0
            while st < ed:
                if arr[st] * arr[ed] > tgt:
                    ed -= 1
                elif arr[st] * arr[ed] < tgt:
                    st += 1
                else:
                    if arr[st] == arr[ed]:
                        ans += (ed-st) * (ed-st+1) // 2
                        break
                    i = st
                    while arr[i] == arr[st]:
                        i += 1
                    j = ed
                    while arr[j] == arr[ed]:
                        j -= 1
                    ans += (i-st) * (ed-j)
                    st = i
                    ed = j  
            return ans
        
        ans = 0
        for n in nums1:
            ans += count_valid(n**2, 2)
        for n in nums2:
            ans += count_valid(n**2, 1)
        return ans