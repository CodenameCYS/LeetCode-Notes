'''
=== 473. Matchsticks to Square ===

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.

Example 1:
    Input: matchsticks = [1,1,2,2,2]
    Output: true
    Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
    Input: matchsticks = [3,3,3,3,4]
    Output: false
    Explanation: You cannot find a way to form a square with all the matchsticks.
 
Constraints:
    1. 1 <= matchsticks.length <= 15
    2. 0 <= matchsticks[i] <= 109
'''
# === 156ms(69.97%) && 16.7MB(11.80%) === #
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks = sorted(matchsticks)
        n, s = len(matchsticks), sum(matchsticks)
        if s % 4 != 0 or matchsticks[-1] > s // 4:
            return False
        s1, s2, s3, s4 = s//4, s//2, s//4*3, s
        
        @lru_cache(None)
        def dp(ss, status):
            if ss < s1:
                target = s1
            elif ss < s2:
                target = s2
            elif ss < s3:
                target = s3
            elif ss < s4:
                target = s4
            else:
                return True
            res = False
            for i in range(n):
                if not status & (1 << i) and ss+matchsticks[i] <= target:
                    res = res or dp(ss+matchsticks[i], status | (1<<i))
            return res
        
        return dp(0, 0)
            