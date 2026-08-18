'''
=== 1632. Rank Transform of a Matrix ===

Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].
The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:
    - If an element is the smallest element in its row and column, then its rank is 1.
    - If two elements p and q are in the same row or column, then:
        - If p < q then rank(p) < rank(q)
        - If p == q then rank(p) == rank(q)
        - If p > q then rank(p) > rank(q)
    - The rank should be as small as possible.
It is guaranteed that answer is unique under the given rules.

Example 1:
    Input: matrix = [[1,2],[3,4]]
    Output: [[1,2],[2,3]]
    Explanation:
    The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
    The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
    The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
    The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
Example 2:
    Input: matrix = [[7,7],[7,7]]
    Output: [[1,1],[1,1]]
Example 3:
    Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
    Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
Example 4:
    Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
    Output: [[5,1,4],[1,2,3],[6,3,1]]
 
Constraints:
    1. m == matrix.length
    2. n == matrix[i].length
    3. 1 <= m, n <= 500
    4. -109 <= matrix[row][col] <= 109
'''
class DSU:
    def __init__(self, n, nums):
        self.dsu = [i for i in range(n)]
        self.val = [v for v in nums]
        
    def find(self, x):
        if self.dsu[x] == x:
            return x
        self.dsu[x] = self.find(self.dsu[x])
        return self.dsu[x]
    
    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.dsu[yr] = xr
        self.val[xr] = max(self.val[xr], self.val[yr])
        return
    
    def getval(self, x):
        return self.val[self.find(x)]
# === 1880ms && 56MB === #
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        rank = [[0 for _ in range(m)] for _ in range(n)]
        elems = [[matrix[i][j], i, j] for i in range(n) for j in range(m)]
        elems = sorted(elems)
        # print(elems)
        
        i = 0
        N = len(elems)
        rows = [0 for _ in range(n)]
        cols = [0 for _ in range(m)]
        while i < N:
            flag = elems[i][0]
            candidates = []
            while i < N and elems[i][0] == flag:
                e, r, c = elems[i]
                candidates.append([max(rows[r], cols[c])+1, r, c])
                i += 1
            M = len(candidates)

            def update_candidates(candidates):
                n = len(candidates)
                status = [False for _ in range(n)]
                dsu = DSU(n, [x[0] for x in candidates])
                row_batch = defaultdict(list)
                col_batch = defaultdict(list)
                for i in range(n):
                    row_batch[candidates[i][1]].append(i)
                    col_batch[candidates[i][2]].append(i)
                for batch in row_batch.values():
                    for i in range(len(batch)-1):
                        dsu.union(batch[i], batch[i+1])
                for batch in col_batch.values():
                    for i in range(len(batch)-1):
                        dsu.union(batch[i], batch[i+1])       
                for i in range(n):
                    candidates[i][0] = dsu.getval(i)
                return candidates  
            if len(candidates) > 1:
                candidates = update_candidates(candidates)
            
            for r, ii, jj in candidates:
                rank[ii][jj] = r
                rows[ii] = r
                cols[jj] = r
        return rank