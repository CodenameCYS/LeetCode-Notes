'''
=== 40. Combination Sum II ===

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
    1. All numbers (including target) will be positive integers.
    2. The solution set must not contain duplicate combinations.

Example 1:
    Input: candidates = [10,1,2,7,6,1,5], target = 8,
    A solution set is:
    [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
    ]
Example 2:
    Input: candidates = [2,5,2,1,2], target = 5,
    A solution set is:
    [
        [1,2,2],
        [5]
    ]
'''
# === 76ms(57.04%) && 12.8MB(100%) === #
class Solution:
    def my_combination_sum(self, candidates, target, present, ans):
        for i, num in enumerate(candidates):
            if num == target:
                ans.append(present + [num])
            elif num < target:
                self.my_combination_sum(candidates[i+1:], target-num, present + [num], ans)
            else:
                break
        return
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        self.my_combination_sum(candidates, target, [], ans)
        ans = set([tuple(it) for it in ans])
        return [list(it) for it in ans]

# === 52ms(75.99%) && 12.7MB(100%) === #
class Solution:
    def my_combination_sum(self, candidates, target, present, ans):
        i = 0
        n = len(candidates)
        for num in candidates:
            if num == target:
                ans.append(present + [num])
                break
            elif num < target:
                self.my_combination_sum(candidates[i+1:], target-num, present + [num], ans)
                while i < n and candidates[i] == num:
                    i += 1
            else:
                break
            # i += 1
        return
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        self.my_combination_sum(candidates, target, [], ans)
        ans = set([tuple(it) for it in ans])
        return [list(it) for it in ans]

# === 40ms(93.35%) && 12.8MB(100%) === #
class Solution:
    def my_combination_sum(self, candidates, target, present, ans):
        i = 0
        n = len(candidates)
        while i<n:
            num = candidates[i]
            if num == target:
                ans.append(present + [num])
                break
            elif num < target:
                self.my_combination_sum(candidates[i+1:], target-num, present + [num], ans)
                while i < n and candidates[i] == num:
                    i += 1
            else:
                break
        return
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        self.my_combination_sum(candidates, target, [], ans)
        return ans