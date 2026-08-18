'''
=== 3256. Maximum Value Sum by Placing Three Rooks I ===

You are given a m x n 2D array board representing a chessboard, where board[i][j] represents the value of the cell (i, j).
Rooks in the same row or column attack each other. You need to place three rooks on the chessboard such that the rooks do not attack each other.
Return the maximum sum of the cell values on which the rooks are placed.

Example 1:
    Input: board = [[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]
    Output: 4
    Explanation:
    We can place the rooks in the cells (0, 2), (1, 3), and (2, 1) for a sum of 1 + 1 + 2 = 4.
Example 2:
    Input: board = [[1,2,3],[4,5,6],[7,8,9]]
    Output: 15
    Explanation:
    We can place the rooks in the cells (0, 0), (1, 1), and (2, 2) for a sum of 1 + 5 + 9 = 15.
Example 3:
    Input: board = [[1,1,1],[1,1,1],[1,1,1]]
    Output: 3
    Explanation:
    We can place the rooks in the cells (0, 2), (1, 1), and (2, 0) for a sum of 1 + 1 + 1 = 3.

Constraints:
    1. 3 <= m == board.length <= 100
    2. 3 <= n == board[i].length <= 100
    3. -109 <= board[i][j] <= 109
'''
# === 230ms && 21.7MB === #
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        n, m = len(board), len(board[0])
        ans = -math.inf
        cells = [(board[i][j], i, j) for i in range(n) for j in range(m)]
        cells = sorted(cells, reverse=True)
        N = n * m
        
        def dfs(idx, selected, pre):
            nonlocal ans
            if len(selected) == 3:
                ans = max(ans, pre)
            if idx >= N:
                return
            if pre + sum(x[0] for x in cells[idx: idx+3-len(selected)]) <= ans:
                return
            if selected == [] or all(cells[idx][1] != x and cells[idx][2] != y for x, y in selected):
                dfs(idx+1, selected + [(cells[idx][1], cells[idx][2])], pre + cells[idx][0])
            dfs(idx+1, selected, pre)
            return
        
        dfs(0, [], 0)
        return ans
            
            