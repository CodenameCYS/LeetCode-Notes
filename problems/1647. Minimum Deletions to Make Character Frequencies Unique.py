'''
=== 1647. Minimum Deletions to Make Character Frequencies Unique ===

A string s is called good if there are no two different characters in s that have the same frequency.
Given a string s, return the minimum number of characters you need to delete to make s good.
The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:
    Input: s = "aab"
    Output: 0
    Explanation: s is already good.
Example 2:
    Input: s = "aaabbbcc"
    Output: 2
    Explanation: You can delete two 'b's resulting in the good string "aaabcc".
    Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:
    Input: s = "ceabaacb"
    Output: 2
    Explanation: You can delete both 'c's resulting in the good string "eabaab".
    Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 
Constraints:
    1. 1 <= s.length <= 105
    2. s contains only lowercase English letters.
'''
# === 112ms && 14.9MB === #
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = sorted(Counter(s).values())
        if len(counter) <= 1:
            return 0
        ans = 0
        idx = 1
        n = len(counter)
        while idx < n:
            if counter[idx] == counter[idx-1]:
                i = idx-1
                while i >= 0 and counter[i] > 0 and counter[i] == counter[idx]-(idx-1-i):
                    i -= 1
                ans += (idx-1-i)
                tmp = counter.pop(idx)
                tmp -= idx-1-i
                bisect.insort(counter, tmp)
            idx += 1
        return ans
    
# === 116ms && 14.9MB === #
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = sorted(Counter(s).values())
        if len(counter) <= 1:
            return 0
        ans = 0
        seen = set()
        for c in counter:
            if c not in seen:
                seen.add(c)
                continue
            while c in seen and c > 0:
                c -= 1
                ans += 1
            if c > 0:
                seen.add(c)
        return ans
    
# === 104ms && 14.8MB === #
class Solution:
    def minDeletions(self, s: str) -> int:
        c=Counter(s)
        cnt=sorted(c.values(),reverse=True)
        cur = cnt[0]
        ans = 0
        for x in cnt:
            ans += max(0,x - cur)
            cur = min(x - 1, cur - 1)
            cur = max(0, cur)
        return ans