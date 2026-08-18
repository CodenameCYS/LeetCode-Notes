'''
=== 1655. Distribute Repeating Integers ===

You are given an array of n integers, nums, where there are at most 50 unique values in the array. You are also given an array of m customer order quantities, quantity, where quantity[i] is the amount of integers the ith customer ordered. Determine if it is possible to distribute nums such that:
    - The ith customer gets exactly quantity[i] integers,
    - The integers the ith customer gets are all equal, and
    - Every customer is satisfied.
Return true if it is possible to distribute nums according to the above conditions.

Example 1:
    Input: nums = [1,2,3,4], quantity = [2]
    Output: false
    Explanation: The 0th customer cannot be given two different integers.
Example 2:
    Input: nums = [1,2,3,3], quantity = [2]
    Output: true
    Explanation: The 0th customer is given [3,3]. The integers [1,2] are not used.
Example 3:
    Input: nums = [1,1,2,2], quantity = [2,2]
    Output: true
    Explanation: The 0th customer is given [1,1], and the 1st customer is given [2,2].
Example 4:
    Input: nums = [1,1,2,3], quantity = [2,2]
    Output: false
    Explanation: Although the 0th customer could be given [1,1], the 1st customer cannot be satisfied.
Example 5:
    Input: nums = [1,1,1,1,1], quantity = [2,3]
    Output: true
    Explanation: The 0th customer is given [1,1], and the 1st customer is given [1,1,1].
 
Constraints:
    1. n == nums.length
    2. 1 <= n <= 105
    3. 1 <= nums[i] <= 1000
    4. m == quantity.length
    5. 1 <= m <= 10
    6. 1 <= quantity[i] <= 105
    7. There are at most 50 unique values in nums.
'''
# === 4268ms && 25.6MB === #
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        counter = list(Counter(nums).values())
        quantity = sorted(quantity, reverse=True)
        n = len(quantity)
        
        def dfs(idx):
            if idx >= n:
                return True
            for i, c in enumerate(counter):
                if c < quantity[idx]:
                    continue
                counter[i] -= quantity[idx]
                if dfs(idx+1):
                    return True
                counter[i] += quantity[idx]
            return False
        
        return dfs(0)