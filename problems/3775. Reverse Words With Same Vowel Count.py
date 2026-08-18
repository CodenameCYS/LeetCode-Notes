'''
=== 3775. Reverse Words With Same Vowel Count ===

You are given a string s consisting of lowercase English words, each separated by a single space.
Determine how many vowels appear in the first word. Then, reverse each following word that has the same vowel count. Leave all remaining words unchanged.
Return the resulting string.
Vowels are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
    Input: s = "cat and mice"
    Output: "cat dna mice"
    Explanation:​​​​​​​
    The first word "cat" has 1 vowel.
    "and" has 1 vowel, so it is reversed to form "dna".
    "mice" has 2 vowels, so it remains unchanged.
    Thus, the resulting string is "cat dna mice".
Example 2:
    Input: s = "book is nice"
    Output: "book is ecin"
    Explanation:
    The first word "book" has 2 vowels.
    "is" has 1 vowel, so it remains unchanged.
    "nice" has 2 vowels, so it is reversed to form "ecin".
    Thus, the resulting string is "book is ecin".
Example 3:
    Input: s = "banana healthy"
    Output: "banana healthy"
    Explanation:
    The first word "banana" has 3 vowels.
    "healthy" has 2 vowels, so it remains unchanged.
    Thus, the resulting string is "banana healthy".
 
Constraints:
    1. 1 <= s.length <= 105
    2. s consists of lowercase English letters and spaces.
    3. Words in s are separated by a single space.
    4. s does not contain leading or trailing spaces.
'''
# === 227ms && 22.67MB === #
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        def count_vowel(word):
            return sum([1 if ch in "aeiou" else 0 for ch in word])

        cnt = count_vowel(words[0])
        n = len(words)
        for i in range(1, n):
            if count_vowel(words[i]) == cnt:
                words[i] = words[i][::-1]
        return " ".join(words)