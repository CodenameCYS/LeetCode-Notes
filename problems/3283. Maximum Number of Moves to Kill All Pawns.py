'''
=== 3283. Maximum Number of Moves to Kill All Pawns ===

There is a 50 x 50 chessboard with one knight and some pawns on it. You are given two integers kx and ky where (kx, ky) denotes the position of the knight, and a 2D array positions where positions[i] = [xi, yi] denotes the position of the pawns on the chessboard.
Alice and Bob play a turn-based game, where Alice goes first. In each player's turn:
    - The player selects a pawn that still exists on the board and captures it with the knight in the fewest possible moves. Note that the player can select any pawn, it might not be one that can be captured in the least number of moves.
    - In the process of capturing the selected pawn, the knight may pass other pawns without capturing them. Only the selected pawn can be captured in this turn.
Alice is trying to maximize the sum of the number of moves made by both players until there are no more pawns on the board, whereas Bob tries to minimize them.
Return the maximum total number of moves made during the game that Alice can achieve, assuming both players play optimally.
Note that in one move, a chess knight has eight possible positions it can move to, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.

Example 1:
    Input: kx = 1, ky = 1, positions = [[0,0]]
    Output: 4
    Explanation:
    The knight takes 4 moves to reach the pawn at (0, 0).
Example 2:
    Input: kx = 0, ky = 2, positions = [[1,1],[2,2],[3,3]]
    Output: 8
    Explanation:
    Alice picks the pawn at (2, 2) and captures it in two moves: (0, 2) -> (1, 4) -> (2, 2).
    Bob picks the pawn at (3, 3) and captures it in two moves: (2, 2) -> (4, 1) -> (3, 3).
    Alice picks the pawn at (1, 1) and captures it in four moves: (3, 3) -> (4, 1) -> (2, 2) -> (0, 3) -> (1, 1).
Example 3:
    Input: kx = 0, ky = 0, positions = [[1,2],[2,4]]
    Output: 3
    Explanation:
    Alice picks the pawn at (2, 4) and captures it in two moves: (0, 0) -> (1, 2) -> (2, 4). Note that the pawn at (1, 2) is not captured.
    Bob picks the pawn at (1, 2) and captures it in one move: (2, 4) -> (1, 2).
 
Constraints:
    1. 0 <= kx, ky <= 49
    2. 1 <= positions.length <= 15
    3. positions[i].length == 2
    4. 0 <= positions[i][0], positions[i][1] <= 49
    5. All positions[i] are unique.
    6. The input is generated such that positions[i] != [kx, ky] for all 0 <= i < positions.length.
'''
# === 11035ms && 119MB === #
@lru_cache(None)
def move(x0, y0, x1, y1):
    dirs = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    if abs(x0-x1) == 2 * abs(y0-y1):
        return abs(y0-y1)
    if abs(y0-y1) == 2 * abs(x0-x1):
        return abs(x0-x1)
    q = [(0, abs(x0-x1) + abs(y0-y1), x0, y0)]
    seen = {(x0, y0)}
    while q:
        step, _, x, y = heapq.heappop(q)
        for dx, dy in dirs:
            if x + dx == x1 and y+dy == y1:
                return step+1
            if 0 <= x+dx < 50 and 0 <= y+dy < 50 and (x+dx, y+dy) not in seen:
                seen.add((x+dx, y+dy))
                heapq.heappush(q, (step+1, abs(x+dx-x1) + abs(y+dy-y1), x+dx, y+dy))
    return math.inf

class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        # print(move(0, 6, 9, 3))
        n = len(positions)
        END = 2**n-1
        
        @lru_cache(None)
        def dp_alice(x, y, status):
            if status == END:
                return 0
            ans = 0
            for i in range(n):
                if status & (1 << i) != 0:
                    continue
                x1, y1 = positions[i][0], positions[i][1]
                ans = max(ans, move(x, y, x1, y1) + dp_bob(x1, y1, status | (1 << i)))
            return ans
            
        @lru_cache(None)
        def dp_bob(x, y, status):
            if status == END:
                return 0
            ans = math.inf
            for i in range(n):
                if status & (1 << i) != 0:
                    continue
                x1, y1 = positions[i][0], positions[i][1]
                ans = min(ans, move(x, y, x1, y1) + dp_alice(x1, y1, status | (1 << i)))
            return ans
        
        return dp_alice(kx, ky, 0)