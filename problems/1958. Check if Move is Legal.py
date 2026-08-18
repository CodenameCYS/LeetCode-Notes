'''
=== 1958. Check if Move is Legal ===

You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the cell (r, c) on a game board. On the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'.
Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal).
A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color (no cells in the line are free). You can find examples for good lines in the figure below:
Given two integers rMove and cMove and a character color representing the color you are playing as (white or black), return true if changing cell (rMove, cMove) to color color is a legal move, or false if it is not legal.

Example 1:
    Input: board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
    Output: true
    Explanation: '.', 'W', and 'B' are represented by the colors blue, white, and black respectively, and cell (rMove, cMove) is marked with an 'X'.
    The two good lines with the chosen cell as an endpoint are annotated above with the red rectangles.
Example 2:
    Input: board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"
    Output: false
    Explanation: While there are good lines with the chosen cell as a middle cell, there are no good lines with the chosen cell as an endpoint.
 
Constraints:
    1. board.length == board[r].length == 8
    2. 0 <= rMove, cMove < 8
    3. board[rMove][cMove] == '.'
    4. color is either 'B' or 'W'.
'''
# === 128ms && 14.3MB === #
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1,1), (-1,-1)]
        for dx, dy in delta:
            r, c = rMove + dx, cMove + dy
            if not 0 <= r < 8 or not 0 <= c < 8:
                continue
            pad = "B" if color == "W" else "W"
            if board[r][c] != pad:
                continue
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == pad:
                r += dx
                c += dy
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == color:
                return True
        return False
        