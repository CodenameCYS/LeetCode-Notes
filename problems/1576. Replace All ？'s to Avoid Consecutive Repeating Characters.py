'''
=== 1576. Replace All ?'s to Avoid Consecutive Repeating Characters ===

Given a string s containing only lower case English letters and the '?' character, convert all the '?' characters into lower case letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.
It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.

Example 1:
    Input: s = "?zs"
    Output: "azs"
    Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid modification as the string will consist of consecutive repeating characters in "zzs".
Example 2:
    Input: s = "ubv?w"
    Output: "ubvaw"
    Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings will consist of consecutive repeating characters in "ubvvw" and "ubvww".
Example 3:
    Input: s = "j?qg??b"
    Output: "jaqgacb"
Example 4:
    Input: s = "??yw?ipkj?"
    Output: "acywaipkja"
 
Constraints:
    1. 1 <= s.length <= 100
    2. s contains only lower case English letters and '?'.
'''
# === 32ms && 13.6MB === #
class Solution:
    def modifyString(self, s: str) -> str:
        def get_valid(pre, nxt):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c != pre and c != nxt:
                    return c
                
        ans = []
        count = 0
        for c in s:
            if c != "?":
                last = '' if ans == [] else ans[-1]
                stack = []
                nxt = c
                while count > 0:
                    nxt = get_valid(last, nxt)
                    stack.insert(0, nxt)
                    count -= 1
                ans += stack
                ans.append(c)
            else:
                count += 1
        last = '' if ans == [] else ans[-1]
        stack = []
        nxt= ''
        while count > 0:
            nxt = get_valid(last, nxt)
            stack.insert(0, nxt)
            count -= 1
        ans += stack
        return "".join(ans)
                