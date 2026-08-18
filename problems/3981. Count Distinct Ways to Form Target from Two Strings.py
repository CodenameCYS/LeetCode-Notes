'''
=== 3981. Count Distinct Ways to Form Target from Two Strings ===

You are given three strings word1, word2, and target.
Your task is to count the number of ways to form target by choosing characters from word1 and word2 under the following conditions:
    - For each character of target, choose one matching character from either word1 or word2.
    - The chosen indices from word1 must be strictly increasing.
    - The chosen indices from word2 must be strictly increasing.
    - At least one character must be chosen from both word1 and word2.
Two ways are considered different if, for at least one position in target, the chosen character comes from a different string or a different index.
Return the number of ways. Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: word1 = "abc", word2 = "bac", target = "abc"
    Output: 5
    Explanation:
    There are 5 ways to form target:
    word1[0] = 'a', word1[1] = 'b', word2[2] = 'c'
    word1[0] = 'a', word2[0] = 'b', word1[2] = 'c'
    word1[0] = 'a', word2[0] = 'b', word2[2] = 'c'
    word2[1] = 'a', word1[1] = 'b', word1[2] = 'c'
    word2[1] = 'a', word1[1] = 'b', word2[2] = 'c'
    All ways preserve the increasing index order inside each string and choose at least one character from each string.
Example 2:
    Input: word1 = "cd", word2 = "cd", target = "ccd"
    Output: 4
    Explanation:
    There are 4 ways to form target:
    word1[0] = 'c', word2[0] = 'c', word1[1] = 'd'
    word1[0] = 'c', word2[0] = 'c', word2[1] = 'd'
    word2[0] = 'c', word1[0] = 'c', word1[1] = 'd'
    word2[0] = 'c', word1[0] = 'c', word2[1] = 'd'
    The first two 'c' characters in target must come one from each string. The final 'd' can be chosen from either string.
Example 3:
    Input: word1 = "xy", word2 = "xy", target = "xyxy"
    Output: 2
    Explanation:
    There are 2 ways to form target:
    word1[0] = 'x', word1[1] = 'y', word2[0] = 'x', word2[1] = 'y'
    word2[0] = 'x', word2[1] = 'y', word1[0] = 'x', word1[1] = 'y'
    Each "xy" part in target comes entirely from one string.
Example 4:
    Input: word1 = "ab", word2 = "cde", target = "ace"
    Output: 1
    Explanation:
    The only way is to choose word1[0] = 'a', word2[0] = 'c', and word2[2] = 'e'. Thus, the answer is 1.

Constraints:
    - 1 <= word1.length, word2.length, target.length <= 100
    - word1, word2, and target consist of lowercase English letters only.
'''
MOD = 10**9+7
# === 16301ms && 255.01MB === #
class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        n, m, l = len(target), len(word1), len(word2)
        chs1 = defaultdict(list)
        chs2 = defaultdict(list)
        for i, ch in enumerate(word1):
            chs1[ch].append(i)
        for i, ch in enumerate(word2):
            chs2[ch].append(i)

        @lru_cache(None)
        def dp(i, j, k, use1, use2):
            if i >= n:
                return 1 if use1 and use2 else 0
            elif j >= m and k >= l:
                return 0
            elif j >= m:
                if not use1:
                    return 0
                else:
                    return dp(i, j, k+1, use1, use2) if word2[k] != target[i] else (dp(i+1, j, k+1, use1, True) + dp(i, j, k+1, use1, use2)) % MOD
            elif k >= l:
                if not use2:
                    return 0
                else:
                    return dp(i, j+1, k, use1, use2) if word1[j] != target[i] else (dp(i+1, j+1, k, True, use2) + dp(i, j+1, k, use1, use2)) % MOD
            else:
                jj, kk = bisect.bisect_left(chs1[target[i]], j), bisect.bisect_left(chs2[target[i]], k)
                ans = 0
                for nxtj in chs1[target[i]][jj:]:
                    ans = (ans + dp(i+1, nxtj+1, k, True, use2)) % MOD
                for nxtk in chs2[target[i]][kk:]:
                    ans = (ans + dp(i+1, j, nxtk+1, use1, True)) % MOD
                return ans

        return dp(0, 0, 0, False, False)
