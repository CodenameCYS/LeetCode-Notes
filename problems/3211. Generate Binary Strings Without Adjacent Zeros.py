'''
=== 3211. Generate Binary Strings Without Adjacent Zeros ===

You are given a positive integer n.
A binary string x is valid if all substrings of x of length 2 contain at least one "1".
Return all valid strings with length n, in any order.

Example 1:
    Input: n = 3
    Output: ["010","011","101","110","111"]
    Explanation:
    The valid strings of length 3 are: "010", "011", "101", "110", and "111".
Example 2:
    Input: n = 1
    Output: ["0","1"]
    Explanation:
    The valid strings of length 1 are: "0" and "1".

Constraints:
    1. 1 <= n <= 18
'''
# === 49ms && 21.1MB === #
class Solution:
    @lru_cache(None)
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        pre = self.validStrings(n-1)
        ans = []
        for sub in pre:
            ans.append("1" + sub)
            if sub[0] == "1":
                ans.append("0" + sub)
        return ans
        