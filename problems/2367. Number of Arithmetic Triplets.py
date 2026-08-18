'''
=== 2367. Number of Arithmetic Triplets ===

You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
    - i < j < k,
    - nums[j] - nums[i] == diff, and
    - nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.

Example 1:
    Input: nums = [0,1,4,6,7,10], diff = 3
    Output: 2
    Explanation:
    (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
    (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
Example 2:
    Input: nums = [4,5,6,7,8,9], diff = 2
    Output: 2
    Explanation:
    (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
    (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
 
Constraints:
    1. 3 <= nums.length <= 200
    2. 0 <= nums[i] <= 200
    3. 1 <= diff <= 50
    4. nums is strictly increasing.
'''
# === 84ms && 13.9MB === #
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        res = 0
        status = [0 for _ in range(n)]
        for i in range(n):
            if status[i] != 0:
                continue
            pre, cnt = nums[i], 1
            status[i] = 1
            for j in range(i+1, n):
                if nums[j] == pre + diff:
                    cnt += 1
                    pre = nums[j]
                    status[j] = 1
            res += max(0, cnt-2)
        return res