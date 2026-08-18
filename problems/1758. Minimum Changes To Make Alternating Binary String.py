'''
=== 1758. Minimum Changes To Make Alternating Binary String ===

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating.

Example 1:
    Input: s = "0100"
    Output: 1
    Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:
    Input: s = "10"
    Output: 0
    Explanation: s is already alternating.
Example 3:
    Input: s = "1111"
    Output: 2
    Explanation: You need two operations to reach "0101" or "1010".
 
Constraints:
    1. 1 <= s.length <= 104
    2. s[i] is either '0' or '1'.
'''
# === 48ms && 14.4MB === #
class Solution:
    def minOperations(self, s: str) -> int:
        odd = 0
        even = 0
        for i, c in enumerate(s):
            if i % 2 == 0:
                if c == "0":
                    even += 1
                else:
                    odd += 1
            else:
                if c == "1":
                    even += 1
                else:
                    odd += 1
        return min(odd, even)