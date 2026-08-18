'''
=== 130. Surrounded Regions ===

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
    X X X X
    X O O X
    X X O X
    X O X X
  After running your function, the board should be:
    X X X X
    X X X X
    X X X X
    X O X X
Explanation:
  Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''
# === 4324ms(5.02%) && 70.7MB(5%) === #
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return board
        m = len(board[0])
        have_visited = set()
    
        def dfs(row, col):
            nonlocal have_visited, n, m
            area = [(row, col)]
            state = row in [0, n-1] or col in [0, m-1]
            if row-1 >= 0 and board[row-1][col] == 'O' and (row-1, col) not in have_visited:
                have_visited.add((row-1, col))
                zone, s = dfs(row-1, col)
                area.extend(zone)
                state = state or s
            if row+1 < n and board[row+1][col] == 'O' and (row+1, col) not in have_visited:
                have_visited.add((row+1, col))
                zone, s = dfs(row+1, col)
                area.extend(zone)
                state = state or s
            if col-1 >= 0 and board[row][col-1] == 'O' and (row, col-1) not in have_visited:
                have_visited.add((row, col-1))
                zone, s = dfs(row, col-1)
                area.extend(zone)
                state = state or s
            if col+1 < m and board[row][col+1] == 'O' and (row, col+1) not in have_visited:
                have_visited.add((row, col+1))
                zone, s = dfs(row, col+1)
                area.extend(zone)
                state = state or s
            return area, state
        
        for i in range(n):
            for j in range(m):
                if (i, j) in have_visited or board[i][j] == 'X':
                    continue
                area, state = dfs(i, j)
                if not state:
                    for r, c in area:
                        board[r][c] = 'X'
        return
    
# === 144ms(81.47%) && 15.7MB(24.37%) === #      
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return board
        m = len(board[0])
        if m == 0:
            return board
        border = set()
    
        def dfs(row, col):
            if row-1 >= 0 and board[row-1][col] == 'O' and (row-1, col) not in border:
                border.add((row-1, col))
                dfs(row-1, col)
            if row+1 < n and board[row+1][col] == 'O' and (row+1, col) not in border:
                border.add((row+1, col))
                dfs(row+1, col)
            if col-1 >= 0 and board[row][col-1] == 'O' and (row, col-1) not in border:
                border.add((row, col-1))
                dfs(row, col-1)
            if col+1 < m and board[row][col+1] == 'O' and (row, col+1) not in border:
                border.add((row, col+1))
                dfs(row, col+1)
            return
        
        for i in range(n):
            if board[i][0] == 'O' and (i, 0) not in border:
                border.add((i, 0))
                dfs(i, 0)
            if board[i][m-1] == 'O' and (i, m-1) not in border:
                border.add((i, m-1))
                dfs(i, m-1)
        for j in range(m):
            if board[0][j] == 'O' and (0, j) not in border:
                border.add((0, j))
                dfs(0, j)
            if board[n-1][j] == 'O' and (n-1,j) not in border:
                border.add((n-1, j))
                dfs(n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i, j) not in border:
                    board[i][j] = 'X'
        return
            
        