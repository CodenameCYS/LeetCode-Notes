'''
=== 1611. Minimum One Bit Operations to Make Integers Zero ===

Given an integer n, you must transform it into 0 using the following operations any number of times:
    - Change the rightmost (0th) bit in the binary representation of n.
    - Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.

Example 1:
    Input: n = 0
    Output: 0
Example 2:
    Input: n = 3
    Output: 2
    Explanation: The binary representation of 3 is "11".
    "11" -> "01" with the 2nd operation since the 0th bit is 1.
    "01" -> "00" with the 1st operation.
Example 3:
    Input: n = 6
    Output: 4
    Explanation: The binary representation of 6 is "110".
    "110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
    "010" -> "011" with the 1st operation.
    "011" -> "001" with the 2nd operation since the 0th bit is 1.
    "001" -> "000" with the 1st operation.
Example 4:
    Input: n = 9
    Output: 14
Example 5:
    Input: n = 333
    Output: 393
 
Constraints:
    1. 0 <= n <= 109
'''
# === 24ms && 14.4MB === #
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        digits = []
        while n != 0:
            digits.append(n & 1)
            n = n >> 1
        # print(digits)
        n = len(digits)
        
        from_zero = [1 for i in range(n)]
        to_zero = [1 for i in range(n)]
        for i in range(1, n):
            to_zero[i] = 1 + from_zero[i-1] + to_zero[i-1]
            from_zero[i] = 1 + to_zero[i-1] + from_zero[i-1]
        
        @lru_cache(None)
        def dp(idx):
            if idx < 0:
                return 0
            if idx == 0:
                return digits[idx]
            if digits[idx] == 0:
                return dp(idx-1)
            else:
                return to_zero[idx] - dp(idx-1)
        
        return dp(n-1)