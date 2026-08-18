'''
=== 3863. Minimum Operations to Sort a String ===

You are given a string s consisting of lowercase English letters.
In one operation, you can select any substring of s that is not the entire string and sort it in ascending alphabetical order.
Return the minimum number of operations required to make s sorted in ascending order. If it is not possible, return -1.
A substring is a contiguous non-empty sequence of characters within a string.
 
Example 1:
    Input: s = "dog"
    Output: 1
    Explanation:​​​​​​​
    Sort substring "og" to "go".
    Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.
Example 2:
    Input: s = "card"
    Output: 2
    Explanation:
    Sort substring "car" to "acr", so s = "acrd".
    Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.
Example 3:
    Input: s = "gf"
    Output: -1
    Explanation:
    It is impossible to sort s under the given constraints. Thus, the answer is -1.

Constraints:
    1. 1 <= s.length <= 105
    2. s consists of only lowercase English letters.
'''
# === 298ms && 21.00MB === #
class Solution:
    def minOperations(self, s: str) -> int:
        cnt = Counter(s)
        tgt = "".join(sorted(s))
        if tgt == s:
            return 0
        elif len(s) == 2:
            return -1
        elif s[0] == tgt[0] or s[-1] == tgt[-1]:
            return 1
        elif s[-1] == tgt[0] and cnt[s[-1]] == 1 and s[0] == tgt[-1] and cnt[s[0]] == 1:
            return 3
        else:
            return 2