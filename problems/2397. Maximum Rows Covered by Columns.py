'''
=== 2397. Maximum Rows Covered by Columns ===

You are given a 0-indexed m x n binary matrix mat and an integer cols, which denotes the number of columns you must choose.
A row is covered by a set of columns if each cell in the row that has a value of 1 also lies in one of the columns of the chosen set.
Return the maximum number of rows that can be covered by a set of cols columns.

Example 1:
    Input: mat = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], cols = 2
    Output: 3
    Explanation:
    As shown in the diagram above, one possible way of covering 3 rows is by selecting the 0th and 2nd columns.
    It can be shown that no more than 3 rows can be covered, so we return 3.
Example 2:
    Input: mat = [[1],[0]], cols = 1
    Output: 2
    Explanation:
    Selecting the only column will result in both rows being covered, since the entire matrix is selected.
    Therefore, we return 2.
    
Constraints:
    1. m == mat.length
    2. n == mat[i].length
    3. 1 <= m, n <= 12
    4. mat[i][j] is either 0 or 1.
    5. 1 <= cols <= n
'''
# === 102ms && 13.9MB === #
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        n, m = len(mat), len(mat[0])
        cache = defaultdict(set)
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    cache[j].add(i)
        
        res = 0
        def dfs(idx, unblock, cnt):
            # print(idx, unblock, cnt)
            nonlocal res
            if idx >= m:
                res = max(res, n - len(unblock))
            elif cnt == 0:
                dfs(idx+1, unblock | cache[idx], cnt)
            else:
                dfs(idx+1, unblock | cache[idx], cnt)
                dfs(idx+1, unblock, cnt-1)
            return
        
        dfs(0, set(), cols)
        # print("=" * 10)
        return res
        
# === 60ms && 14MB === #
class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        n, m = len(mat), len(mat[0])
        cache = defaultdict(set)
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    cache[j].add(i)
        
        def dfs(idx, unblock, cnt):
            if idx >= m:
                return n - len(unblock)
            elif cnt == 0:
                return dfs(idx+1, unblock | cache[idx], cnt)
            else:
                return max(
                    dfs(idx+1, unblock | cache[idx], cnt),
                    dfs(idx+1, unblock, cnt-1)
                )
        
        return dfs(0, set(), cols)
