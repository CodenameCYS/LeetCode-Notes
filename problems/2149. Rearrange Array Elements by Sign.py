'''
=== 2149. Rearrange Array Elements by Sign ===

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should rearrange the elements of nums such that the modified array follows the given conditions:
    1. Every consecutive pair of integers have opposite signs.
    2. For all integers with the same sign, the order in which they were present in nums is preserved.
    3. The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Example 1:
    Input: nums = [3,1,-2,-5,2,-4]
    Output: [3,-2,1,-5,2,-4]
    Explanation:
    The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
    The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
    Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  
Example 2:
    Input: nums = [-1,1]
    Output: [1,-1]
    Explanation:
    1 is the only positive integer and -1 the only negative integer in nums.
    So nums is rearranged to [1,-1].
 
Constraints:
    1. 2 <= nums.length <= 2 * 105
    2. nums.length is even
    3. 1 <= |nums[i]| <= 105
    4. nums consists of equal number of positive and negative integers.
'''
# === 1576ms && 45.8MB === #
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        n = len(pos)
        res = [0 for _ in range(2*n)]
        for i in range(n):
            res[2*i] = pos[i]
            res[2*i+1] = neg[i]
        return res
                    
        