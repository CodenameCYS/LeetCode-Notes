'''
=== 1297. Maximum Number of Occurrences of a Substring ===

Given a string s, return the maximum number of ocurrences of any substring under the following rules:
    - The number of unique characters in the substring must be less than or equal to maxLetters.
    - The substring size must be between minSize and maxSize inclusive.
 
Example 1:
    Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
    Output: 2
    - Explanation: Substring "aab" has 2 ocurrences in the original string.
    It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
Example 2:
    Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
    Output: 2
    - Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
Example 3:
    Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
    Output: 3
Example 4:
    Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
    Output: 0
 
Constraints:
    1. 1 <= s.length <= 10^5
    2. 1 <= maxLetters <= 26
    3. 1 <= minSize <= maxSize <= min(26, s.length)
    4. s only contains lowercase English letters.
'''
# === Time Limit Exceeded (37/40) === #
class Solution:
    def isValid(self, s: str, maxLetters: int):
        return len(set(s)) <= maxLetters
    
    def CountOccurrences(self, string: str, substring: str): 
        count = 0
        start = 0
        slen = len(string)
        while start < slen: 
            flag = string.find(substring, start) 
            if flag != -1: 
                start = flag + 1
                count += 1
            else: 
                return count
        return count

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ans = 0
        slen = len(s)
        have_seen = set()
        for i in range(slen-minSize):
            for j in range(maxSize-minSize+1):
                ed = i+j+minSize
                if ed > slen:
                    break
                if s[i:ed] in have_seen:
                    continue
                if self.isValid(s[i:ed], maxLetters):
                    tmp = self.CountOccurrences(s, s[i:ed])
                    # print(s[i:ed], tmp)
                    if tmp > ans:
                        ans = tmp
                have_seen.add(s[i:ed])
        return ans
# === 1224ms & 124.2MB === #
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        slen = len(s)
        count = {}
        for st in range(slen-minSize+1):
            ed = st + 1
            tmp = set()
            while ed-st <= maxSize and ed <= slen:
                tmp.add(s[ed-1])
                if len(tmp) > maxLetters:
                    break
                if ed-st >= minSize:
                    if s[st:ed] in count.keys():
                        count[s[st:ed]] += 1
                    else:
                        count[s[st:ed]] = 1
                ed += 1
        # print(count)
        ans = max(count.values()) if count else 0
        return ans
# === 180ms === #
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter, n = collections.Counter(), len(s)
        for i in range(n - minSize + 1):
            if len(set(s[i:i + minSize])) <= maxLetters:
                counter[s[i:i + minSize]] += 1
        return max(counter.values()) if counter else 0
# === 180ms & 14.9MB === #
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        slen = len(s)
        count = {}
        for st in range(slen-minSize+1):
            ed = st + minSize
            if len(set(s[st:ed])) <= maxLetters:
                if s[st:ed] in count.keys():
                    count[s[st:ed]] += 1
                else:
                    count[s[st:ed]] = 1
        ans = max(count.values()) if count else 0
        return ans