'''
=== 1963. Minimum Number of Swaps to Make the String Balanced ===

You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
A string is called balanced if and only if:
    - It is the empty string, or
    - It can be written as AB, where both A and B are balanced strings, or
    - It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.
Return the minimum number of swaps to make s balanced.

Example 1:
    Input: s = "][]["
    Output: 1
    Explanation: You can make the string balanced by swapping index 0 with index 3.
    The resulting string is "[[]]".
Example 2:
    Input: s = "]]][[["
    Output: 2
    Explanation: You can do the following to make the string balanced:
    - Swap index 0 with index 4. s = "[]][][".
    - Swap index 1 with index 5. s = "[[][]]".
    The resulting string is "[[][]]".
Example 3:
    Input: s = "[]"
    Output: 0
    Explanation: The string is already balanced.
 
Constraints:
    1. n == s.length
    2. 2 <= n <= 106
    3. n is even.
    4. s[i] is either '[' or ']'.
    5. The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.
'''
# === 947ms && 389.1MB === #
class Solution:
    def minSwaps(self, s: str) -> int:
        bra, ket = 0, 0
        for c in s:
            if c == "[":
                bra += 1
            else:
                if bra == 0:
                    ket += 1
                else:
                    bra -= 1
        # print(res)
        n = bra + ket
        
        @lru_cache(None)
        def fn(n):
            if n == 0:
                return 0
            if n == 2:
                return 1
            return 1 + fn(n-4)
        
        return fn(n)

# === 367ms && 25.3MB === #
class Solution:
    def minSwaps(self, s: str) -> int:
        bra, ket = 0, 0
        for c in s:
            if c == "[":
                bra += 1
            else:
                if bra == 0:
                    ket += 1
                else:
                    bra -= 1
        # print(res)
        n = bra
        return (n+1)//2
                