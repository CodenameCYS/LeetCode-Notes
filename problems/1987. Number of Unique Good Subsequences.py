'''
=== 1987. Number of Unique Good Subsequences ===

You are given a binary string binary. A subsequence of binary is considered good if it is not empty and has no leading zeros (with the exception of "0").
Find the number of unique good subsequences of binary.
    - For example, if binary = "001", then all the good subsequences are ["0", "0", "1"], so the unique good subsequences are "0" and "1". Note that subsequences "00", "01", and "001" are not good because they have leading zeros.
Return the number of unique good subsequences of binary. Since the answer may be very large, return it modulo 109 + 7.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
    Input: binary = "001"
    Output: 2
    Explanation: The good subsequences of binary are ["0", "0", "1"].
    The unique good subsequences are "0" and "1".
Example 2:
    Input: binary = "11"
    Output: 2
    Explanation: The good subsequences of binary are ["1", "1", "11"].
    The unique good subsequences are "1" and "11".
Example 3:
    Input: binary = "101"
    Output: 5
    Explanation: The good subsequences of binary are ["1", "0", "1", "10", "11", "101"]. 
    The unique good subsequences are "0", "1", "10", "11", and "101".
 
Constraints:
    1. 1 <= binary.length <= 105
    2. binary consists of only '0's and '1's.
'''
# === 216ms && 15.2MB === #
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9+7
        dp = [0, 0]
        for c in binary[::-1]:
            if c == "0":
                dp[0] = (dp[0] + dp[1] + 1) % MOD
            else:
                dp[1] = (dp[1] + dp[0] + 1) % MOD
        if '0' in binary:
            dp[1] = (dp[1] + 1) % MOD
        return dp[1]