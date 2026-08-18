'''
=== 1547. Minimum Cost to Cut a Stick ===

Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:
Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.
You should perform the cuts in order, you can change the order of the cuts as you wish.
The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.
Return the minimum total cost of the cuts.

Example 1:
    Input: n = 7, cuts = [1,3,4,5]
    Output: 16
    Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:
    The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
    Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).
Example 2:
    Input: n = 9, cuts = [5,6,1,4,2]
    Output: 22
    Explanation: If you try the given cuts ordering the cost will be 25.
    There are much ordering with total cost <= 25, for example, the order [4, 6, 5, 2, 1] has total cost = 22 which is the minimum possible.

Constraints:
    1. 2 <= n <= 10^6
    2. 1 <= cuts.length <= min(n - 1, 100)
    3. 1 <= cuts[i] <= n - 1
    4. All the integers in cuts array are distinct.
'''
import math
# === 2925ms && 27MB === #
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = tuple(sorted(cuts))
        print(cuts)
        
        @lru_cache(None)
        def dp(st, ed, cuts):
            if len(cuts) == 0:
                return 0
            ans = math.inf
            for idx, cut in enumerate(cuts):
                s1 = dp(st, cut, cuts[:idx])
                s2 = dp(cut, ed, cuts[idx+1:])
                ans = min(ans, ed-st + s1 + s2)
            return ans
        return dp(0, n, cuts)

# === 1500ms && 18.1MB === #
class SolutionV2:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts)
        # print(cuts)
        
        @lru_cache(None)
        def dp(st, ed, st_idx, ed_idx):
            if st_idx == ed_idx:
                return 0
            ans = math.inf
            for idx in range(st_idx, ed_idx):
                cut = cuts[idx]
                s1 = dp(st, cut, st_idx, idx)
                s2 = dp(cut, ed, idx+1, ed_idx)
                ans = min(ans, ed-st + s1 + s2)
            return ans
        return dp(0, n, 0, len(cuts))
    
# === 1156ms && 18.9MB === #
class SolutionV3:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted(cuts)
        
        @lru_cache(None)
        def dp(st, ed, st_idx, ed_idx):
            if st_idx == ed_idx:
                return 0
            return ed-st + min([dp(st, cuts[idx], st_idx, idx) + dp(cuts[idx], ed, idx+1, ed_idx) for idx in range(st_idx, ed_idx)])
        
        return dp(0, n, 0, len(cuts))
    
# === 844ms && 17.7MB === #
class SolutionV4:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        
        @lru_cache(None)
        def dp(st, ed):
            if ed - st == 1:
                return 0
            return cuts[ed]-cuts[st] + min([dp(st, idx) + dp(idx, ed) for idx in range(st+1, ed)])
        
        return dp(0, len(cuts)-1)