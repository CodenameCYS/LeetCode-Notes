'''
=== 3943. Number of Pairs After Increment ===

You are given two integer arrays nums1 and nums2, and a 2D integer array queries.
Each queries[i] is one of the following types:
    - [1, x, y, val] – Add val to every element in nums2[x..y].
    - [2, tot] – Compute the number of pairs (j, k) such that nums1[j] + nums2[k] == tot.
Return an integer array answer, where answer[j] is the number of pairs for the jth query of type 2.

Example 1:
    Input: nums1 = [1,2], nums2 = [3,4], queries = [[2,5],[1,0,0,2],[2,5]]
    Output: [2,1]
    Explanation:
    queries[0] = [2, 5]: Valid pairs are nums1[0] + nums2[1] = 1 + 4 = 5 and nums1[1] + nums2[0] = 2 + 3 = 5.
    queries[1] = [1, 0, 0, 2]: Add 2 to nums2[0], resulting in nums2 = [5, 4].
    queries[2] = [2, 5]: Valid pair is nums1[0] + nums2[1] = 1 + 4 = 5.
    Thus, the answer = [2, 1].
Example 2:
    Input: nums1 = [1,1], nums2 = [2,2,3], queries = [[2,4],[1,0,1,1],[2,4]]
    Output: [2,6]
    Explanation:
    queries[0] = [2, 4]: Valid pairs are nums1[0] + nums2[2] = 1 + 3 and nums1[1] + nums2[2] = 1 + 3.
    queries[1] = [1, 0, 1, 1]: Add 1 to nums2[0] and nums2[1], resulting in nums2 = [3, 3, 3].
    queries[2] = [2, 4]: Every element of nums1 = [1, 1] pairs with every element of nums2 = [3, 3, 3] as 1 + 3 = 4. That gives 2 × 3 = 6 pairs in total.
    Thus, the answer = [2, 6].
Example 3:
    Input: nums1 = [2,5,8,4], nums2 = [1,3,8], queries = [[2,9],[1,1,2,1],[2,10]]
    Output: [1,0]
    Explanation:
    queries[0] = [2, 9]: Only valid pair is nums1[2] + nums2[0] = 8 + 1 = 9.
    queries[1] = [1, 1, 2, 1]: Add 1 to nums2[1] and nums2[2], resulting in​​​​​​​ nums2 = [1, 4, 9].
    queries[2] = [2, 10]: No pair sums to 10.
    Thus, the answer = [1, 0].
 
Constraints:
    1. 1 <= nums1.length <= 5
    2. 1 <= nums2.length <= 5 * 104
    3. 1 <= nums1[i], nums2[i] <= 105
    4. 1 <= queries.length <= 5 * 104
    5. queries[i].length == 2 or 4
        - queries[i] == [1, x, y, val], or
        - queries[i] == [2, tot]
        - 0 <= x <= y < nums2.length
        - 1 <= val <= 105
        - 1 <= tot <= 109
'''
import numpy as np
import time
import random

class GlobalFreqQuery:
    def __init__(self, arr: list):
        # 使用 int64 防止加法溢出
        self.data = np.array(arr, dtype=np.int64)
        self.n = len(self.data)

    def range_add(self, l: int, r: int, val: int):
        """
        区间 [l, r] 增加 val。
        NumPy 切片是左闭右开，所以要 r+1。
        """
        # 直接向量化操作，这是 NumPy 最快的地方
        self.data[l:r+1] += val

    def query_freq(self, x: int) -> int:
        """
        查询全局数组中值等于 x 的个数。
        利用 NumPy 的布尔掩码和求和，底层是 C 实现。
        """
        # 方法一：布尔索引求和 (对于查找单个值通常很快)
        # return int(np.sum(self.data == x))
        
        # 方法二：使用 unique (如果你经常查不同的值，或者需要一次性看很多值的分布，这个更好)
        # 但这里我们只查一个值，方法一更直接。
        return int(np.count_nonzero(self.data == x))
# === 4190ms && 53.62MB === #
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        
        segment_tree = GlobalFreqQuery(nums2)
        n = len(nums2)

        def query_fn(tot):
            ans = 0
            for x in nums1:
                ans += segment_tree.query_freq(tot-x)
            return ans

        ans = []
        for query in queries:
            if query[0] == 1:
                l, r, val = query[1:]
                segment_tree.range_add(l, r, val)
            else:
                ans.append(query_fn(query[1]))
        return ans
