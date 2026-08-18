'''
=== 594. Longest Harmonious Subsequence ===

We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
    Input: [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].
 
Note: The length of the input array will not exceed 20,000.
'''
# === 352ms(46.2%) && 15MB(7.69%) === #
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            counter[n] = counter[n] + 1 if n in counter.keys() else 1
        counter = sorted(counter.items(), key = lambda x:x[0])
        ans = 0
        for i in range(len(counter)-1):
            if counter[i+1][0] - counter[i][0] == 1:
                tmp = counter[i][1] + counter[i+1][1]
                ans = ans if ans > tmp else tmp
        return ans