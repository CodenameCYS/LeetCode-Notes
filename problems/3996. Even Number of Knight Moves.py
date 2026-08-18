'''
=== 3996. Even Number of Knight Moves ===

You are given two integer arrays start and target, where each array is of the form [x, y] representing a cell on a standard 8 x 8 chessboard.
Return true if a knight can move from start to target in an even number of moves. Otherwise, return false.
Note: A valid knight move consists of moving two squares in one direction and one square perpendicular to it. The figure below illustrates all eight possible moves from a cell.

Example 1:
    Input: start = [1,1], target = [2,2]
    Output: true
    Explanation:
    One possible sequence of moves is (1, 1) -> (3, 2) -> (2, 4) -> (4, 3) -> (2, 2).
    The knight reaches the target in 4 moves, which is even. Thus, the answer is true.
Example 2:
    Input: start = [4,5], target = [6,6]
    Output: false
    Explanation:​​​​​​​
    It is impossible to reach target = [6, 6] from start = [4, 5] in an even number of moves. Thus, the answer is false.

Constraints:
    1. start.length == target.length == 2
    2. 0 <= start[i], target[i] <= 7
'''
# === 0ms && 19.12MB === #
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        dx, dy = abs(start[0] - target[0]), abs(start[1] - target[1])
        return dx % 2 == dy % 2