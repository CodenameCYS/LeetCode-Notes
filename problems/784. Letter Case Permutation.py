'''
=== 784. Letter Case Permutation ===

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
    Input: S = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

    Input: S = "3z4"
    Output: ["3z4", "3Z4"]

    Input: S = "12345"
    Output: ["12345"]

Note:
    1. S will be a string with length between 1 and 12.
    2. S will consist only of letters or digits.
'''
# === 48ms(92.67%) && 14.1MB(20%) === #
class Solution:
    def insert(self, ans, c):
        if ans == []:
            ans = [c]
        else:
            ans = [it+c for it in ans]
        return ans
    
    def letterCasePermutation(self, S: str) -> List[str]:
        digits = set("1234567890")
        delta = ord('A') - ord('a')
        ans = []
        for c in S.lower():
            if c in digits:
                ans = self.insert(ans, c)
            else:
                ans = self.insert(ans, c) + self.insert(ans, chr(ord(c) + delta))
        return ans