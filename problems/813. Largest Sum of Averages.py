'''
=== 813. Largest Sum of Averages ===

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?
Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
    Input: 
    A = [9,1,2,3,9]
    K = 3
    Output: 20
    Explanation: 
    The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
    We could have also partitioned A into [9, 1], [2], [3, 9], for example.
    That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
 
Note:
    1. 1 <= A.length <= 100.
    2. 1 <= A[i] <= 10000.
    3. 1 <= K <= A.length.
    4. Answers within 10^-6 of the correct answer will be accepted as correct.
'''
# === 120ms(95.83%) && 16.5MB(33.33%) === #
class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        @lru_cache(None)
        def dp(i, j, k):
            if k == 1:
                return sum(A[i:j]) / (j-i)
            return max([dp(i,m,1) + dp(m,j,k-1) for m in range(i+1, j-k+2)])
        return dp(0, len(A), K)