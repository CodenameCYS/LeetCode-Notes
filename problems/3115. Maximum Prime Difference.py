'''
=== 3115. Maximum Prime Difference ===

You are given an integer array nums.
Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.

Example 1:
    Input: nums = [4,2,9,5,3]
    Output: 3
    Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.
Example 2:
    Input: nums = [4,8,2,8]
    Output: 0
    Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.

Constraints:
    1. 1 <= nums.length <= 3 * 105
    2. 1 <= nums[i] <= 100
    3. The input is generated such that the number of prime numbers in the nums is at least one.
'''
# === 744ms && 26.8MB === #
PRIMES = set()
status = [0 for _ in range(100)]
for i in range(2, 100):
    if status[i] != 0:
        continue
    status[i] = 1
    PRIMES.add(i)
    for j in range(i, 100, i):
        status[j] = 1
        

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        lb, rb = -1, -1
        for i, x in enumerate(nums):
            if x in PRIMES:
                if lb == -1:
                    lb = i
                rb = i
        return rb-lb