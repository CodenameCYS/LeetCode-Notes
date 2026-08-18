'''
=== 1593. Split a String Into the Max Number of Unique Substrings ===

Given a string s, return the maximum number of unique substrings that the given string can be split into.
You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
A substring is a contiguous sequence of characters within a string.

Example 1:
    Input: s = "ababccc"
    Output: 5
    Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:
    Input: s = "aba"
    Output: 2
    Explanation: One way to split maximally is ['a', 'ba'].
Example 3:
    Input: s = "aa"
    Output: 1
    Explanation: It is impossible to split the string any further.
 
Constraints:
    1. 1 <= s.length <= 16
    2. s contains only lower case English letters.
'''
# === 392ms && 14MB === #
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        
        ans = 1
        used = set()
        def dfs(idx):
            nonlocal ans, used
            # print(idx, used)
            if idx >= n:
                ans = max(ans, len(used))
            for i in range(idx+1, n+1):
                if s[idx: i] not in used:
                    used.add(s[idx:i])
                    dfs(i)
                    used.remove(s[idx:i])
            return
        
        dfs(0)
        # print("="*10)
        return ans
         
# === 84ms && 13.8MB === #   
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        
        ans = 1
        used = set()
        def dfs(idx):
            nonlocal ans, used
            # print(idx, used)
            if idx >= n:
                ans = max(ans, len(used))
            elif len(used) + n-idx+1 <= ans:
                return
            for i in range(idx+1, n+1):
                if s[idx: i] not in used:
                    used.add(s[idx:i])
                    dfs(i)
                    used.remove(s[idx:i])
            return
        
        dfs(0)
        # print("="*10)
        return ans