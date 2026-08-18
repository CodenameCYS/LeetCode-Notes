'''
=== 506. Relative Ranks ===

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
    Input: [5, 4, 3, 2, 1]
    Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
    For the left two athletes, you just need to output their relative ranks according to their scores.

Note:
    1. N is a positive integer and won't exceed 10,000.
    2. All the scores of athletes are guaranteed to be unique.
'''
import numpy
# === 120ms(26.21%) && 29.1MB(25%) === #
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        rank = numpy.argsort(-numpy.array(nums))
        ans = ["" for i in range(len(nums))]
        for i,r in enumerate(rank):
            if i == 0:
                ans[r] = "Gold Medal"
            elif i == 1:
                ans[r] = "Silver Medal"
            elif i == 2:
                ans[r] = "Bronze Medal"
            else:
                ans[r] = str(i+1)
        return ans