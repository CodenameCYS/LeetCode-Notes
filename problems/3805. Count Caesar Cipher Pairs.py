'''
=== 3805. Count Caesar Cipher Pairs ===

You are given an array words of n strings. Each string has length m and contains only lowercase English letters.
Two strings s and t are similar if we can apply the following operation any number of times (possibly zero times) so that s and t become equal.
    - Choose either s or t.
    - Replace every letter in the chosen string with the next letter in the alphabet cyclically. The next letter after 'z' is 'a'.
Count the number of pairs of indices (i, j) such that:
    - i < j
    - words[i] and words[j] are similar.
Return an integer denoting the number of such pairs.

Example 1:
    Input: words = ["fusion","layout"]
    Output: 1
    Explanation:
    words[0] = "fusion" and words[1] = "layout" are similar because we can apply the operation to "fusion" 6 times. The string "fusion" changes as follows.
    "fusion"
    "gvtjpo"
    "hwukqp"
    "ixvlrq"
    "jywmsr"
    "kzxnts"
    "layout"
Example 2:
    Input: words = ["ab","aa","za","aa"]
    Output: 2
    Explanation:
    words[0] = "ab" and words[2] = "za" are similar. words[1] = "aa" and words[3] = "aa" are similar.

Constraints:
    1. 1 <= n == words.length <= 105
    2. 1 <= m == words[i].length <= 105
    3. 1 <= n * m <= 105
    4. words[i] consists only of lowercase English letters.
'''
# === 1852ms && 29.78MB === #
class Solution:
    def countPairs(self, words: List[str]) -> int:
        
        def fn(word):
            nxt = [chr((ord(ch)-ord('a')+1)%26 + ord('a')) for ch in word]
            return "".join(nxt)

        mapping = {}
        cnt = defaultdict(int)
        for word in words:
            if word in mapping:
                cnt[mapping[word]] += 1
                continue
            mapping[word] = word
            cnt[word] += 1
            nxt = word
            for _ in range(25):
                nxt = fn(nxt)
                mapping[nxt] = word
        ans = 0
        for v in cnt.values():
            ans += v*(v-1)//2
        return ans