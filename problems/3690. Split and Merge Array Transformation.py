'''
=== 3690. Split and Merge Array Transformation ===

You are given two integer arrays nums1 and nums2, each of length n. You may perform the following split-and-merge operation on nums1 any number of times:
    - Choose a subarray nums1[L..R].
    - Remove that subarray, leaving the prefix nums1[0..L-1] (empty if L = 0) and the suffix nums1[R+1..n-1] (empty if R = n - 1).
    - Re-insert the removed subarray (in its original order) at any position in the remaining array (i.e., between any two elements, at the very start, or at the very end).
Return the minimum number of split-and-merge operations needed to transform nums1 into nums2.

Example 1:
    Input: nums1 = [3,1,2], nums2 = [1,2,3]
    Output: 1
    Explanation:
    Split out the subarray [3] (L = 0, R = 0); the remaining array is [1,2].
    Insert [3] at the end; the array becomes [1,2,3].
Example 2:
    Input: nums1 = [1,1,2,3,4,5], nums2 = [5,4,3,2,1,1]
    Output: 3
    Explanation:
    Remove [1,1,2] at indices 0 - 2; remaining is [3,4,5]; insert [1,1,2] at position 2, resulting in [3,4,1,1,2,5].
    Remove [4,1,1] at indices 1 - 3; remaining is [3,2,5]; insert [4,1,1] at position 3, resulting in [3,2,5,4,1,1].
    Remove [3,2] at indices 0 - 1; remaining is [5,4,1,1]; insert [3,2] at position 2, resulting in [5,4,3,2,1,1].
    
Constraints:
    1. 2 <= n == nums1.length == nums2.length <= 6
    2. -105 <= nums1[i], nums2[i] <= 105
    3. nums2 is a permutation of nums1.
'''
# === 315ms && 18.19MB === #
class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        src = tuple(nums1)
        tgt = tuple(nums2)
        if src == tgt:
            return 0
        seen = {src}
        q = [(0, src)]
        while q:
            # print(q)
            op, nums = q.pop(0)
            if nums == tgt:
                return op
            for i in range(n):
                left = nums[:i]
                for j in range(i+1, n+1):
                    right = nums[j:]
                    remain = left + right
                    removed = nums[i:j]
                    # print(f"remain={remain}, removed={removed}")
                    for k in range(len(remain) + 1):
                        nxt = tuple(remain[:k] + removed + remain[k:])
                        if nxt in seen:
                            continue
                        # print(f"ops = {op+1}, src = {nums} -> tgt = {nxt}")
                        seen.add(nxt)
                        q.append((op+1, nxt))
        return -1
