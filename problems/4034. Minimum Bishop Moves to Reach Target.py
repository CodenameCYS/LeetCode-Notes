'''
=== 4034. Minimum Bishop Moves to Reach Target ===

There is an 8 x 8 empty chessboard with 1-indexed rows and columns.
You are given an array source = [sr, sc] representing the starting position of a bishop, and an array target = [tr, tc]. In one move, the bishop travels any number of squares along a single diagonal direction, staying within the board.
Return the minimum number of moves for the bishop to land exactly on target. If it can never reach target, return -1.

Example 1:
    Input: source = [8,1], target = [1,8]
    Output: 1
    Explanation:
    A single diagonal move takes the bishop straight from (8, 1) to (1, 8).
Example 2:
    Input: source = [4,2], target = [1,3]
    Output: 2
    Explanation:
    The bishop moves from (4, 2) to (3, 1), then from (3, 1) to (1, 3), reaching the target in 2 moves.
Example 3:
    Input: source = [1,1], target = [3,4]
    Output: -1
    Explanation:
    No matter how many diagonal moves it makes, the bishop starting at (1, 1) can never land on (3, 4). Thus, the answer is -1.

Constraints:​​​​​​​
    1. source.length == target.length == 2
    2.  1 <= sr, sc, tr, tc <= 8
    3. source != target
'''
# === 0ms && 19.32MB === #
class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        x0, y0 = source
        x1, y1 = target
        if (x0 + y0) % 2 != (x1 + y1) % 2:
            return -1
        elif x0 + y0 == x1 + y1 or x0-y0 == x1-y1:
            return 1
        else:
            return 2