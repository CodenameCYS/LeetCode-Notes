'''
=== 856. Score of Parentheses ===

Given a balanced parentheses string S, compute the score of the string based on the following rule:
    - () has score 1
    - AB has score A + B, where A and B are balanced parentheses strings.
    - (A) has score 2 * A, where A is a balanced parentheses string.
 
Example 1:
    Input: "()"
    Output: 1
Example 2:
    Input: "(())"
    Output: 2
Example 3:
    Input: "()()"
    Output: 2
Example 4:
    Input: "(()(()))"
    Output: 6
 
Note:
    1. S is a balanced parentheses string, containing only ( and ).
    2. 2 <= S.length <= 50
'''
# === 48ms(16.46%) && 13.9MB(44.07%) === #
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0] * 26
        level = -1
        for c in S:
            if c == "(":
                level += 1
            else:
                if stack[level+1] == 0:
                    stack[level] += 1
                else:
                    stack[level] += 2 * stack[level+1]
                    stack[level+1] = 0
                level -= 1
            # print(stack)
        return stack[0]