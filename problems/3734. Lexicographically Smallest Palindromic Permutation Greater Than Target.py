'''
=== 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target ===

You are given two strings s and target, each of length n, consisting of lowercase English letters.
Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

Example 1:
    Input: s = "baba", target = "abba"
    Output: "baab"
    Explanation:
    The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
    The lexicographically smallest permutation that is strictly greater than target is "baab".
Example 2:
    Input: s = "baba", target = "bbaa"
    Output: ""
    Explanation:
    The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
    None of them is lexicographically strictly greater than target. Therefore, the answer is "".
Example 3:
    Input: s = "abc", target = "abb"
    Output: ""
    Explanation:
    s has no palindromic permutations. Therefore, the answer is "".
Example 4:
    Input: s = "aac", target = "abb"
    Output: "aca"
    Explanation:
    The only palindromic permutation of s is "aca".
    "aca" is strictly greater than target. Therefore, the answer is "aca".

Constraints:
    1. 1 <= n == s.length == target.length <= 300
    2. s and target consist of only lowercase English letters.
'''
# === 33m2 && 18.42MB === #
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        src, tgt = Counter(s), Counter(target)

        def dfs(idx):
            nonlocal src, tgt
            if idx == n-1:
                # print(src, tgt)
                r, t = list(src.keys())[0], list(tgt.keys())[0]
                if r > t:
                    src.pop(r)
                    tgt.pop(t)
                    return r
                else:
                    return ""
            elif max(src.keys()) <= min(tgt.keys()):
                return ""
            t = target[idx]
            candi = sorted([ch for ch in src.keys() if ch >= t])
            if len(candi) == 0:
                return ""
            elif t == candi[0]:
                src[t] -= 1
                if src[t] == 0:
                    src.pop(t)
                tgt[t] -= 1
                if tgt[t] == 0:
                    tgt.pop(t)
                remain = dfs(idx+1)
                src[t] = 1 if t not in src else src[t]+1
                tgt[t] = 1 if t not in tgt else tgt[t]+1
                if remain != "":
                    return t + remain
                elif len(candi) == 1:
                    return ""
                else:
                    candi = candi[1]
            else:
                candi = candi[0]
            src[candi] -= 1
            remain = ""
            for ch in string.ascii_lowercase:
                remain += ch * src[ch]
            src[ch] += 1
            return candi + remain

        ans = dfs(0)
        return ans
        
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        mid = [ch for ch in cnt if cnt[ch] % 2 == 1]
        if len(mid) > 1:
            return ""
        elif len(mid) == 1:
            mid = mid[0]
        else:
            mid = ""
        src = ""
        for ch in cnt:
            src += ch * (cnt[ch] // 2)
        tgt = target[:len(src)]
        if src == "":
            return s if s > target else ""
        if "".join(sorted(src)) == "".join(sorted(tgt)):
            ans = tgt + mid + tgt[::-1]
            if ans > target:
                return ans
        ans = self.lexGreaterPermutation(src, tgt)
        # print(src, tgt, ans)
        if len(ans) < len(src):
            return ""
        ans = ans + mid + ans[::-1]
        return ans if ans > target else ""
        