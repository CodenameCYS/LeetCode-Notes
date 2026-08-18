'''
=== 3518. Smallest Palindromic Rearrangement II ===

You are given a palindromic string s and an integer k.
Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.
Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.
A string is palindromic if it reads the same forward and backward.
A permutation is a rearrangement of all the characters of a string.
A string a is lexicographically smaller than a string b if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
If the first min(a.length, b.length) characters do not differ, then the shorter string is the lexicographically smaller one.

Example 1:
    Input: s = "abba", k = 2
    Output: "baab"
    Explanation:
    The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
    Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".
Example 2:
    Input: s = "aa", k = 2
    Output: ""
    Explanation:
    There is only one palindromic rearrangement: "aa".
    The output is an empty string since k = 2 exceeds the number of possible rearrangements.
Example 3:
    Input: s = "bacab", k = 1
    Output: "abcba"
    Explanation:
    The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
    Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".
 
Constraints:
    1. 1 <= s.length <= 104
    2. s consists of lowercase English letters.
    3. s is guaranteed to be palindromic.
    4. 1 <= k <= 106
'''
MOD = 10**20 + 39
Factorials = [1 for i in range(10**4+1)]
for i in range(2, 10**4+1):
    Factorials[i] = i * Factorials[i-1] % MOD
    
def get_kth_smallest_string(s, k):
    cnt = Counter(s)
    n = len(s)
    
    def get_count(cnt):
        n = 0
        ans = 1
        for m in cnt.values():
            ans = (ans * pow(Factorials[m], -1, MOD)) % MOD
            n += m
        ans = (ans * Factorials[n]) % MOD
        return ans
    
    tot = get_count(cnt)
    if k == 1:
        return "".join(sorted(s))
    elif tot < k:
        return ""
    elif tot == k:
        return "".join(sorted(s)[::-1])
    
    def dfs(idx, k):
        if k == 1:
            return "".join([ch * cnt[ch] for ch in string.ascii_lowercase])
        for ch in string.ascii_lowercase:
            if cnt[ch] > 0:
                cnt[ch] -= 1
                tot = get_count(cnt)
                if tot >= k:
                    return ch + dfs(idx+1, k)
                k -= tot
                cnt[ch] += 1
        return ""
    
    return dfs(0, k)
            
# === 7403ms && 20MB === #
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # print("=" * 10)
        cnt = Counter(s)
        mid = ""
        ans = ""
        for ch in string.ascii_lowercase:
            ans += ch * (cnt[ch] // 2)
            if cnt[ch] % 2 == 1:
                mid = ch
        if ans == "":
            return mid if k == 1 else ""
        
        ans = get_kth_smallest_string(ans, k)
        return ans + mid + ans[::-1] if ans != "" else ""
    
# === 1055ms && 19.4MB === #
class Solution:
    def get_kth_smallest_string(self, s, k):
        cnt = Counter(s)
        n = len(s)

        def c(n, m, upper):
            m = min(n-m, m)
            ans = 1
            for i in range(m):
                ans = ans * (n-i) // (i+1)
                if ans >= upper:
                    return ans
            return ans

        def get_count(cnt, upper):
            n = sum(cnt.values())
            ans = 1
            for m in cnt.values():
                ans = ans * c(n, m, upper)
                n -= m
                if ans >= upper:
                    return ans
            return ans

        tot = get_count(cnt, k)
        if k == 1:
            return "".join(sorted(s))
        elif tot < k:
            return ""

        def dfs(idx, k):
            if k == 1:
                return "".join([ch * cnt[ch] for ch in string.ascii_lowercase])
            for ch in string.ascii_lowercase:
                if cnt[ch] > 0:
                    cnt[ch] -= 1
                    tot = get_count(cnt, k)
                    if tot >= k:
                        return ch + dfs(idx+1, k)
                    k -= tot
                    cnt[ch] += 1
            return ""

        return dfs(0, k)

    def smallestPalindrome(self, s: str, k: int) -> str:
        # print("=" * 10)
        cnt = Counter(s)
        mid = ""
        ans = ""
        for ch in string.ascii_lowercase:
            ans += ch * (cnt[ch] // 2)
            if cnt[ch] % 2 == 1:
                mid = ch
        if ans == "":
            return mid if k == 1 else ""
        
        ans = self.get_kth_smallest_string(ans, k)
        return ans + mid + ans[::-1] if ans != "" else ""
        
        
            
            
        
            
        
        
            
            
        
            