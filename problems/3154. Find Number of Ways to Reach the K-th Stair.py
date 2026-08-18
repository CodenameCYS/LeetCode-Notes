'''
=== 3154. Find Number of Ways to Reach the K-th Stair ===

You are given a non-negative integer k. There exists a staircase with an infinite number of stairs, with the lowest stair numbered 0.
Alice has an integer jump, with an initial value of 0. She starts on stair 1 and wants to reach stair k using any number of operations. If she is on stair i, in one operation she can:
    - Go down to stair i - 1. This operation cannot be used consecutively or on stair 0.
    - Go up to stair i + 2jump. And then, jump becomes jump + 1.
Return the total number of ways Alice can reach stair k.
Note that it is possible that Alice reaches the stair k, and performs some operations to reach the stair k again.

Example 1:
    Input: k = 0
    Output: 2
    Explanation:
    The 2 possible ways of reaching stair 0 are:
    Alice starts at stair 1.
    - Using an operation of the first type, she goes down 1 stair to reach stair 0.
    Alice starts at stair 1.
    - Using an operation of the first type, she goes down 1 stair to reach stair 0.
    - Using an operation of the second type, she goes up 20 stairs to reach stair 1.
    - Using an operation of the first type, she goes down 1 stair to reach stair 0.
Example 2:
    Input: k = 1
    Output: 4
    Explanation:
    The 4 possible ways of reaching stair 1 are:
    Alice starts at stair 1. Alice is at stair 1.
    Alice starts at stair 1.
    - Using an operation of the first type, she goes down 1 stair to reach stair 0.
    - Using an operation of the second type, she goes up 20 stairs to reach stair 1.
    Alice starts at stair 1.
    - Using an operation of the second type, she goes up 20 stairs to reach stair 2.
    - Using an operation of the first type, she goes down 1 stair to reach stair 1.
    Alice starts at stair 1.
    - Using an operation of the first type, she goes down 1 stair to reach stair 0.
    - Using an operation of the second type, she goes up 20 stairs to reach stair 1.
    - Using an operation of the first type, she goes down 1 stair to reach stair 0.
    - Using an operation of the second type, she goes up 21 stairs to reach stair 2.
    - Using an operation of the first type, she goes down 1 stair to reach stair 1.
 

Constraints:
    1. 0 <= k <= 109
'''
# === 116ms && 18.4MB === #
class Solution:
    def waysToReachStair(self, k: int) -> int:
        # ans = 0
        
        @lru_cache(None)
        def dp(loc, jump, allow_op1):
            ans = 0
            if loc == k:
                ans += 1
            if allow_op1 and loc != 0:
                ans += dp(loc-1, jump, False)
            if loc + jump <= k+1:
                ans += dp(loc+jump, jump * 2, True)
            return ans
        
        ans = dp(1, 1, True)
        return ans
            