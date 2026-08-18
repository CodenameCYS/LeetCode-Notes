'''
=== 3388. Count Beautiful Splits in an Array ===

You are given an array nums.
A split of an array nums is beautiful if:
    - The array nums is split into three non-empty subarrays: nums1, nums2, and nums3, such that nums can be formed by concatenating nums1, nums2, and nums3 in that order.
    - The subarray nums1 is a prefix of nums2 OR nums2 is a prefix of nums3.
Return the number of ways you can make this split.
A subarray is a contiguous non-empty sequence of elements within an array.
A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

Example 1:
    Input: nums = [1,1,2,1]
    Output: 2
    Explanation:
    The beautiful splits are:
    A split with nums1 = [1], nums2 = [1,2], nums3 = [1].
    A split with nums1 = [1], nums2 = [1], nums3 = [2,1].
Example 2:
    Input: nums = [1,2,3,4]
    Output: 0
    Explanation:
    There are 0 beautiful splits.

Constraints:
    1. 1 <= nums.length <= 5000
    2. 0 <= nums[i] <= 50
'''
def z_algorithm(s):
    n = len(s)
    z = [0 for _ in range(n)]
    l, r = -1, -1
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r-l] == s[r]:
                r += 1
            z[i] = r-l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r-l] == s[r]:
                    r += 1
                z[i] = r-l
                r -= 1
    z[0] = n
    return z
# === 5648ms && 18.2MB === #
class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        z = z_algorithm(nums)
        for i in range(1, n-1):
            zi = z_algorithm(nums[i:])
            
            if z[i] >= i:
                # print(f"nums1 = {nums[:i]}, remain = {nums[i:]}, cnt = {n-i-i}")
                ans += (n-i-i)
                for j in range(1, i):
                    if zi[j] >= j:
                        # print(f"nums1 = {nums[:i]}, nums2 = {nums[i:i+j]}, nums3 = {nums[i+j:]}, cnt = 1")
                        ans += 1
            else:
                for j in range(1, n-i):
                    if zi[j] >= j:
                        # print(f"nums1 = {nums[:i]}, nums2 = {nums[i:i+j]}, nums3 = {nums[i+j:]}, cnt = 1")
                        ans += 1
        # print("=" * 10)
        return ans
            
# # zfunc
# def zfunc(s):
#     n = len(s)
#     z = [0]*n
#     l, r = 0, 0 # [l, r)
#     for i in range(1, n):
#         if i<r: z[i]=min(r-i, z[i-l])
#         while i+z[i]<n and s[z[i]] == s[i+z[i]]: z[i]+=1
#         if i+z[i]>r: l, r = i, i+z[i]
#     return z

# class Solution:
#     def beautifulSplits(self, nums: List[int]) -> int:
#         n = len(nums)
#         xz = [set() for _ in range(n)]
#         for i in range(n-1):
#             zz = zfunc(nums[i:])
#             j=i+1
#             while j<n:
#                 if zz[j-i]>=j-i:
#                     # print("match", i, j)
#                     xz[i].add(j)
#                 j+=1
#             # print(i, xz[i])
#         zz = zfunc(nums)
#         r = 0
#         for i in range(1, n-1):
#             for j in range(i+1, n):
#                 if j-i>=i and zz[i]>=i or (n-j>=j-i and j in xz[i]):
#                     print(f"nums1 = {nums[:i]}, nums2 = {nums[i:j]}, nums3 = {nums[j:]}, cnt = {r+1}")
#                     r+=1
#         print("=" * 10)
#         return r