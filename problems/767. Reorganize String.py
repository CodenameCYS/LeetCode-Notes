'''
=== 767. Reorganize String ===

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.

Example 1:
    Input: S = "aab"
    Output: "aba"
Example 2:
    Input: S = "aaab"
    Output: ""

Note:
    - S will consist of lowercase letters and have length in range [1, 500].
'''
# === 32ms(54.55%) && 12.9MB(100%) === #
class Solution:
    def insert(self, s, c, num):
        c = [c] * num
        ans = []
        while s != [] and c != []:
            ans.extend([c.pop(), s.pop()])
        if s != []:
            ans.extend(s[::-1])
        else:
            ans.extend(c)
        return ans
    
    def reorganizeString(self, S: str) -> str:
        alphabet = {}
        for c in S:
            if c in alphabet.keys():
                alphabet[c] += 1
            else:
                alphabet[c] = 1
        alphabet = sorted(alphabet.items(), key=lambda x:x[1])
        if alphabet[-1][1] > (len(S)+1) // 2:
            return ""
        ans = []
        for c, num in alphabet:
            ans = self.insert(ans, c, num)
            # print(ans)
        return "".join(ans)