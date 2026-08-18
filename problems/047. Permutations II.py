'''
=== 47. Permutations II ===

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
    Input: [1,1,2]
    Output:
    [
        [1,1,2],
        [1,2,1],
        [2,1,1]
    ]
'''
# === 72ms(38.92%) && 13MB(100%) === #
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        import itertools
        ans = set()
        for it in itertools.permutations(nums):
            ans.add(tuple(it))
        return [list(it) for it in ans]