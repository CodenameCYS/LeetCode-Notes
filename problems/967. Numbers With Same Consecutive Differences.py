'''
=== 967. Numbers With Same Consecutive Differences ===

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.
Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.
You may return the answer in any order.

Example 1:
    Input: N = 3, K = 7
    Output: [181,292,707,818,929]
    Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:
    Input: N = 2, K = 1
    Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 
Note:
    1. 1 <= N <= 9
    2. 0 <= K <= 9
'''
# === 32ms(97.21%) && 14MB(71.63%) === #
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1:
            return [i for i in range(10)]
        if K == 0:
            return [str(i) * N for i in range(1, 10)]
        
        def dp(i, n, his):
            nonlocal ans
            if n == 0:
                ans.append(his)
                return
            if i + K <= 9:
                dp(i+K, n-1, his + str(i+K))
            if i - K >= 0:
                dp(i-K, n-1, his + str(i-K))
            return
        
        ans = []
        for i in range(1, 10):
            dp(i, N-1, str(i))
        return ans