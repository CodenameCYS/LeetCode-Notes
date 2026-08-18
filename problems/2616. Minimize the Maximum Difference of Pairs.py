'''
=== 2616. Minimize the Maximum Difference of Pairs ===

You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.
Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.
Return the minimum maximum difference among all p pairs.

Example 1:
    Input: nums = [10,1,2,7,1,3], p = 2
    Output: 1
    Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
    The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
Example 2:
    Input: nums = [4,2,1,2], p = 1
    Output: 0
    Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 0 <= nums[i] <= 109
    3. 0 <= p <= (nums.length)/2
'''
# === 1210ms && 28.7MB === #
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        
        def is_possible(k):
            i, cnt = 0, 0
            while i < n-1:
                if nums[i+1] - nums[i] <= k:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt >= p:
                    break
            return cnt >= p
        
        i, j = -1, nums[-1]-nums[0]
        while j-i > 1:
            m = (i+j) // 2
            if is_possible(m):
                j = m
            else:
                i = m
        return j
            