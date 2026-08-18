'''
=== 2062. Count Vowel Substrings of a String ===

A substring is a contiguous (non-empty) sequence of characters within a string.
A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
Given a string word, return the number of vowel substrings in word.

Example 1:
    Input: word = "aeiouu"
    Output: 2
    Explanation: The vowel substrings of word are as follows (underlined):
    - "aeiouu"
    - "aeiouu"
Example 2:
    Input: word = "unicornarihan"
    Output: 0
    Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:
    Input: word = "cuaieuouac"
    Output: 7
    Explanation: The vowel substrings of word are as follows (underlined):
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    - "cuaieuouac"
    Example 4:
    Input: word = "bbaeixoubb"
    Output: 0
    Explanation: The only substrings that contain all five vowels also contain consonants, so there are no vowel substrings.
 
Constraints:
    1. 1 <= word.length <= 100
    2. word consists of lowercase English letters only.
'''
# === 200ms && 14.2MB === #
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        
        def have_all(cnt):
            return all(cnt[ch] > 0 for ch in "aeiou")
        
        res = 0
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                if word[j] not in "aeiou":
                    break
                cnt[word[j]] += 1
                if have_all(cnt):
                    res += 1
        return res