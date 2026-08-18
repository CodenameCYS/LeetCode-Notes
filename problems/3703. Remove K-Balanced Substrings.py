'''
=== 3703. Remove K-Balanced Substrings ===

You are given a string s consisting of '(' and ')', and an integer k.
A string is k-balanced if it is exactly k consecutive '(' followed by k consecutive ')', i.e., '(' * k + ')' * k.
For example, if k = 3, k-balanced is "((()))".
You must repeatedly remove all non-overlapping k-balanced substrings from s, and then join the remaining parts. Continue this process until no k-balanced substring exists.
Return the final string after all possible removals.
A substring is a contiguous non-empty sequence of characters within a string.

​​​​​​​Example 1:
    Input: s = "(())", k = 1
    Output: ""
    Explanation:
    k-balanced substring is "()"
    Step	Current s	k-balanced	Result s
    1	(())	(())	()
    2	()	()	Empty
    Thus, the final string is "".
Example 2:
    Input: s = "(()(", k = 1
    Output: "(("
    Explanation:
    k-balanced substring is "()"
    Step	Current s	k-balanced	Result s
    1	(()(	(()(	((
    2	((	-	((
    Thus, the final string is "((".
Example 3:
    Input: s = "((()))()()()", k = 3
    Output: "()()()"
    Explanation:
    k-balanced substring is "((()))"
    Step	Current s	k-balanced	Result s
    1	((()))()()()	((()))()()()	()()()
    2	()()()	-	()()()
    Thus, the final string is "()()()".

Constraints:
    1. 2 <= s.length <= 105
    2. s consists only of '(' and ')'.
    3. 1 <= k <= s.length / 2
'''
# === 255ms && 22.75MB === #
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []
        prev, cnt = "(", 0
        
        def push(stack, ch, cnt):
            if len(stack) == 0:
                stack.append([ch, cnt])
            elif ch == stack[-1][0]:
                stack[-1] = [ch, stack[-1][1] + cnt]
            elif ch == "(":
                stack.append([ch, cnt])
            else:
                while stack and cnt >= k and stack[-1][1] >= k:
                    stack[-1][1] -= k
                    cnt -= k
                    if stack[-1][-1] == 0:
                        stack.pop()
                        if stack and stack[-1][0] == ch:
                            cnt += stack.pop()[1]
                if cnt > 0:
                    if len(stack) == 0 or stack[-1][0] != ch:
                        stack.append([ch, cnt])
                    else:
                        stack[-1] = [ch, stack[-1][1] + cnt]
            return

        for ch in s:
            if ch == prev:
                cnt += 1
                continue
            if cnt != 0:
                push(stack, prev, cnt)
            prev, cnt = ch, 1
        push(stack, ch, cnt)
        ans = ""
        for ch, cnt in stack:
            ans += ch * cnt
        return ans