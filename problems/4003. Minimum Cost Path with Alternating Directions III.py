'''
=== 4003. Minimum Cost Path with Alternating Directions III ===

You are given two integers m and n representing the number of rows and columns of a grid. Your goal is to reach cell (m - 1, n - 1). You are also given a 2D integer array penalty.
The cost to enter cell (i, j) is (i + 1) * (j + 1).
You begin at cell (0, 0) and initially pay its entrance cost. Actions performed after entering (0, 0) are numbered starting from 1.
On each action, you may move to an adjacent cell or wait in the current cell. A move follows the parity rule if:
    - On an odd-numbered action, you move right or down.
    - On an even-numbered action, you move left or up.
The cost of an action is determined as follows:
    - If you move according to the parity rule, pay only the entrance cost of the destination cell.
    - If you move in a direction that violates the parity rule, pay the entrance cost of the destination cell plus penalty[i][j], where (i, j) is the cell you move from.
    - If you wait in cell (i, j), pay penalty[i][j].
After every move or wait, the action number increases by 1. Therefore, the required parity alternates after every action, regardless of whether a penalty was paid.
Return the minimum total cost required to reach (m - 1, n - 1).

Example 1:
    Input: m = 2, n = 2, penalty = [[5,3],[1,4]]
    Output: 8
    Explanation:
    The optimal path is:
    Start at cell (0, 0) with entry cost (0 + 1) * (0 + 1) = 1.
    Move 1: Move down to cell (1, 0) with entry cost (1 + 1) * (0 + 1) = 2.
    Move 2: Move right to cell (1, 1) with entry cost (1 + 1) * (1 + 1) = 4 and an extra cost of penalty[1][0] = 1 for violating the even parity rule.
    Thus, the total cost is 1 + 2 + 4 + 1 = 8.
Example 2:
    Input: m = 2, n = 2, penalty = [[0,7],[3,2]]
    Output: 7
    Explanation:
    The optimal path is:
    Start at cell (0, 0) with entry cost (0 + 1) * (0 + 1) = 1.
    Move 1: Wait at cell (0, 0) with an extra cost of penalty[0][0] = 0 to flip to even parity.
    Move 2: Move right to cell (0, 1) with entry cost (0 + 1) * (1 + 1) = 2 and an extra cost of penalty[0][0] = 0 for violating the even parity rule.
    Move 3: Move down to cell (1, 1) with entry cost (1 + 1) * (1 + 1) = 4.
    Thus, the total cost is 1 + 0 + 2 + 0 + 4 = 7.
Example 3:
    Input: m = 2, n = 3, penalty = [[8,0,9],[7,4,1]]
    Output: 12
    Explanation:
    The optimal path is:
    Start at cell (0, 0) with entry cost (0 + 1) * (0 + 1) = 1.
    Move 1: Move right to cell (0, 1) with entry cost (0 + 1) * (1 + 1) = 2.
    Move 2: Move right to cell (0, 2) with entry cost (0 + 1) * (2 + 1) = 3 and an extra cost of penalty[0][1] = 0 for violating the even parity rule.
    Move 3: Move down to cell (1, 2) with entry cost (1 + 1) * (2 + 1) = 6.
    Thus, the total cost is 1 + 2 + 3 + 0 + 6 = 12.

Constraints:
    1. 1 <= m, n <= 105
    2. 2 <= m * n <= 105
    3. penalty.length == m
    4. penalty[i].length == n
    5. 0 <= penalty[i][j] <= 105
'''
# === 3898ms && 76.18MB === #
class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        q = [(1, 0, 0, 1)]
        seen = set()
        while q:
            cost, i, j, t = heapq.heappop(q)
            i, j = -i, -j
            if (i, j, t) in seen:
                continue
            seen.add((i, j, t))
            if i == m-1 and j == n-1:
                return cost
            nt, p = (t+1)%2, penalty[i][j]
            heapq.heappush(q, (cost+p, -i, -j, nt))
            if t == 1:
                if i+1 < m and (i+1, j, nt) not in seen:
                    heapq.heappush(q, (cost + (i+2)*(j+1), -i-1, -j, nt))
                if j+1 < n and (i, j+1, nt) not in seen:
                    heapq.heappush(q, (cost + (i+1)*(j+2), -i, -j-1, nt))
                if i-1 >= 0 and (i-1, j, nt) not in seen:
                    heapq.heappush(q, (cost + i*(j+1) + p, -i+1, -j, nt))
                if j-1 >= 0 and (i, j-1, nt) not in seen:
                    heapq.heappush(q, (cost + (i+1)*j + p, -i, -j+1, nt))
            else:
                if i+1 < m and (i+1, j, nt) not in seen:
                    heapq.heappush(q, (cost + (i+2)*(j+1) + p, -i-1, -j, nt))
                if j+1 < n and (i, j+1, nt) not in seen:
                    heapq.heappush(q, (cost + (i+1)*(j+2) + p, -i, -j-1, nt))
                if i-1 >= 0 and (i-1, j, nt) not in seen:
                    heapq.heappush(q, (cost + i*(j+1), -i+1, -j, nt))
                if j-1 >= 0 and (i, j-1, nt) not in seen:
                    heapq.heappush(q, (cost + (i+1)*j, -i, -j+1, nt))
        return -1

