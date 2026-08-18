'''
=== 2531. Make Number of Distinct Characters Equal ===

You are given two 0-indexed strings word1 and word2.
A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].
Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.

Example 1:
    Input: word1 = "ac", word2 = "b"
    Output: false
    Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string.
Example 2:
    Input: word1 = "abcc", word2 = "aab"
    Output: true
    Explanation: We swap index 2 of the first string with index 0 of the second string. The resulting strings are word1 = "abac" and word2 = "cab", which both have 3 distinct characters.
Example 3:
    Input: word1 = "abcde", word2 = "fghij"
    Output: true
    Explanation: Both resulting strings will have 5 distinct characters, regardless of which indices we swap.
 
Constraints:
    1. 1 <= word1.length, word2.length <= 105
    2. word1 and word2 consist of only lowercase English letters.
'''
# === 114ms && 15.4MB === #
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        
        diff = len(cnt1) - len(cnt2)
        
        for ch1 in cnt1:
            for ch2 in cnt2:
                if ch1 == ch2:
                    change = 0
                elif cnt1[ch1] == 1 and cnt2[ch2] == 1:
                    if cnt2[ch1] > 0 and cnt1[ch2] > 0:
                        change = 0
                    elif cnt2[ch1] > 0 and cnt1[ch2] == 0:
                        change = 1
                    elif cnt2[ch1] == 0 and cnt1[ch2] > 0:
                        change = -1
                    else:
                        change = 0
                elif cnt1[ch1] == 1 and cnt2[ch2] > 1:
                    if cnt2[ch1] > 0 and cnt1[ch2] > 0:
                        change = -1
                    elif cnt2[ch1] > 0 and cnt1[ch2] == 0:
                        change = 0
                    elif cnt2[ch1] == 0 and cnt1[ch2] > 0:
                        change = -2
                    else:
                        change = -1
                elif cnt1[ch1] > 1 and cnt2[ch2] == 1:
                    if cnt2[ch1] > 0 and cnt1[ch2] > 0:
                        change = 1
                    elif cnt2[ch1] > 0 and cnt1[ch2] == 0:
                        change = 2
                    elif cnt2[ch1] == 0 and cnt1[ch2] > 0:
                        change = 0
                    else:
                        change = 1
                else:
                    if cnt2[ch1] > 0 and cnt1[ch2] > 0:
                        change = 0
                    elif cnt2[ch1] > 0 and cnt1[ch2] == 0:
                        change = 1
                    elif cnt2[ch1] == 0 and cnt1[ch2] > 0:
                        change = -1
                    else:
                        change = 0
                
                if change == -diff:
                    return True
                        
        return False
            