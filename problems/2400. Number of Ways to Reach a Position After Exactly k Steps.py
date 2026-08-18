'''
=== 2400. Number of Ways to Reach a Position After Exactly k Steps ===

You are given two positive integers startPos and endPos. Initially, you are standing at position startPos on an infinite number line. With one step, you can move either one position to the left, or one position to the right.
Given a positive integer k, return the number of different ways to reach the position endPos starting from startPos, such that you perform exactly k steps. Since the answer may be very large, return it modulo 109 + 7.
Two ways are considered different if the order of the steps made is not exactly the same.
Note that the number line includes negative integers.

Example 1:
    Input: startPos = 1, endPos = 2, k = 3
    Output: 3
    Explanation: We can reach position 2 from 1 in exactly 3 steps in three ways:
    - 1 -> 2 -> 3 -> 2.
    - 1 -> 2 -> 1 -> 2.
    - 1 -> 0 -> 1 -> 2.
    It can be proven that no other way is possible, so we return 3.
Example 2:
    Input: startPos = 2, endPos = 5, k = 10
    Output: 0
    Explanation: It is impossible to reach position 5 from position 2 in exactly 10 steps.
 
Constraints:
    1. 1 <= startPos, endPos, k <= 1000
'''
# === 2553ms && 302.8MB === #
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9+7
        
        @lru_cache(None)
        def dp(st, ed, k):
            if abs(ed-st) > k:
                return 0
            elif abs(ed-st) == k:
                return 1
            return (dp(st+1, ed, k-1) + dp(st-1, ed, k-1)) % MOD
        
        return dp(startPos, endPos, k)

# === 58ms && 15.2MB === #
class Solution:
    @lru_cache(None)
    def Cnm(self, n, k):
        MOD = 10**9 + 7
        if k == 0 or k == n:
            return 1
        return self.Cnm(n-1, k) * n * pow(n-k, -1, MOD) % MOD
    
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        d = endPos - startPos
        if d % 2 != k % 2 or abs(d) > k:
            return 0
        r = (k - d) // 2
        l = k - r
        return self.Cnm(k, r)
                
                