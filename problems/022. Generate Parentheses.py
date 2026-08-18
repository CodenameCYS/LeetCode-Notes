'''
=== 22. Generate Parentheses ===

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
# === 36ms(70.43%) && 14.1MB(45.79%) === #
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dp(i, j, s):
            nonlocal ans
            if j == n:
                ans.append(s)
            elif i <= j:
                dp(i+1, j, s + '(')
            elif i == n:
                dp(i, j+1, s + ')')
            else:
                dp(i+1, j, s + '(')
                dp(i, j+1, s + ')')
        
        dp(0, 0, "")
        
        return ans
                