'''
=== 1871. Jump Game VII ===

You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:
    - i + minJump <= j <= min(i + maxJump, s.length - 1), and
    - s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

Example 1:
    Input: s = "011010", minJump = 2, maxJump = 3
    Output: true
    Explanation:
    In the first step, move from index 0 to index 3. 
    In the second step, move from index 3 to index 5.
Example 2:
    Input: s = "01101110", minJump = 2, maxJump = 3
    Output: false
    
Constraints:
    1. 2 <= s.length <= 105
    2. s[i] is either '0' or '1'.
    3. s[0] == '0'
    4. 1 <= minJump <= maxJump < s.length
'''
# === 400ms && 15.9MB === #
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False
        
        dp = [0 for i in range(n)]
        dp[-1] = 1
        cnt = 0
        for i in range(n-1-minJump, -1, -1):
            cnt += dp[i+minJump]
            if i + maxJump + 1 < n:
                cnt -= dp[i + maxJump + 1]
            if s[i] == '0' and cnt > 0:
                dp[i] = 1
        print(dp)
            
        
        return dp[0] == 1