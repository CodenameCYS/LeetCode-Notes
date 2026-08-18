'''
=== 1861. Rotating the Box ===

You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:
    - A stone '#'
    - A stationary obstacle '*'
    - Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.
Return an n x m matrix representing the box after the rotation described above.

Example 1:
    Input: box = [["#",".","#"]]
    Output: [["."],
             ["#"],
             ["#"]]
Example 2:
    Input: box = [["#",".","*","."],
                  ["#","#","*","."]]
    Output: [["#","."],
             ["#","#"],
             ["*","*"],
             [".","."]]
Example 3:
    Input: box = [["#","#","*",".","*","."],
                  ["#","#","#","*",".","."],
                  ["#","#","#",".","#","."]]
    Output: [[".","#","#"],
             [".","#","#"],
             ["#","#","*"],
             ["#","*","."],
             ["#",".","*"],
             ["#",".","."]]
 
Constraints:
    1. m == box.length
    2. n == box[i].length
    3. 1 <= m, n <= 500
    4. box[i][j] is either '#', '*', or '.'.
'''
# === 2456ms && 30.3MB === #
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])
        counter = [[] for _ in range(n)]
        res = [["." for _ in range(n)] for _ in range(m)]
        for i in range(n):
            cnt = 0
            for j in range(m):
                if box[i][j] == "#":
                    cnt += 1
                elif box[i][j] == "*":
                    res[j][n-1-i] = "*"
                    counter[i].append((cnt, j))
                    cnt = 0
            counter[i].append((cnt, m))
        
        for i in range(n):
            for cnt, j in counter[i]:
                for k in range(j-cnt, j):
                    res[k][n-1-i] = "#"
        return res