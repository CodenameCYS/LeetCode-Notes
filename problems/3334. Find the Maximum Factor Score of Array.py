'''
=== 3334. Find the Maximum Factor Score of Array ===

You are given an integer array nums.
The factor score of an array is defined as the product of the LCM and GCD of all elements of that array.
Return the maximum factor score of nums after removing at most one element from it.
Note that both the LCM and GCD of a single number are the number itself, and the factor score of an empty array is 0.
The term lcm(a, b) denotes the least common multiple of a and b.
The term gcd(a, b) denotes the greatest common divisor of a and b.

Example 1:
    Input: nums = [2,4,8,16]
    Output: 64
    Explanation:
    On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a maximum factor score of 4 * 16 = 64.
Example 2:
    Input: nums = [1,2,3,4,5]
    Output: 60
    Explanation:
    The maximum factor score of 60 can be obtained without removing any elements.
Example 3:
    Input: nums = [3]
    Output: 9

Constraints:
    1. 1 <= nums.length <= 100
    2. 1 <= nums[i] <= 30
'''
# === 12ms && 16.7MB === #
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        
        def fn(rm):
            _lcm = 0
            _gcd = 0
            for x in nums:
                if x == rm:
                    continue
                elif _lcm == 0:
                    _lcm, _gcd = x, x
                else:
                    _lcm = lcm(x, _lcm)
                    _gcd = gcd(x, _gcd)
            # print(f"nums = {nums}, rm={rm}, lcm={_lcm}, gcd={_gcd}, ans={_lcm * _gcd}")
            return _lcm * _gcd
        
        ans = fn(-1)
        for k, v in cnt.items():
            if v == 1:
                ans = max(ans, fn(k))
        return ans