'''
=== 688. Knight Probability in Chessboard ===

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:
    Input: 3, 2, 0, 0
    Output: 0.0625
    Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
    From each of those positions, there are also two moves that will keep the knight on the board.
    The total probability the knight stays on the board is 0.0625.
    
Note:
    1. N will be between 1 and 25.
    2. K will be between 0 and 100.
    3. The knight always initially starts on the board.
'''
# === 420ms(5.93%) && 21MB(53.85%) === #
class Solution:
    cache = {}
    
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1
        if (N,K,r,c) in self.cache.keys():
            return self.cache[(N,K,r,c)]
        p = 0
        if r+2>=0 and r+2<N and c+1>=0 and c+1<N:
            p += 1/8 * self.knightProbability(N, K-1, r+2, c+1)
        if r+2>=0 and r+2<N and c-1>=0 and c-1<N:
            p += 1/8 * self.knightProbability(N, K-1, r+2, c-1)
        if r-2>=0 and r-2<N and c+1>=0 and c+1<N:
            p += 1/8 * self.knightProbability(N, K-1, r-2, c+1)
        if r-2>=0 and r-2<N and c-1>=0 and c-1<N:
            p += 1/8 * self.knightProbability(N, K-1, r-2, c-1)
        if r+1>=0 and r+1<N and c+2>=0 and c+2<N:
            p += 1/8 * self.knightProbability(N, K-1, r+1, c+2)
        if r+1>=0 and r+1<N and c-2>=0 and c-2<N:
            p += 1/8 * self.knightProbability(N, K-1, r+1, c-2)
        if r-1>=0 and r-1<N and c+2>=0 and c+2<N:
            p += 1/8 * self.knightProbability(N, K-1, r-1, c+2)
        if r-1>=0 and r-1<N and c-2>=0 and c-2<N:
            p += 1/8 * self.knightProbability(N, K-1, r-1, c-2)
        self.cache[(N,K,r,c)] = p
        return p