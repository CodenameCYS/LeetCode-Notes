'''
=== 3455. Shortest Matching Substring ===

You are given a string s and a pattern string p, where p contains exactly two '*' characters.
The '*' in p matches any sequence of zero or more characters.
Return the length of the shortest substring in s that matches p. If there is no such substring, return -1.
A substring is a contiguous sequence of characters within a string (the empty substring is considered valid).

Example 1:
    Input: s = "abaacbaecebce", p = "ba*c*ce"
    Output: 8
    Explanation:
    The shortest matching substring of p in s is "baecebce".
Example 2:
    Input: s = "baccbaadbc", p = "cc*baa*adb"
    Output: -1
    Explanation:
    There is no matching substring in s.
Example 3:
    Input: s = "a", p = "**"
    Output: 0
    Explanation:
    The empty substring is the shortest matching substring.
Example 4:
    Input: s = "madlogic", p = "*adlogi*"
    Output: 6
    Explanation:
    The shortest matching substring of p in s is "adlogi".

Constraints:
    1. 1 <= s.length <= 105
    2. 2 <= p.length <= 105
    3. s contains only lowercase English letters.
    4. p contains only lowercase English letters and exactly two '*'.
'''
def z_algorithm(s):
    n = len(s)
    z = [0 for _ in range(n)]
    l, r = -1, -1
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r-l] == s[r]:
                r += 1
            z[i] = r-l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and s[r-l] == s[r]:
                    r += 1
                z[i] = r-l
                r -= 1
    z[0] = n
    return z
# === 1015ms && 30.7MB === #
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        if p.replace("*", "") in s:
            return len(p.replace("*", ""))
        
        subs = p.strip("*").split("*")
        if len(subs) == 1:
            return len(subs[0]) if subs[0] in s else -1
        
        def get_matches_idx(sub):
            n = len(sub)
            z = z_algorithm(sub + s)[n:]
            return [i for i, k in enumerate(z) if k >= n]
        
        n = len(subs)
        ans = math.inf
        matches = [get_matches_idx(sub) for sub in subs]
        for st in matches[0]:
            ed = st+len(subs[0])
            for match, sub in zip(matches[1:], subs[1:]):
                i = bisect.bisect_left(match, ed)
                if i >= len(match):
                    ed = math.inf
                    break
                else:
                    ed = match[i] + len(sub)
            ans = min(ans, ed-st)
        return ans if ans != math.inf else -1
        
        
            