'''
=== 4050. Minimum Days to Score Exactly N Points ===

You are given an integer n representing a target score.
Your score starts at 0, and each day you either earn points or skip.
Points are earned during a streak. On the first day of a streak you earn 1 point, on the second day 2 points, on the third day 3 points, and so on. Skipping a day earns nothing and resets the streak, so the next time you earn points, you start from 1 again.
Return the minimum number of days, including any skipped days, needed to reach a score of exactly n.

Example 1:
    Input: n = 2
    Output: 3
    Explanation:​​​​​​​
    Day 1: earn 1 point. Score is 1.
    Day 2: skip, which resets the streak. Earning here would add 2 points and take the score past n = 2.
    Day 3: the streak has reset, so earning gives 1 point. Score is exactly n = 2 in 3 days.
Example 2:
    Input: n = 9
    Output: 6
    Explanation:​​​​​​​
    Days 1 to 3: earn 1, 2, and 3 points. Score is 1 + 2 + 3 = 6.
    Day 4: skip, which resets the streak.
    Days 5 and 6: earn 1 and 2 points. Score is exactly 6 + 1 + 2 = 9 in 6 days.
Example 3:
    Input: n = 12
    Output: 7
    Explanation:​​​​​​​
    Days 1 to 3: earn 1, 2, and 3 points. Score is 1 + 2 + 3 = 6.
    Day 4: skip, which resets the streak.
    Days 5 to 7: earn 1, 2, and 3 points. Score is exactly 6 + 1 + 2 + 3 = 12 in 7 days.
 
Constraints:
    1. 1 <= n <= 105
'''
# === 15616ms && 46.63MB === #
class Solution:
    def minDays(self, n: int) -> int:
        q = [(0, 0)]
        seen = {0:0}
        while q:
            t, score = heapq.heappop(q)
            score = -score
            if score == n:
                return t
            gap = 0 if t == 0 else 1
            for k in range(1, 450):
                gain = k*(k+1)//2
                if gain + score > n:
                    break
                if t+gap+k < seen.get(score+gain, math.inf):
                    seen[score+gain] = t+gap+k
                    heapq.heappush(q, (t+gap+k, -score-gain))
        return -1
# === 0ms && 22.7MB === # 
MX = 100_001
f = [inf] * MX
f[0] = -1

s = i = 1
while s < MX:
    for j in range(s, MX):
        f[j] = min(f[j], f[j - s] + i + 1)
    i += 1
    s += i

class Solution:
    def minDays(self, n: int) -> int:
        return f[n]