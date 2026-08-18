'''
=== 3152. Special Array II ===

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that subarray nums[fromi..toi] is special or not.
Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.
 
Example 1:
    Input: nums = [3,4,1,2,6], queries = [[0,4]]
    Output: [false]
    Explanation:
    The subarray is [3,4,1,2,6]. 2 and 6 are both even.
Example 2:
    Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
    Output: [false,true]
    Explanation:
    - The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
    - The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
    3. 1 <= queries.length <= 105
    4. queries[i].length == 2
    5. 0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
'''
# === 915ms && 56.4MB === #
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        group = [i for i in range(n)]
        for i in range(n-1):
            if nums[i] % 2 != nums[i+1] % 2:
                group[i+1] = group[i]
        return [group[i] == group[j] for i, j in queries]