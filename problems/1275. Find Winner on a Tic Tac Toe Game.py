'''
=== 1275. Find Winner on a Tic Tac Toe Game ===

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.
Here are the rules of Tic-Tac-Toe:
    - Players take turns placing characters into empty squares (" ").
    - The first player A always places "X" characters, while the second player B always places "O" characters.
    - "X" and "O" characters are always placed into empty squares, never on filled ones.
    - The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
    - The game also ends if all squares are non-empty.
    - No more moves can be played if the game is over.
    - Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.
Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".
You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

Example 1:
    Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    Output: "A"
    - Explanation: "A" wins, he always plays first.
    "X  "    "X  "    "X  "    "X  "    "X  "
    "   " -> "   " -> " X " -> " X " -> " X "
    "   "    "O  "    "O  "    "OO "    "OOX"
Example 2:
    Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    Output: "B"
    - Explanation: "B" wins.
    "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
    "   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
    "   "    "   "    "   "    "   "    "   "    "O  "
Example 3:
    Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    Output: "Draw"
    - Explanation: The game ends in a draw since there are no moves to make.
    "XXO"
    "OOX"
    "XOX"
Example 4:
    Input: moves = [[0,0],[1,1]]
    Output: "Pending"
    - Explanation: The game has not finished yet.
    "X  "
    " O "
    "   "

Constraints:
    1. 1 <= moves.length <= 9
    2. moves[i].length == 2
    3. 0 <= moves[i][j] <= 2
    4. There are no repeated elements on moves.
    5. moves follow the rules of tic tac toe.
'''
# === 24ms & 12.7MB === #
class Solution:
    def is_won(self, moves: List[int]) -> bool:
        winning_set = [{0,1,2}, {3,4,5}, {6,7,8}, {0,3,6}, {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}]
        for it in winning_set:
            if it.issubset(moves):
                return True
        return False
    
    def tictactoe(self, moves: List[List[int]]) -> str:
        A = set()
        B = set()
        for i, it in enumerate(moves):
            if i%2 == 0:
                A.add(3*it[0] + it[1])
            else:
                B.add(3*it[0] + it[1])
        if self.is_won(A):
            return "A"
        elif self.is_won(B):
            return "B"
        elif len(moves) == 9:
            return "Draw"
        else:
            return "Pending"