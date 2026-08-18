'''
=== 1926. Nearest Exit from Entrance in Maze ===

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:
    Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
    Output: 1
    Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
    Initially, you are at the entrance cell [1,2].
    - You can reach [1,0] by moving 2 steps left.
    - You can reach [0,2] by moving 1 step up.
    It is impossible to reach [2,3] from the entrance.
    Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:
    Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
    Output: 2
    Explanation: There is 1 exit in this maze at [1,2].
    [1,0] does not count as an exit since it is the entrance cell.
    Initially, you are at the entrance cell [1,0].
    - You can reach [1,2] by moving 2 steps right.
    Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:
    Input: maze = [[".","+"]], entrance = [0,0]
    Output: -1
    Explanation: There are no exits in this maze.

Constraints:
    1. maze.length == m
    2. maze[i].length == n
    3. 1 <= m, n <= 100
    4. maze[i][j] is either '.' or '+'.
    5. entrance.length == 2
    6. 0 <= entrancerow < m
    7. 0 <= entrancecol < n
    8. entrance will always be an empty cell.
'''
# === 968ms && 15.9MB === #
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        seen = {tuple(entrance)}
        q = [[entrance[0], entrance[1], 0]]
        # for line in maze:
        #     print(" ".join(line))
        while q:
            # print(q)
            x, y, s = q.pop(0)
            if s != 0 and (x == n-1 or y == m-1 or x == 0 or y == 0):
                return s
            if x-1 >= 0 and (x-1, y) not in seen and maze[x-1][y] == ".":
                q.append((x-1, y, s+1))
                seen.add((x-1, y))
            if x+1 < n and (x+1, y) not in seen and maze[x+1][y] == ".":
                q.append((x+1, y, s+1))
                seen.add((x+1, y))
            if y-1 >= 0 and (x, y-1) not in seen and maze[x][y-1] == ".":
                q.append((x, y-1, s+1))
                seen.add((x, y-1))
            if y+1 < m and (x, y+1) not in seen and maze[x][y+1] == ".":
                q.append((x, y+1, s+1))
                seen.add((x, y+1))
        return -1
            
        