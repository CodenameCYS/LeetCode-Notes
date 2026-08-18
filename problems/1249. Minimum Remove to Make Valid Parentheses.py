'''
# === 1249. Minimum Remove to Make Valid Parentheses === #

Given a string s of '(' , ')' and lowercase English characters. 
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
    - It is the empty string, contains only lowercase characters, or
    - It can be written as AB (A concatenated with B), where A and B are valid strings, or
    - It can be written as (A), where A is a valid string.
 
Example 1:
    Input: s = "lee(t(c)o)de)"
    Output: "lee(t(c)o)de"
    - Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:
    Input: s = "a)b(c)d"
    Output: "ab(c)d"
Example 3:
    Input: s = "))(("
    Output: ""
    - Explanation: An empty string is also valid.
Example 4:
    Input: s = "(a(b(c)d)"
    Output: "a(b(c)d)"
 
Constraints:
    1. 1 <= s.length <= 10^5
    2. s[i] is one of  '(' , ')' and lowercase English letters.
'''
# === 1020ms(8.5%) & 16.5MB === #
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ""
        count = 0
        loc = 0
        loc_list = []
        for w in s:
            if w == "(":
                ans += w
                count += 1
                loc_list.append(loc)
                loc += 1
            elif w == ")":
                if count > 0:
                    ans += w
                    count -= 1
                    loc += 1
            else:
                ans += w
                loc += 1
        if count == 0:
            return ans
        else:
            return ''.join([ans[i] for i in range(len(ans)) if i not in loc_list[-count:]])

# === 108ms(76.85%) && 16MB(55.49%) === #
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        brakets = []
        res = []
        length = 0
        for c in s:
            if c == "(":
                brakets.append(length)
            elif c == ")":
                if brakets == []:
                    continue
                brakets.pop()
            res.append(c)
            length += 1
        while brakets:
            idx = brakets.pop()
            res.pop(idx)
        return "".join(res)
        
        