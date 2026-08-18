'''
=== 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows ===

You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.
You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.

Example 1:
    Input: mat = [[1,3,11],[2,4,6]], k = 5
    Output: 7
    Explanation: Choosing one element from each row, the first k smallest sum are:
    [1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.  
Example 2:
    Input: mat = [[1,3,11],[2,4,6]], k = 9
    Output: 17
Example 3:
    Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
    Output: 9
    Explanation: Choosing one element from each row, the first k smallest sum are:
    [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
Example 4:
    Input: mat = [[1,1,10],[2,2,9]], k = 7
    Output: 12
 
Constraints:
    1. m == mat.length
    2. n == mat.length[i]
    3. 1 <= m, n <= 40
    4. 1 <= k <= min(200, n ^ m)
    5. 1 <= mat[i][j] <= 5000
    6. mat[i] is a non decreasing array.
'''
from copy import deepcopy
# === 1552ms && 18.4MB === #
class Solution:
    def cal_sum(self, mat, loc):
        return sum([r[c] for r, c in zip(mat, loc)])
    
    def get_min_loc(self, next_loc):
        result, loc = next_loc[0]
        idx = 0
        for i, it in enumerate(next_loc):
            r, l = it
            if r < result:
                result = r
                loc = l
                idx = i
        result, loc = next_loc.pop(idx)
        return result, loc
    
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])
        loc = [0 for i in range(m)]
        result = self.cal_sum(mat, loc)
        have_seen = {tuple(loc)}
        next_loc = []
        for _ in range(k-1):
            # print(loc)
            for i in range(m):
                if loc[i] == n-1:
                    continue
                new_loc = deepcopy(loc)
                new_loc[i] = loc[i]+1
                if tuple(new_loc) in have_seen:
                    continue
                next_loc.append([self.cal_sum(mat, new_loc), new_loc])
                have_seen.add(tuple(new_loc))
            result, loc = self.get_min_loc(next_loc)
        
        return result