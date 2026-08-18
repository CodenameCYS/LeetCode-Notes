'''
=== 3478. Choose K Elements With Maximum Sum ===

You are given two integer arrays, nums1 and nums2, both of length n, along with a positive integer k.
For each index i from 0 to n - 1, perform the following:
    - Find all indices j where nums1[j] is less than nums1[i].
    - Choose at most k values of nums2[j] at these indices to maximize the total sum.
Return an array answer of size n, where answer[i] represents the result for the corresponding index i.

Example 1:
    Input: nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2
    Output: [80,30,0,80,50]
    Explanation:
    For i = 0: Select the 2 largest values from nums2 at indices [1, 2, 4] where nums1[j] < nums1[0], resulting in 50 + 30 = 80.
    For i = 1: Select the 2 largest values from nums2 at index [2] where nums1[j] < nums1[1], resulting in 30.
    For i = 2: No indices satisfy nums1[j] < nums1[2], resulting in 0.
    For i = 3: Select the 2 largest values from nums2 at indices [0, 1, 2, 4] where nums1[j] < nums1[3], resulting in 50 + 30 = 80.
    For i = 4: Select the 2 largest values from nums2 at indices [1, 2] where nums1[j] < nums1[4], resulting in 30 + 20 = 50.
Example 2:
    Input: nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1
    Output: [0,0,0,0]
    Explanation:
    Since all elements in nums1 are equal, no indices satisfy the condition nums1[j] < nums1[i] for any i, resulting in 0 for all positions.

Constraints:
    1. n == nums1.length == nums2.length
    2. 1 <= n <= 105
    3. 1 <= nums1[i], nums2[i] <= 106
    4. 1 <= k <= n
'''
# === 1165ms && 48.3MB === #
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        ans = [0 for _ in range(n)]
        ordered_nums1 = sorted([(x, i) for i, x in enumerate(nums1)])
        pre_max, topk_sum = 0, 0
        cache, topk_elems = [], []
        
        for num, idx in ordered_nums1:
            if num > pre_max:
                for candidate in cache:
                    if len(topk_elems) < k:
                        bisect.insort(topk_elems, candidate)
                        topk_sum += candidate
                    elif topk_elems[0] < candidate:
                        bisect.insort(topk_elems, candidate)
                        topk_sum += candidate - topk_elems[0]
                        topk_elems.pop(0)
                cache = []
                pre_max = num
            
            ans[idx] = topk_sum
            cache.append(nums2[idx])
        return ans