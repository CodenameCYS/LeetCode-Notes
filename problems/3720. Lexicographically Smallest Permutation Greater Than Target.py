'''
=== 3720. Lexicographically Smallest Permutation Greater Than Target ===

You are given two strings s and target, both having length n, consisting of lowercase English letters.
Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.
A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.
A permutation is a rearrangement of all the characters of a string.

Example 1:
    Input: s = "abc", target = "bba"
    Output: "bca"
    Explanation:
    The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
    The lexicographically smallest permutation that is strictly greater than target is "bca".
Example 2:
    Input: s = "leet", target = "code"
    Output: "eelt"
    Explanation:
    The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
    The lexicographically smallest permutation that is strictly greater than target is "eelt".
Example 3:
    Input: s = "baba", target = "bbaa"
    Output: ""
    Explanation:
    The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
    None of them is lexicographically strictly greater than target. Therefore, the answer is "".

Constraints:
    1. 1 <= s.length == target.length <= 300
    2. s and target consist of only lowercase English letters.
'''
# === 34ms && 18.30MB === #
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        src, tgt = Counter(s), Counter(target)

        def dfs(idx):
            nonlocal src, tgt
            if idx == n-1:
                print(src, tgt)
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
                # if len(candi) == 1:
                #     print(src, tgt, idx)
                #     exit()
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