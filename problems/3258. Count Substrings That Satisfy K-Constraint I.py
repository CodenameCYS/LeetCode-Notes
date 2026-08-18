'''
=== 3258. Count Substrings That Satisfy K-Constraint I ===

You are given a binary string s and an integer k.
A binary string satisfies the k-constraint if either of the following conditions holds:
    - The number of 0's in the string is at most k.
    - The number of 1's in the string is at most k.
Return an integer denoting the number of substrings of s that satisfy the k-constraint.

Example 1:
    Input: s = "10101", k = 1
    Output: 12
    Explanation:
    Every substring of s except the substrings "1010", "10101", and "0101" satisfies the k-constraint.
Example 2:
    Input: s = "1010101", k = 2
    Output: 25
    Explanation:
    Every substring of s except the substrings with a length greater than 5 satisfies the k-constraint.
Example 3:
    Input: s = "11111", k = 1
    Output: 15
    Explanation:
    All substrings of s satisfy the k-constraint.

Constraints:
    1. 1 <= s.length <= 50
    2. 1 <= k <= s.length
    3. s[i] is either '0' or '1'.
'''
# === 44ms && 16.4MB === #
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        i, j = 0, 0
        cnt = defaultdict(int)
        ans = 0
        while i < n:
            while j < n:
                if cnt["0"] > k and cnt["1"] > k:
                    break
                cnt[s[j]] += 1
                j += 1
            if cnt["0"] > k and cnt["1"] > k:
                ans += j-i-1
            else:
                ans += j-i
            # print(f"i={i}, j={j}, cnt={cnt}, cnt={j-i}, ans={ans}")
            cnt[s[i]] -= 1
            i += 1
        return ans
                