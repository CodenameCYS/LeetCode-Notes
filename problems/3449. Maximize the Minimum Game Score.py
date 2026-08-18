'''
=== 3449. Maximize the Minimum Game Score ===

You are given an array points of size n and an integer m. There is another array gameScore of size n, where gameScore[i] represents the score achieved at the ith game. Initially, gameScore[i] == 0 for all i.
You start at index -1, which is outside the array (before the first position at index 0). You can make at most m moves. In each move, you can either:
    - Increase the index by 1 and add points[i] to gameScore[i].
    - Decrease the index by 1 and add points[i] to gameScore[i].
Note that the index must always remain within the bounds of the array after the first move.
Return the maximum possible minimum value in gameScore after at most m moves.

Example 1:
    Input: points = [2,4], m = 3
    Output: 4
    Explanation:
    Initially, index i = -1 and gameScore = [0, 0].
    Move	Index	gameScore
    Increase i	0	[2, 0]
    Increase i	1	[2, 4]
    Decrease i	0	[4, 4]
    The minimum value in gameScore is 4, and this is the maximum possible minimum among all configurations. Hence, 4 is the output.
Example 2:
    Input: points = [1,2,3], m = 5
    Output: 2
    Explanation:
    Initially, index i = -1 and gameScore = [0, 0, 0].
    Move	Index	gameScore
    Increase i	0	[1, 0, 0]
    Increase i	1	[1, 2, 0]
    Decrease i	0	[2, 2, 0]
    Increase i	1	[2, 4, 0]
    Increase i	2	[2, 4, 3]
    The minimum value in gameScore is 2, and this is the maximum possible minimum among all configurations. Hence, 2 is the output.

Constraints:
    1. 2 <= n == points.length <= 5 * 104
    2. 1 <= points[i] <= 106
    3. 1 <= m <= 109
'''
# === 3534ms && 24.1MB === #
class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        
        def is_possible(score):
            cnt = 0
            debt = 0
            for i, p in enumerate(points[:-1]):
                need = ceil(score / p)
                if debt >= need:
                    cnt += debt+1
                    debt = 0
                else:
                    cnt += need
                    debt = need-debt-1
                if cnt > m:
                    return False
            if cnt + debt > m:
                return False
            
            allow = debt + (m-cnt-debt+1)//2
            return allow * points[-1] >= score
        
        l, r = 0, max(points) * ((m+1) // 2) + 1
        # print(f"left bound = {l}, right bound = {r}")
        while r-l>1:
            k = (l+r) // 2
            flag = is_possible(k)
            # print(f"score = {k}, is possible = {flag}")
            if flag:
                l = k
            else:
                r = k
        # print("=" * 10)
        return l
        
        