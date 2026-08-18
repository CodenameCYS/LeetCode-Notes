'''
=== 4007. Widest Possible Fence ===

You are given an integer array planks, where planks[i] represents the height of the ith wooden plank. Each plank has a width of 1 unit.
You want to build a fence consisting of planks that all have the same height.
You may either use a plank as is, or combine exactly two distinct original planks into a single plank whose height equals the sum of their heights. Each original plank can be used at most once, and not all original planks need to be used.
Return the maximum possible width of the fence that can be built.

Example 1:
    Input: planks = [1,3,2,5,7,5,4,2,1]
    Output: 4
    Explanation:
    We can have four planks of height 5.
    planks[3] = 5
    planks[5] = 5
    planks[0] + planks[6] = 1 + 4 = 5
    planks[1] + planks[2] = 3 + 2 = 5
    Hence, the maximum width is 4.
Example 2:
    Input: planks = [2,3,7]
    Output: 1
    Explanation:
    It is impossible to form two planks of the same height, even after combining two distinct original planks.
    Since not all original planks need to be used, we can choose any one plank as the fence.
    Therefore, the maximum possible width is 1.
 
Constraints:
    1. 1 <= planks.length <= 1000
    2. 1 <= planks[i] <= 109
'''
# === 1906ms && 75.71MB === #
class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        cnt = Counter(planks)
        heights = sorted(cnt.keys())
        n = len(heights)
        comb = defaultdict(int)
        for i in range(n):
            x = heights[i]
            if cnt[x] >= 2:
                comb[2*x] += cnt[x] // 2
            for j in range(i+1, n):
                y = heights[j]
                comb[x+y] += min(cnt[x], cnt[y])
        ans = 0
        for h in heights:
            ans = max(ans, cnt[h] + comb[h])
        for h in comb.keys():
            ans = max(ans, cnt[h] + comb[h])
        return ans
