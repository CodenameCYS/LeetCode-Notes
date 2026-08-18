'''
=== 2663. Lexicographically Smallest Beautiful String ===

A string is beautiful if:
    - It consists of the first k letters of the English lowercase alphabet.
    - It does not contain any substring of length 2 or more which is a palindrome.
You are given a beautiful string s of length n and a positive integer k.
Return the lexicographically smallest string of length n, which is larger than s and is beautiful. If there is no such string, return an empty string.
A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b.
For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.

Example 1:
    Input: s = "abcz", k = 26
    Output: "abda"
    Explanation: The string "abda" is beautiful and lexicographically larger than the string "abcz".
    It can be proven that there is no string that is lexicographically larger than the string "abcz", beautiful, and lexicographically smaller than the string "abda".
Example 2:
    Input: s = "dc", k = 4
    Output: ""
    Explanation: It can be proven that there is no string that is lexicographically larger than the string "dc" and is beautiful.
    
Constraints:
    1. 1 <= n == s.length <= 105
    2. 4 <= k <= 26
    3. s is a beautiful string.
'''
# === 754ms && 19.1MB === #
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        chars = [ord(ch) - ord('a') for ch in s]
        n = len(chars)
        idx = n-1
        chars[idx] += 1
        while 0 <= idx < n:
            # print(chars, idx, chars[idx])
            if chars[idx] >= k:
                while idx >= 0 and chars[idx] >= k:
                    chars[idx] = 0
                    idx -= 1
                if idx >= 0:
                    chars[idx] += 1
            else:
                while (idx-1 >= 0 and chars[idx-1] == chars[idx]) or (idx-2 >= 0 and chars[idx-2] == chars[idx]):
                    chars[idx] += 1
                if chars[idx] < k:
                    idx += 1
        # print(chars)
        if idx == -1:
            return ""
        chars = [chr(x + ord('a')) for x in chars]
        return "".join(chars)
                
            
            
        
        