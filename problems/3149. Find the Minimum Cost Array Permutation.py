'''
=== 3149. Find the Minimum Cost Array Permutation ===

You are given an array nums which is a permutation of [0, 1, 2, ..., n - 1]. The score of any permutation of [0, 1, 2, ..., n - 1] named perm is defined as:
score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|
Return the permutation perm which has the minimum possible score. If multiple permutations exist with this score, return the one that is lexicographically smallest among them.

Example 1:
    Input: nums = [1,0,2]
    Output: [0,1,2]
    Explanation:
    The lexicographically smallest permutation with minimum cost is [0,1,2]. The cost of this permutation is |0 - 0| + |1 - 2| + |2 - 1| = 2.
Example 2:
    Input: nums = [0,2,1]
    Output: [0,2,1]
    Explanation:
    The lexicographically smallest permutation with minimum cost is [0,2,1]. The cost of this permutation is |0 - 1| + |2 - 2| + |1 - 0| = 2.

Constraints:
    1. 2 <= n == nums.length <= 14
    2. nums is a permutation of [0, 1, 2, ..., n - 1].
'''
# === 7140ms && 237.1MB === #
class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        status = 0
        best_score = math.inf
        
        @lru_cache(None)
        def dp(idx, status, first, pre, pre_score):
            nonlocal best_score
            if pre_score >= best_score:
                return math.inf, []
            if idx >= n:
                best_score = min(best_score, abs(pre - nums[first]) + pre_score)
                return abs(pre - nums[first]) + pre_score, []
            score, ans = math.inf, []
            for i in range(n):
                if status & (1 << i) == 0:
                    if idx == 0:
                        s, nxt = dp(idx+1, status | (1 << i), i, i, 0)
                    else:
                        s, nxt = dp(idx+1, status | (1 << i), first, i, pre_score + abs(pre-nums[i]))
                    if s < score:
                        ans = [i] + nxt
                        score = s
            return score, ans
        
        score, ans = dp(0, 0, 0, 0, 0)
        return ans

                