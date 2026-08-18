'''
=== 1832. Check if the Sentence Is Pangram ===

A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
    Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    Output: true
    Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:
    Input: sentence = "leetcode"
    Output: false
 
Constraints:
    1. 1 <= sentence.length <= 1000
    2. sentence consists of lowercase English letters.
'''
# === 36ms && 14.3MB === #
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cnt = [0 for _ in range(26)]
        for c in sentence:
            cnt[ord(c) - ord('a')] += 1
        return all(x > 0 for x in cnt)