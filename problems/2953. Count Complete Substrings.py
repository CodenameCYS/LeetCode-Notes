'''
=== 2953. Count Complete Substrings ===

You are given a string word and an integer k.
A substring s of word is complete if:
    - Each character in s occurs exactly k times.
    - The difference between two adjacent characters is at most 2. That is, for any two adjacent characters c1 and c2 in s, the absolute difference in their positions in the alphabet is at most 2.
Return the number of complete substrings of word.
A substring is a non-empty contiguous sequence of characters in a string.

Example 1:
    Input: word = "igigee", k = 2
    Output: 3
    Explanation: The complete substrings where each character appears exactly twice and the difference between adjacent characters is at most 2 are: igigee, igigee, igigee.
Example 2:
    Input: word = "aaabbbccc", k = 3
    Output: 6
    Explanation: The complete substrings where each character appears exactly three times and the difference between adjacent characters is at most 2 are: aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc.
 
Constraints:
    1. 1 <= word.length <= 105
    2. word consists only of lowercase English letters.
    3. 1 <= k <= word.length
'''
# === 7872ms && 52.8MB === #
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        
        def count_complete(s):
            n = len(s)
            if len(set(s)) == 1:
                return max(n-k+1, 0)
            
            cnt = [[0 for _ in range(26)] for _ in range(n+1)]
            for i, ch in enumerate(s):
                for j in range(26):
                    cnt[i+1][j] = cnt[i][j]
                cnt[i+1][ord(ch) - ord('a')] += 1
            
            ans = 0
            for i in range(n-k+1):
                j = i+k
                while j <= n:
                    diff = [y-x for x, y in zip(cnt[i], cnt[j])]
                    if any(x > k for x in diff):
                        break
                    if all(x == k or x == 0 for x in diff):
                        ans += 1
                    j += k
            return ans
        
        idx = 0
        i, n = 0, len(word)
        ans = 0
        while i < n-1:
            if abs(ord(word[i]) - ord(word[i+1])) > 2:
                ans += count_complete(word[idx:i+1])
                idx = i+1
            i += 1
        ans += count_complete(word[idx:])
        return ans