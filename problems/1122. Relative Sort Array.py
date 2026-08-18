'''
=== 1122. Relative Sort Array ===

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:
    Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
    Output: [2,2,2,1,4,3,3,9,6,7,19]
 
Constraints:
    1. arr1.length, arr2.length <= 1000
    2. 0 <= arr1[i], arr2[i] <= 1000
    3. Each arr2[i] is distinct.
    4. Each arr2[i] is in arr1.
'''
# === 36ms & 13.4MB === #
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        tmp1 = {k:0 for k in arr2}
        tmp2 = sorted([it for it in arr1 if it not in arr2])
        for it in arr1:
            if it in tmp1.keys():
                tmp1[it] += 1
        tmp1 = [[k]*v for k,v in tmp1.items()]
        ans = [it for itl in tmp1 for it in itl] + tmp2
        return ans
        