'''
=== 2018. Check if Word Can Be Placed In Crossword ===

You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.
A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:
    - It does not occupy a cell containing the character '#'.
    - The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
    - There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
    - There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
Given a string word, return true if word can be placed in board, or false otherwise.

Example 1:
    Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
    Output: true
    Explanation: The word "abc" can be placed as shown above (top to bottom).
Example 2:
    Input: board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
    Output: false
    Explanation: It is impossible to place the word because there will always be a space/letter above or below it.
Example 3:
    Input: board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
    Output: true
    Explanation: The word "ca" can be placed as shown above (right to left). 
 
Constraints:
    1. m == board.length
    2. n == board[i].length
    3. 1 <= m * n <= 2 * 105
    4. board[i][j] will be ' ', '#', or a lowercase English letter.
    5. 1 <= word.length <= max(m, n)
    6. word will contain only lowercase English letters.
'''
# === 1272ms && 26.1MB === #
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        n, m, l = len(board), len(board[0]), len(word)
        
        def check_horizon(idx):
            # check forward
            j, match = 0, True # init
            for i in range(m):
                if board[idx][i] == "#":
                    if j == l and match:
                        return True
                    j, match = 0, True # init
                    if m-i-1 < l:
                        break
                    continue
                if j >= l:
                    match = False
                elif board[idx][i] != " " and board[idx][i] != word[j]:
                    match = False
                j += 1
            if j == l and match:
                return True
            
            # check backward
            j, match = 0, True # initj = 0
            for i in range(m-1, -1, -1):
                if board[idx][i] == "#":
                    if j == l and match:
                        return True
                    j, match = 0, True # init
                    if i < l:
                        break
                    continue
                if j >= l:
                    match = False
                elif board[idx][i] != " " and board[idx][i] != word[j]:
                    match = False
                j += 1
            return j == l and match
        
        def check_vertical(idx):
            # check forward
            j, match = 0, True # init
            for i in range(n):
                if board[i][idx] == "#":
                    if j == l and match:
                        return True
                    j = 0
                    match = True
                    if n-i-1 < l:
                        break
                    continue
                if j >= l:
                    match = False
                elif board[i][idx] != " " and board[i][idx] != word[j]:
                    match = False
                j += 1
            if j == l and match:
                return True
            
            # check backward
            j, match = 0, True # init
            for i in range(n-1, -1, -1):
                if board[i][idx] == "#":
                    if j == l and match:
                        return True
                    j, match = 0, True # init
                    if i < l:
                        break
                    continue
                if j >= l:
                    match = False
                elif board[i][idx] != " " and board[i][idx] != word[j]:
                    match = False
                j += 1
            return j == l and match
        
        if l <= m:
            if any(check_horizon(i) for i in range(n)):
                return True
        if l <= n:
            if any(check_vertical(i) for i in range(m)):
                return True
        return False
            
        