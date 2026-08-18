'''
=== 3552. Grid Teleportation Traversal ===

You are given a 2D character grid matrix of size m x n, represented as an array of strings, where matrix[i][j] represents the cell at the intersection of the ith row and jth column. Each cell is one of the following:
    - '.' representing an empty cell.
    - '#' representing an obstacle.
    - An uppercase letter ('A'-'Z') representing a teleportation portal.
You start at the top-left cell (0, 0), and your goal is to reach the bottom-right cell (m - 1, n - 1). You can move from the current cell to any adjacent cell (up, down, left, right) as long as the destination cell is within the grid bounds and is not an obstacle.
If you step on a cell containing a portal letter and you haven't used that portal letter before, you may instantly teleport to any other cell in the grid with the same letter. This teleportation does not count as a move, but each portal letter can be used at most once during your journey.
Return the minimum number of moves required to reach the bottom-right cell. If it is not possible to reach the destination, return -1.

Example 1:
    Input: matrix = ["A..",".A.","..."]
    Output: 2
    Explanation:
    Before the first move, teleport from (0, 0) to (1, 1).
    In the first move, move from (1, 1) to (1, 2).
    In the second move, move from (1, 2) to (2, 2).
Example 2:
    Input: matrix = [".#...",".#.#.",".#.#.","...#."]
    Output: 13
    Explanation:

Constraints:
    1. 1 <= m == matrix.length <= 103
    2. 1 <= n == matrix[i].length <= 103
    3. matrix[i][j] is either '#', '.', or an uppercase English letter.
    4. matrix[0][0] is not an obstacle.
'''
# === 6943ms && 147.7MB === #
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        # print("=" * 10)
        n, m = len(matrix), len(matrix[0])
        teleportation = defaultdict(list)
        for i in range(n):
            for j in range(m):
                if matrix[i][j] in "#.":
                    continue
                teleportation[matrix[i][j]].append((i, j))
                
        seen = {(0, 0)}
        q = [(0, 0, 0, 0)]
        
        def add_teleportation(step, i, j, status):
            nonlocal seen, q
            if matrix[i][j] not in "#." and (status & (1 << (ord(matrix[i][j]) - ord('A'))) == 0):
                for ti, tj in teleportation[matrix[i][j]]:
                    if (ti, tj) not in seen:
                        heapq.heappush(q, (step, ti, tj, status | (1 << (ord(matrix[i][j]) - ord('A')))))
                        seen.add((ti, tj))
            return
        
        add_teleportation(0, 0, 0, 0)
        
        while q != []:
            step, i, j, status = heapq.heappop(q)
            if (i, j) == (n-1, m-1):
                return step
            if i+1 < n and (i+1, j) not in seen and matrix[i+1][j] != "#":
                heapq.heappush(q, (step+1, i+1, j, status))
                seen.add((i+1, j))
                add_teleportation(step+1, i+1, j, status)
            if j+1 < m and (i, j+1 ) not in seen and matrix[i][j+1] != "#":
                heapq.heappush(q, (step+1, i, j+1, status))
                seen.add((i, j+1))
                add_teleportation(step+1, i, j+1, status)
            if i-1 >= 0 and (i-1, j) not in seen and matrix[i-1][j] != "#":
                heapq.heappush(q, (step+1, i-1, j, status))
                seen.add((i-1, j))
                add_teleportation(step+1, i-1, j, status)
            if j-1 >= 0 and (i, j-1 ) not in seen and matrix[i][j-1] != "#":
                heapq.heappush(q, (step+1, i, j-1, status))
                seen.add((i, j-1))
                add_teleportation(step+1, i, j-1, status)
            # print(q, seen)
        return -1
                    