'''
=== 39. Combination Sum ===

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
    1. All numbers (including target) will be positive integers.
    2. The solution set must not contain duplicate combinations.

Example 1:
    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
        [7],
        [2,2,3]
    ]
Example 2:
    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
        [2,2,2,2],
        [2,3,3],
        [3,5]
    ]
'''
# === 52ms(85.37%) && 12.7MB(100%) === #
class Solution:
    def my_combination_sum(self, candidates, target, present, ans):
        for i, num in enumerate(candidates):
            if num == target:
                ans.append(present + [num])
            elif num < target:
                self.my_combination_sum(candidates[i:], target-num, present + [num], ans)
            else:
                break
        return
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        self.my_combination_sum(candidates, target, [], ans)
        return ans