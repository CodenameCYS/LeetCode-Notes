'''
=== 557. Reverse Words in a String III ===

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''
# === 32ms(69.61%) && === 13.2MB(96.15%) === #
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = " ".join([t[::-1] for t in s.split()])
        return ans