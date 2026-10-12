'''
=== 4076. Longest Resilient Subarray II ===

You are given an integer array nums and an integer k.
A subarray is resilient if, for every position in it, deleting the element at that position leaves the remaining elements with a sum divisible by k.
For a subarray of length 1, the remaining sum is 0, which is divisible by k.
Return the length of the longest resilient subarray.

Example 1:
    Input: nums = [2,4,6,3], k = 2
    Output: 3
    Explanation:
    The subarray [2, 4, 6] sums to 12. Deleting 2, 4, or 6 leaves a sum of 10, 8, or 6, respectively, each of which is divisible by 2. Therefore, the answer is 3.
Example 2:
    Input: nums = [1,4,7,1], k = 3
    Output: 4
    Explanation:
    The subarray [1, 4, 7, 1] sums to 13. Deleting the first 1, the 4, the 7, or the last 1 leaves a sum of 12, 9, 6, or 12, respectively, each of which is divisible by 3. Therefore, the answer is 4.
Example 3:
    Input: nums = [5,5,4,8], k = 4
    Output: 2
    Explanation:
    The subarray [5, 5] is not resilient, since deleting either 5 leaves a sum of 5, which is not divisible by 4.
    The subarray [4, 8] sums to 12. Deleting 4 or 8 leaves a sum of 8 or 4, respectively, each of which is divisible by 4. Therefore, the answer is 2.

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 105
    3. 1 <= k <= 105
'''
# === 134ms && 31.64MB === #
class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        arr = [x % k for x in nums]
        pre, cnt = 0, 0
        ans = 0
        for r in arr:
            if r != pre and cnt != 0:
                if pre == 0:
                    ans = max(ans, cnt)
                else:
                    m = lcm(pre, k)
                    t = m // pre
                    ans = max(ans, ((cnt-1) // t) * t + 1)
                cnt = 0
            pre = r
            cnt += 1
            # print(pre, cnt, ans)
        if pre == 0:
            ans = max(ans, cnt)
        else:
            m = lcm(r, k)
            t = m // r
            ans = max(ans, ((cnt-1) // t) * t + 1)
        return ans
                