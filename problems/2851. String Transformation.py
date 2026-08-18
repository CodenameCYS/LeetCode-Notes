'''
=== 2851. String Transformation ===

You are given two strings s and t of equal length n. You can perform the following operation on the string s:
    - Remove a suffix of s of length l where 0 < l < n and append it at the start of s.
        - For example, let s = 'abcd' then in one operation you can remove the suffix 'cd' and append it in front of s making s = 'cdab'.
You are also given an integer k. Return the number of ways in which s can be transformed into t in exactly k operations.
Since the answer can be large, return it modulo 109 + 7.

Example 1:
    Input: s = "abcd", t = "cdab", k = 2
    Output: 2
    Explanation: 
    First way:
    In first operation, choose suffix from index = 3, so resulting s = "dabc".
    In second operation, choose suffix from index = 3, so resulting s = "cdab".
    Second way:
    In first operation, choose suffix from index = 1, so resulting s = "bcda".
    In second operation, choose suffix from index = 1, so resulting s = "cdab".
Example 2:
    Input: s = "ababab", t = "ababab", k = 1
    Output: 2
    Explanation: 
    First way:
    Choose suffix from index = 2, so resulting s = "ababab".
    Second way:
    Choose suffix from index = 4, so resulting s = "ababab".
 
Constraints:
    1. 2 <= s.length <= 5 * 105
    2. 1 <= k <= 1015
    3. s.length == t.length
    4. s and t consist of only lowercase English alphabets.
'''
# === 790ms && 41.2MB === #
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

def find_all(s, t):
    l, n = len(s), len(t)
    # print(l, n)
    prefix = z_algorithm(t)
    # print(prefix)
    nxt, m = n, 0
    for i in range(1, n):
        if i + prefix[i] == n:
            nxt = i
            m = prefix[i]
            break
    # print(nxt, m)
            
    idx = 0
    cnt = 0
    while idx < l:
        idx = s.find(t, idx)
        if idx == -1:
            break
        cnt += 1
        if nxt < n:
            while idx+n < l and t[m:] == s[idx+n:idx+n+nxt]:
                idx = idx+nxt
                cnt += 1
        idx += 1
    return cnt
        

class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        MOD = 10**9+7
        
        n = len(s)
        # m = len([idx for idx in re.finditer(f"(?={t})", s+s)])
        m = find_all(s+s, t)
        m = m-1 if s==t else m
        # print(n, m)
        
        f0 = 0 if s != t else 1
        fk = f0 * pow(-1, k) + m * pow(n, -1, MOD) * (pow(n-1, k, MOD) - pow(-1, k))
        return fk % MOD