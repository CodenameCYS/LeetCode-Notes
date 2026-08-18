'''
=== 795. Number of Subarrays with Bounded Maximum ===

We are given an array A of positive integers, and two positive integers L and R (L <= R).
Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :
    Input: 
    A = [2, 1, 4, 3]
    L = 2
    R = 3
    Output: 3
    Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Note:
    1. L, R  and A[i] will be an integer in the range [0, 10^9].
    2. The length of A will be in the range of [1, 50000].
'''
# === 404ms(23.78%) && 17.1MB(14.29%) === #
class Solution:
    def cn2(self, st, ed):
        if ed - st < 1:
            return 0
        return (ed - st) * (ed - st + 1) // 2
    
    def count_subarray(self, st, ed, key_point):
        if st > ed or key_point == []:
            return 0
        ans = self.cn2(st, ed)
        i = st
        for kp in key_point:
            ans -= self.cn2(i, kp)
            i = kp+1
        ans -= self.cn2(i, ed)
        return ans
        
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        hooks = []
        for i, n in enumerate(A):
            if n >= L and n <= R:
                hooks.append((i, 0))
            elif n > R:
                hooks.append((i, 1))
        # print(hooks)
        ans = 0
        st = 0
        key_point = []
        for i, h in enumerate(hooks):
            if h[1] == 1:
                ans += self.count_subarray(st, h[0], key_point)
                key_point = []
                st = h[0] + 1
            else:
                key_point.append(h[0])
        ans += self.count_subarray(st, len(A), key_point)
        return ans