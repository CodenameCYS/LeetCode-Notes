'''
=== 2023. Number of Pairs of Strings With Concatenation Equal to Target ===

Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.

Example 1:
    Input: nums = ["777","7","77","77"], target = "7777"
    Output: 4
    Explanation: Valid pairs are:
    - (0, 1): "777" + "7"
    - (1, 0): "7" + "777"
    - (2, 3): "77" + "77"
    - (3, 2): "77" + "77"
Example 2:
    Input: nums = ["123","4","12","34"], target = "1234"
    Output: 2
    Explanation: Valid pairs are:
    - (0, 1): "123" + "4"
    - (2, 3): "12" + "34"
Example 3:
    Input: nums = ["1","1","1"], target = "11"
    Output: 6
    Explanation: Valid pairs are:
    - (0, 1): "1" + "1"
    - (1, 0): "1" + "1"
    - (0, 2): "1" + "1"
    - (2, 0): "1" + "1"
    - (1, 2): "1" + "1"
    - (2, 1): "1" + "1"
 
Constraints:
    1. 2 <= nums.length <= 100
    2. 1 <= nums[i].length <= 100
    3. 2 <= target.length <= 100
    4. nums[i] and target consist of digits.
    5. nums[i] and target do not have leading zeros.
'''
# === 40ms && 14.2MB === #
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = Counter(nums)
        res = 0
        for s1 in cnt:
            if not target.startswith(s1):
                continue
            s2 = target[len(s1):]
            if s1 != s2:
                res += cnt[s1] * cnt[s2]
            else:
                res += cnt[s1] * (cnt[s1]-1)
        return res
        