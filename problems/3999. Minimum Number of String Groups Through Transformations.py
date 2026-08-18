'''
=== 3999. Minimum Number of String Groups Through Transformations ===

You are given an array of strings words.
Define a transformation on a string s as follows:
    - Let E be the subsequence of characters at even indices of s.
    - Let O be the subsequence of characters at odd indices of s.
    - Independently cyclically shift E and O by any number of positions to the right, possibly zero.
    - Reconstruct the string by placing the shifted E characters back into even indices and the shifted O characters back into odd indices.
Two strings are equivalent if one can be transformed into the other by a single transformation.
Partition words into the minimum number of groups such that:
    - Every string belongs to exactly one group.
    - Every pair of strings in the same group are equivalent.
Return an integer denoting the minimum number of groups.

Example 1:
    Input: words = ["ntgwz","zwntg"]
    Output: 1
    Explanation:
    For "ntgwz", the even-index subsequence is "ngz" and the odd-index subsequence is "tw".
    Shift "ngz" right by 1 position to obtain "zng", and shift "tw" right by 1 position to obtain "wt".
    After reconstructing the string, we obtain "zwntg".
    Therefore, both strings are equivalent and belong to the same group.
Example 2:
    Input: words = ["abc","cab","bac","acb","bca","cba"]
    Output: 3
    Explanation:
    The strings can be partitioned into the following groups:
    ["abc","cba"]
    ["cab","bac"]
    ["acb","bca"]
Example 3:
    Input: words = ["leet","abb","bab","deed","edde","code","bba"]
    Output: 5
    Explanation:
    The strings can be partitioned into the following groups:
    ["abb","bba"]
    ["deed","edde"]
    ["leet"]
    ["bab"]
    ["code"]
    ​​​​​​​​​​​​​​All pairs of strings in each group are equivalent.

Constraints:
    1. 1 <= words.length <= 105
    2. 1 <= words[i].length <= 5 * 105
    3. The sum of words[i].length does not exceed 5 * 105.
    4. words[i] consist of lowercase English letters.
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
# === 3176ms && 60.73MB === #
class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        n = len(words)

        groups = defaultdict(list)
        for word in words:
            cnt = [0 for _ in range(26)]
            for ch in word:
                cnt[ord(ch) - ord('a')] += 1
            groups[tuple(cnt)].append(word)

        def can_transform(src, tgt):
            n, m = len(src), len(tgt)
            if n != m:
                return False
            elif n <= 2:
                return src == tgt
            # cnt1, cnt2 = Counter(src), Counter(tgt)
            # if any(cnt1[ch] != cnt2[ch] for ch in cnt1):
            #     return False
            osrc = "".join([ch for i, ch in enumerate(src) if i % 2 == 1])
            esrc = "".join([ch for i, ch in enumerate(src) if i % 2 == 0])
            otgt = "".join([ch for i, ch in enumerate(tgt) if i % 2 == 1])
            etgt = "".join([ch for i, ch in enumerate(tgt) if i % 2 == 0])
            lo, le = len(osrc), len(esrc)
            zo = z_algorithm(otgt + osrc + osrc)
            ze = z_algorithm(etgt + esrc + esrc)
            return any(x >= lo for x in zo[lo:]) and any(x >= le for x in ze[le:])

        ans = 0
        for clusters in groups.values():
            centers = []
            for word in clusters:
                if centers != [] and any(can_transform(word, s) for s in centers):
                    continue
                centers.append(word)
            ans += len(centers)
        return ans
