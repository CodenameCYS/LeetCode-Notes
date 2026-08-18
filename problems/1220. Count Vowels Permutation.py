'''
=== 1220. Count Vowels Permutation ===

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
    - Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
    - Each vowel 'a' may only be followed by an 'e'.
    - Each vowel 'e' may only be followed by an 'a' or an 'i'.
    - Each vowel 'i' may not be followed by another 'i'.
    - Each vowel 'o' may only be followed by an 'i' or a 'u'.
    - Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: n = 1
    Output: 5
    Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:
    Input: n = 2
    Output: 10
    Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 
    Input: n = 5
    Output: 68
    
Constraints:
    1. 1 <= n <= 2 * 10^4
'''
# === 752ms && 185.3MB === #
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def dp(n, pre):
            if n == 0:
                return 1
            res = 0
            if pre in ["", "e", "i", "u"]:
                res += dp(n-1, "a")
            if pre in ["", "a", "i"]:
                res += dp(n-1, "e")
            if pre in ["", "e", "o"]:
                res += dp(n-1, "i")
            if pre in ["", "i"]:
                res += dp(n-1, "o")
            if pre in ["", "i", "o"]:
                res += dp(n-1, "u")
            return res % MOD
        
        return dp(n, "")
        