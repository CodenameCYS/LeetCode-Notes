'''
=== 3854. Minimum Operations to Make Array Parity Alternating ===

You are given an integer array nums.
An array is called parity alternating if for every index i where 0 <= i < n - 1, nums[i] and nums[i + 1] have different parity (one is even and the other is odd).
In one operation, you may choose any index i and either increase nums[i] by 1 or decrease nums[i] by 1.
Return an integer array answer of length 2 where:
    - answer[0] is the minimum number of operations required to make the array parity alternating.
    - answer[1] is the minimum possible value of max(nums) - min(nums) taken over all arrays that are parity alternating and can be obtained by performing exactly answer[0] operations.
An array of length 1 is considered parity alternating.

Example 1:
    Input: nums = [-2,-3,1,4]
    Output: [2,6]
    Explanation:
    Applying the following operations:
    Increase nums[2] by 1, resulting in nums = [-2, -3, 2, 4].
    Decrease nums[3] by 1, resulting in nums = [-2, -3, 2, 3].
    The resulting array is parity alternating, and the value of max(nums) - min(nums) = 3 - (-3) = 6 is the minimum possible among all parity alternating arrays obtainable using exactly 2 operations.
Example 2:
    Input: nums = [0,2,-2]
    Output: [1,3]
    Explanation:
    Applying the following operation:
    Decrease nums[1] by 1, resulting in nums = [0, 1, -2].
    The resulting array is parity alternating, and the value of max(nums) - min(nums) = 1 - (-2) = 3 is the minimum possible among all parity alternating arrays obtainable using exactly 1 operation.
Example 3:
    Input: nums = [7]
    Output: [0,0]
    Explanation:
    No operations are required. The array is already parity alternating, and the value of max(nums) - min(nums) = 7 - 7 = 0, which is the minimum possible.

Constraints:
    1. 1 <= nums.length <= 105
    2. -109 <= nums[i] <= 109
'''
# === 403ms && 34MB === #
class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:

        def get_min_diff(odd, even):
            if len(odd) > 0:
                max_odd, min_odd = max(odd), min(odd)
                max_odd = max_odd if max_odd % 2 == 1 else max_odd-1
                min_odd = min_odd if min_odd % 2 == 1 else min_odd+1
            if len(even) > 0:
                max_even, min_even = max(even), min(even)
                max_even = max_even if max_even % 2 == 0 else max_even-1
                min_even = min_even if min_even % 2 == 0 else min_even+1
            if len(odd) == 0:
                return max_even - min_even
            elif len(even) == 0:
                return max_odd - min_odd
            elif len(odd) == 1 and len(even) == 1:
                return min(abs(min_odd-max_even), abs(max_odd-min_even))
            elif len(odd) == 1:
                if max_odd >= max_even:
                    return max_odd - min_even
                elif min_odd <= min_even:
                    return max_even - min_odd
                else:
                    return max_even - min_even
            elif len(even) == 1:
                if max_even >= max_odd:
                    return max_even - min_odd
                elif min_even <= min_odd:
                    return max_odd - min_even
                else:
                    return max_odd - min_odd
            else:
                return max(max_odd, max_even) - min(min_odd, min_even)

        # case1: start with odd
        odd, even, cnt1 = set(), set(), 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                if num % 2 == 0:
                    cnt1 += 1
                odd.add(num)
            else:
                if num % 2 == 1:
                    cnt1 += 1
                even.add(num)
        diff1 = get_min_diff(odd, even)
        # print(odd, even, cnt1, diff1)
        
        # case2: start with even
        odd, even, cnt2 = set(), set(), 0
        for i, num in enumerate(nums):
            if i % 2 == 1:
                if num % 2 == 0:
                    cnt2 += 1
                odd.add(num)
            else:
                if num % 2 == 1:
                    cnt2 += 1
                even.add(num)
        diff2 = get_min_diff(odd, even)
        # print(odd, even, cnt2, diff2)

        if cnt1 < cnt2:
            return [cnt1, diff1]
        elif cnt1 > cnt2:
            return [cnt2, diff2]
        else:
            return [cnt1, min(diff1, diff2)]