'''
=== 3962. Maximum Subarray Sum After at Most K Swaps ===

You are given an integer array nums and an integer k.
You are allowed to perform at most k swap operations on the array.
In one swap operation, you may choose any two indices i and j and swap nums[i] and nums[j].
Return an integer denoting the maximum possible subarray sum after performing the swaps.

Example 1:
    Input: nums = [1,-1,0,2], k = 1
    Output: 3
    Explanation:
    We can swap on indices 1 and 3, resulting in the array [1, 2, 0, -1].
    The subarray [1, 2] has a sum of 3, which is the maximum possible subarray sum after at most k = 1​​​​​​​ swap.
Example 2:
    Input: nums = [4,3,2,4], k = 2
    Output: 13
    Explanation:
    The maximum possible subarray sum after at most k = 2 swaps is the sum of the entire array, which is 13.
Example 3:
    Input: nums = [-1,-2], k = 0
    Output: -1
    Explanation:
    k = 0 swaps are allowed.
    The possible subarrays are [-1], [-2], and [-1, -2], with sums -1, -2, and -3 respectively.
    Among these sums, the maximum is -1.
 
Constraints:
    1. 1 <= nums.length <= 1500
    2. -105 <= nums[i] <= 105
    3. 0 <= k <= nums.length
'''
# === 257ms && 19.79MB === #
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        positive = sorted([x for x in nums if x > 0], reverse=True)
        if len(positive) == 0:
            return max(nums)
        elif len(positive) <= k:
            return sum(positive)

        while nums[0] <= 0:
            nums.pop(0)
        while nums[-1] <= 0:
            nums.pop()
        n = len(nums)

        negative = sorted([x for x in nums if x < 0])
        if len(negative) <= k:
            return sum(positive)

        ans = -math.inf
        for l in range(k+1, n+1):
            i, j = 0, l
            tot = sum(nums[i:j])
            candi = sorted([x for x in nums[j:] if x > 0])
            negs = sorted([x for x in nums[i:j] if x <= 0])
            m = min(k, len(negs), len(candi))
            if m > 0:
                ans = max(ans, tot - sum([0] + negs[:m]) + sum([0] + candi[-m:]))
            else:
                ans = max(ans, tot)
            # print(l, ans, tot, candi, negs, m)
            while j < n:
                tot = tot - nums[i] + nums[j]
                print(i, j, nums[i], nums[j], candi, negs)
                if nums[j] > 0:
                    candi.pop(bisect.bisect_left(candi, nums[j]))
                else:
                    bisect.insort(negs, nums[j])
                if nums[i] <= 0:
                    negs.pop(bisect.bisect_left(negs, nums[i]))
                else:
                    bisect.insort(candi, nums[i])
                m = min(k, len(negs), len(candi))
                if m > 0:
                    ans = max(ans, tot - sum([0] + negs[:m]) + sum([0] + candi[-m:]))
                else:
                    ans = max(ans, tot)
                i += 1
                j += 1
                    
        return ans

