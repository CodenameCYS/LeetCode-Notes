'''
=== 4030. Check ASCII Palindromic ===

You are given a string s consisting of lowercase English letters.
Construct a binary string by replacing each character in s with the 8-bit binary representation of its ASCII value, including leading zeros, while preserving the original order of the characters.
Return true if the resulting binary string is a palindrome. Otherwise, return false.

Example 1:
    Input: s = "ff"
    Output: true
    Explanation:
    The ASCII value of f is 102, whose 8-bit binary representation is 01100110.
    Thus, the binary string is 0110011001100110.
    Since this binary string is a palindrome, the output is true.
Example 2:
    Input: s = "leet"
    Output: false
    Explanation:
    The ASCII values of l, e, e, and t are 108, 101, 101, and 116, respectively.
    Their 8-bit binary representations are 01101100, 01100101, 01100101, and 01110100.
    Thus, the binary string is 01101100011001010110010101110100.
    Since this binary string is not a palindrome, the output is false.
 
Constraints:
    1. 1 <= s.length <= 100
    2. s consists of lowercase English letters.
'''
# === 0ms && 19.48MB === #
class Solution:
    def isPalindromic(self, s: str) -> bool:

        def fn(ch):
            return bin(ord(ch))[2:].rjust(8, '0')
        
        digits = "".join([fn(ch) for ch in s])
        return digits == digits[::-1]