'''
=== 2423. Remove Letter To Equalize Frequency ===

You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.
Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:
    - The frequency of a letter x is the number of times it occurs in the string.
    - You must remove exactly one letter and cannot chose to do nothing.
 
Example 1:
    Input: word = "abcc"
    Output: true
    Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:
    Input: word = "aazz"
    Output: false
    Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
 
Constraints:
    1. 2 <= word.length <= 100
    2. word consists of lowercase English letters only.
'''
# === 28ms && 13.9MB === #
class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = list(Counter(word).values())
        
        def is_valid(arr, tgt):
            cnt = 0
            for x in arr:
                if tgt != 1 and (x == tgt+1 or x == 1):
                    cnt += 1
                elif tgt == 1 and x == tgt + 1:
                    cnt += 1
                elif x != tgt:
                    return False
            return (tgt != 1 and cnt == 1) or (tgt == 1 and cnt <= 1)
        
        return len(cnt) == 1 or any(is_valid(cnt, x) for x in cnt)