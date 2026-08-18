'''
=== 2472. Maximum Number of Non-overlapping Palindrome Substrings ===

You are given a string s and a positive integer k.
Select a set of non-overlapping substrings from the string s that satisfy the following conditions:
    - The length of each substring is at least k.
    - Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.
A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "abaccdbbd", k = 3
    Output: 2
    Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
    It can be shown that we cannot find a selection with more than two valid substrings.
Example 2:
    Input: s = "adbcda", k = 2
    Output: 0
    Explanation: There is no palindrome substring of length at least 2 in the string.
 
Constraints:
    1. 1 <= k <= s.length <= 2000
    2. s consists of lowercase English letters.
'''
# === 2849ms && 96.7MB === #
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        if k == 1:
            return n
        
        palindromes = defaultdict(list)
        for m in range(n):
            l, r = m-1, m+1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                if r-l+1 >= k:
                    palindromes[l].append(r+1)
                l -= 1
                r += 1
            
            l, r = m, m+1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                if r-l+1 >= k:
                    palindromes[l].append(r+1)
                l -= 1
                r += 1
            
                    
        @lru_cache(None)
        def dp(idx):
            if idx >= n:
                return 0
            res = dp(idx+1)
            for j in palindromes[idx]:
                res = max(res, 1+dp(j))
            return res
        
        return dp(0)
                    
# === 97ms && 14MB === #
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pals = [-1] * n
        
        for m in range(n):
            # odd
            l, r = m, m
            while 0 <= l and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    pals[r] = max(pals[r], l)
                    break
                l -= 1
                r += 1

            # even
            l, r = m - 1, m
            while 0 <= l and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    pals[r] = max(pals[r], l)
                    break
                l -= 1
                r += 1

        dp = [0] * (n + 1)
        for r in range(n):
            if pals[r] == -1:
                dp[r + 1] = dp[r]
            else:
                dp[r + 1] = max(dp[r], dp[pals[r]] + 1)
        return dp[n]