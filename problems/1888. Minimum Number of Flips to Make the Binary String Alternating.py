'''
=== 1888. Minimum Number of Flips to Make the Binary String Alternating ===

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:
    - Type-1: Remove the character at the start of the string s and append it to the end of the string.
    - Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
The string is called alternating if no two adjacent characters are equal.
    - For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 
Example 1:
    Input: s = "111000"
    Output: 2
    Explanation: Use the first operation two times to make s = "100011".
    Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:
    Input: s = "010"
    Output: 0
    Explanation: The string is already alternating.
Example 3:
    Input: s = "1110"
    Output: 1
    Explanation: Use the second operation on the second element to make s = "1010".
 
Constraints:
    1. 1 <= s.length <= 105
    2. s[i] is either '0' or '1'.
'''
# === 1460ms && 15MB === #
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        cnt = [[0, 0], [0, 0]]
        for i, c in enumerate(s):
            cnt[ord(c)-ord('0')][i%2] += 1
        # print(cnt)
        d1 = abs((n+1)//2 - cnt[0][0]) + abs(n//2 - cnt[1][1])
        d2 = abs((n+1)//2 - cnt[1][0]) + abs(n//2 - cnt[0][1])
        res = min(d1, d2)
        for i in range(n-1):
            cnt[ord(s[i])-ord('0')][0] -= 1
            cnt[ord(s[i])-ord('0')][n % 2] += 1
            cnt = [cnt[0][::-1], cnt[1][::-1]]
            # print(cnt)
            d1 = abs((n+1)//2 - cnt[0][0]) + abs(n//2 - cnt[1][1])
            d2 = abs((n+1)//2 - cnt[1][0]) + abs(n//2 - cnt[0][1])
            res = min(res, d1, d2)
        return res