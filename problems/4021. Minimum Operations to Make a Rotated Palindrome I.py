'''
=== 4021. Minimum Operations to Make a Rotated Palindrome I ===

You are given a string s consisting of lowercase English letters.
You can perform the following operations any number of times (including zero) and in any order:
    - Increment: Choose any index i and replace s[i] with the next lowercase English letter. The letter after 'z' is 'a'.
    - Left rotate: Move the first character of the string to the end.
Return the minimum number of operations required to make s a palindrome.

Example 1:
    Input: s = "abc"
    Output: 2
    Explanation:
    One optimal solution:
    Left rotate the string: "abc" -> "bca".
    Increment 'a' to 'b': "bca" -> "bcb".
    "bcb" is a palindrome. Thus, the answer is 2.
Example 2:
    Input: s = "yb"
    Output: 3
    Explanation:
    Increment the first character three times: "yb" -> "zb" -> "ab" -> "bb".
    "bb" is a palindrome. Thus, the answer is 3.
 
Constraints:
    1. 2 <= s.length <= 2000
    2. s consists only of lowercase English letters.
'''
# === 6810ms && 19.17MB === #
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        ss = s + s
        ans = math.inf
        for i in range(n):
            cnt = i
            for j in range(n//2):
                diff = (ord(ss[i+n-1-j]) - ord(ss[i+j]) + 26) % 26
                # print(f"{ss[i+j]} -> {ss[i+n-1-j]}, op = {diff}")
                cnt += min(diff, 26-diff)
            ans = min(ans, cnt)
        return ans