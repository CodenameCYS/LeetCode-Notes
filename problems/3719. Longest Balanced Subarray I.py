'''
=== 3719. Longest Balanced Subarray I ===

You are given an integer array nums.
A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.
Return the length of the longest balanced subarray.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [2,5,4,3]
    Output: 4
    Explanation:
    The longest balanced subarray is [2, 5, 4, 3].
    It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
Example 2:
    Input: nums = [3,2,2,5,4]
    Output: 5
    Explanation:
    The longest balanced subarray is [3, 2, 2, 5, 4].
    It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
Example 3:
    Input: nums = [1,2,3,2]
    Output: 3
    Explanation:
    The longest balanced subarray is [2, 3, 2].
    It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.

Constraints:
    1. 1 <= nums.length <= 1500
    2. 1 <= nums[i] <= 105
'''
# === 1303ms && 18.25MB === #
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        odd, even = defaultdict(int), defaultdict(int)
        for num in nums:
            if num % 2 == 0:
                even[num] += 1
            else:
                odd[num] += 1
        ans = 0
        for i in range(n):
            if n-i <= ans:
                break
            _odd, _even = deepcopy(odd), deepcopy(even)
            for j in range(n-1, i, -1):
                if j+1 - i <= ans:
                    break
                if len(_odd) == len(_even):
                    ans = j+1-i
                    break
                if nums[j] % 2 == 0:
                    _even[nums[j]] -= 1
                    if _even[nums[j]] == 0:
                        _even.pop(nums[j])
                else:
                    _odd[nums[j]] -= 1
                    if _odd[nums[j]] == 0:
                        _odd.pop(nums[j])
            if nums[i] % 2 == 0:
                even[nums[i]] -= 1
                if even[nums[i]] == 0:
                    even.pop(nums[i])
            else:
                odd[nums[i]] -= 1
                if odd[nums[i]] == 0:
                    odd.pop(nums[i])
        return ans