'''
=== 2425. Bitwise XOR of All Pairings ===

You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).
Return the bitwise XOR of all integers in nums3.

Example 1:
    Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
    Output: 13
    Explanation:
    A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
    The bitwise XOR of all these numbers is 13, so we return 13.
Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 0
    Explanation:
    All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
    and nums1[1] ^ nums2[1].
    Thus, one possible nums3 array is [2,5,1,6].
    2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
 
Constraints:
    1. 1 <= nums1.length, nums2.length <= 105
    2. 0 <= nums1[i], nums2[j] <= 109
'''
# === 5859ms && 33MB === #
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        digits1, digits2 = [0 for _ in range(32)], [0 for _ in range(32)]
        for x in nums1:
            k = 0
            while x != 0:
                digits1[k] += x % 2
                x = x // 2
                k += 1
        for x in nums2:
            k = 0
            while x != 0:
                digits2[k] += x % 2
                x = x // 2
                k += 1
        # print(digits1, digits2)
        
        res = 0
        k = 1
        for i in range(32):
            d1 = digits1[i] * (n2 - digits2[i])
            d2 = (n1-digits1[i]) * digits2[i]
            d = (d1 + d2) % 2
            res += k * d
            k *= 2
        return res

# === 2114ms && 32.9MB === #
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        digits1, digits2 = [0 for _ in range(32)], [0 for _ in range(32)]
        for x in nums1:
            x = bin(x)[2:].rjust(32, "0")
            for i in range(32):
                if x[i] == "1":
                    digits1[i] += 1
                    
        for x in nums2:
            x = bin(x)[2:].rjust(32, "0")
            for i in range(32):
                if x[i] == "1":
                    digits2[i] += 1
                    
        
        res = 0
        for i in range(32):
            d1 = digits1[i] * (n2 - digits2[i])
            d2 = (n1-digits1[i]) * digits2[i]
            d = (d1 + d2) % 2
            res = res * 2 + d
        return res