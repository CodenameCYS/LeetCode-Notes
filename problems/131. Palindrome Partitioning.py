'''
=== 131. Palindrome Partitioning ===

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
# === 128ms(6.17%) && 13MB(100%) === #
class Solution:
    def is_palindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(int(n/2)):
            if s[i] != s[n-i-1]:
                return False
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        if s == "":
            return []
        n = len(s)
        if n == 1:
            return [[s]]
        ans = []
        for i in range(n):
            s1 = s[:i+1]
            s2 = s[i+1:]
            if self.is_palindrome(s1):
                if s2 == "":
                    ans.append([s1])
                else:
                    rest = self.partition(s2)
                    ans.extend([[s1] + sub for sub in rest])
        return ans
            