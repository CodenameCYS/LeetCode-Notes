'''
=== 1589. Maximum Sum Obtained of Any Permutation ===

We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.
Return the maximum total sum of all requests among all permutations of nums.
Since the answer may be too large, return it modulo 109 + 7.

Example 1:
    Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
    Output: 19
    Explanation: One permutation of nums is [2,1,3,4,5] with the following result: 
    requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
    requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
    Total sum: 8 + 3 = 11.
    A permutation with a higher total sum is [3,5,4,2,1] with the following result:
    requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
    requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
    Total sum: 11 + 8 = 19, which is the best that you can do.
Example 2:
    Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
    Output: 11
    Explanation: A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].
Example 3:
    Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
    Output: 47
    Explanation: A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].
 
Constraints:
    1. n == nums.length
    2. 1 <= n <= 105
    3. 0 <= nums[i] <= 105
    4. 1 <= requests.length <= 105
    5. requests[i].length == 2
    6. 0 <= starti <= endi < n
'''
# === 1664ms && 46.9MB === #
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 1000000007
        # requests = sorted(requests)
        n = len(nums)
        counter = [0 for i in range(n+1)]
        for st, ed in requests:
            counter[st] += 1
            counter[ed+1] -= 1
        for i in range(1, n+1):
            counter[i] += counter[i-1]
        counter = sorted(counter[:-1])
        nums = sorted(nums)
        ans = 0
        for i in range(n):
            ans = (ans + counter[i] * nums[i]) % MOD
        return ans
        