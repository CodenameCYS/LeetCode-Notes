'''
=== 90. Subsets II ===

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
    Input: [1,2,2]
    Output:
    [
        [2],
        [1],
        [1,2,2],
        [2,2],
        [1,2],
        []
    ]
'''
# === 32ms(93.01%) & 13MB(100%) === #
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        count = {}
        for n in nums:
            if n in count.keys():
                count[n] += 1
            else:
                count[n] = 1
        # print(count)
        ans = [[]]
        for k,v in count.items():
            tmp = []
            for i in range(v+1):
                tmp.extend([[k]*i + it for it in ans])
            ans = tmp
            # print("ans: {}".format(ans))
        return ans