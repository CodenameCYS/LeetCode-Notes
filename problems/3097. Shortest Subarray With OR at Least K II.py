'''
=== 3097. Shortest Subarray With OR at Least K II ===

You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

Example 1:
    Input: nums = [1,2,3], k = 2
    Output: 1
    Explanation:
    The subarray [3] has OR value of 3. Hence, we return 1.
Example 2:
    Input: nums = [2,1,8], k = 10
    Output: 3
    Explanation:
    The subarray [2,1,8] has OR value of 11. Hence, we return 3.
Example 3:
    Input: nums = [1,2], k = 0
    Output: 1
    Explanation:
    The subarray [1] has OR value of 1. Hence, we return 1.

Constraints:
    1. 1 <= nums.length <= 2 * 105
    2. 0 <= nums[i] <= 109
    3. 0 <= k <= 109
'''
# === 3221ms && 38MB === #
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        def num2digit(num):
            ret = [0 for _ in range(32)]
            idx = 31
            while num > 0:
                ret[idx] = num % 2
                num = num // 2
                idx -= 1
            return ret
        
        def is_greater(digit1, digit2):
            for i in range(32):
                if digit1[i] > 0 and digit2[i] == 0:
                    return True
                elif digit1[i] == 0 and digit2[i] > 0:
                    return False
            return True
        
        i, j, n = 0, 0, len(nums)
        ans = n+1
        dk = num2digit(k)
        digit = [0 for _ in range(32)]
        while i < n:
            while j < n and (j ==i or not is_greater(digit, dk)):
                dj = num2digit(nums[j])
                digit = [x+y for x, y in zip(digit, dj)]
                j += 1
            if is_greater(digit, dk):
                ans = min(ans, j-i)
            else:
                break
            # print(f"i={i}, j={j}, digit={digit}, k={dk}")
            di = num2digit(nums[i])
            digit = [x-y for x, y in zip(digit, di)]
            i += 1
        # print("=" * 10)
        return ans if ans != n+1 else -1
                
                