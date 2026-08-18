'''
=== 454. 4Sum II ===

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:
    Input:
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    Output:
    2
    Explanation:
    The two tuples are:
    1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
# === 488ms(10.49%) && 49.4MB(8.33%) === #
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        n = len(A)
        sum1 = {}
        sum2 = {}
        for i in range(n):
            for j in range(n):
                s1 = A[i] + B[j]
                s2 = C[i] + D[j]
                sum1[s1] = 1 if s1 not in sum1.keys() else sum1[s1] + 1
                sum2[s2] = 1 if s2 not in sum2.keys() else sum2[s2] + 1
                
        ans = 0
        for s1 in sum1.keys():
            if -s1 in sum2.keys():
                ans += sum1[s1] * sum2[-s1]
        return ans