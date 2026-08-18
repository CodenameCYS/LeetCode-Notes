'''
=== 474. Ones and Zeroes ===

You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:
    Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
    Output: 4
    Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
    Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
    {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:
    Input: strs = ["10","0","1"], m = 1, n = 1
    Output: 2
    Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 
Constraints:
    1. 1 <= strs.length <= 600
    2. 1 <= strs[i].length <= 100
    3. strs[i] consists only of digits '0' and '1'.
    4. 1 <= m, n <= 100
'''
# === 1172ms(96.72%) && 120.3MB(16.80%) === #
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnt = [Counter(s) for s in strs]
        cnt = [[s["0"], s["1"]] for s in cnt]
        cnt = sorted(cnt, key=lambda x: [x[0]+x[1], x[0], x[1]])
        N = len(cnt)
        
        @lru_cache(None)
        def dp(idx, m, n):
            if idx >= N or cnt[idx][0] + cnt[idx][1] > m + n:
                return 0
            res = dp(idx+1, m, n)
            if cnt[idx][0] <= m and cnt[idx][1] <= n:
                res = max(res, 1 + dp(idx+1, m-cnt[idx][0], n-cnt[idx][1]))
            return res
        
        return dp(0, m, n)
        