'''
=== 4061. Minimum Queen Moves to Reach Target ===

There is an 8 x 8 empty chessboard with 1-indexed rows and columns.
You are given an array source = [sr, sc] representing the starting position of a queen, and an array target = [tr, tc] representing the target position.
In one move, the queen travels one or more squares along a single row, column, or diagonal, staying within the board.
Return the minimum number of moves for the queen to land exactly on target.

Example 1:
    Input: source = [8,1], target = [1,8]
    Output: 1
    Explanation:
    A single diagonal move takes the queen straight from (8, 1) to (1, 8).
Example 2:
    Input: source = [4,2], target = [1,3]
    Output: 2
    Explanation:
    The queen moves from (4, 2) to (4, 3), then from (4, 3) to (1, 3), reaching the target in 2 moves.
Example 3:
    Input: source = [1,1], target = [1,1]
    Output: 0
    Explanation:
    The queen is already at the target position, so no moves are needed.

Constraints:​​​​​​​
    1. source == [sr, sc]
    2. target == [tr, tc]
    3. 1 <= sr, sc, tr, tc <= 8
'''
# === 0ms && 19.08MB === #
class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        x1, y1 = source
        x2, y2 = target
        if x1 == x2 and y1 == y2:
            return 0
        if x1 == x2 or y1 == y2 or abs(x1-x2) == abs(y1-y2):
            return 1
        return 2