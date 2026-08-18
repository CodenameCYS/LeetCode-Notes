'''
=== 2116. Check if a Parentheses String Can Be Valid ===

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
    - It is ().
    - It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    - It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,
    - If locked[i] is '1', you cannot change s[i].
    - But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

Example 1:
    Input: s = "))()))", locked = "010100"
    Output: true
    Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
    We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
Example 2:
    Input: s = "()()", locked = "0000"
    Output: true
    Explanation: We do not need to make any changes because s is already valid.
Example 3:
    Input: s = ")", locked = "0"
    Output: false
    Explanation: locked permits us to change s[0]. 
    Changing s[0] to either '(' or ')' will not make s valid.
 
Constraints:
    1. n == s.length == locked.length
    2. 1 <= n <= 105
    3. s[i] is either '(' or ')'.
    4. locked[i] is either '0' or '1'.
'''
# === 208ms && 15.4MB === #
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        cnt = 0
        for ch, st in zip(s, locked):
            if st == "0" or ch == "(":
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    return False
                
        cnt = 0
        for ch, st in zip(s[::-1], locked[::-1]):
            if st == "0" or ch == ")":
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    return False
        return True