'''
=== 3133. Minimum Array End ===

You are given two integers n and x. You have to construct an array of positive integers nums of size n where for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], and the result of the bitwise AND operation between all elements of nums is x.
Return the minimum possible value of nums[n - 1].

Example 1:
    Input: n = 3, x = 4
    Output: 6
    Explanation:
    nums can be [4,5,6] and its last element is 6.
Example 2:
    Input: n = 2, x = 7
    Output: 15
    Explanation:
    nums can be [7,15] and its last element is 15.

Constraints:
    1. 1 <= n, x <= 108
'''
# === 31ms && 16.6MB === #
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        move = bin(n-1)[2:]
        x = bin(x)[2:]
        idx = len(x)-1
        ans = []
        for ch in move[::-1]:
            while idx >= 0 and x[idx] == "1":
                ans.insert(0, 1)
                idx -= 1
            ans.insert(0, int(ch))
            if idx != -1:
                idx -= 1
        while idx >= 0:
            ans.insert(0, int(x[idx]))
            idx -= 1
            
        ret = 0
        for d in ans:
            ret = ret * 2 + d
        return ret
            
        