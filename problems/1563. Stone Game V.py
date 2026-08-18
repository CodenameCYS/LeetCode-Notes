'''
=== 1563. Stone Game V ===

There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.
The game ends when there is only one stone remaining. Alice's is initially zero.
Return the maximum score that Alice can obtain.

Example 1:
    Input: stoneValue = [6,2,3,4,5,5]
    Output: 18
    Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
    In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
    The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.
Example 2:
    Input: stoneValue = [7,7,7,7,7,7,7]
    Output: 28
Example 3:
    Input: stoneValue = [4]
    Output: 0
 
Constraints:
    1. 1 <= stoneValue.length <= 500
    2. 1 <= stoneValue[i] <= 10^6
'''
# === 5252ms && 39MB === #
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        cumsum = [0 for i in range(n + 1)]
        for i, v in enumerate(stoneValue):
            cumsum[i+1] = cumsum[i] + stoneValue[i]
        # print(cumsum)
        
        @lru_cache(None)
        def dp(st, ed):
            nonlocal cumsum
            if ed - st == 1:
                return 0
            ans = 0
            for i in range(st+1, ed):
                if cumsum[i] - cumsum[st] < cumsum[ed] - cumsum[i]:
                    ans = max(ans, cumsum[i] - cumsum[st] + dp(st, i))
                elif cumsum[i] - cumsum[st] > cumsum[ed] - cumsum[i]:
                    ans = max(ans, cumsum[ed] - cumsum[i] + dp(i, ed))
                else:
                    ans = max(ans, cumsum[i] - cumsum[st] + dp(st, i), cumsum[ed] - cumsum[i] + dp(i, ed))
            return ans
        
        return dp(0, n)