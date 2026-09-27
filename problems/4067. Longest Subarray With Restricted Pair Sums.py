'''
=== 4067. Longest Subarray With Restricted Pair Sums ===

You are given an integer array nums.
A subarray nums[l..r] is valid if there are no three distinct indices i, j, and k such that l <= i, j, k <= r and:
    - nums[i] + nums[j] == nums[k]
Return the maximum length of a valid subarray of nums.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input: nums = [2,3,5,3,2,1]
    Output: 3
    Explanation:
    Consider the subarray [3, 5, 3]. The pairs of elements at distinct indices have the following sums:
    3 + 5 = 8
    3 + 3 = 6, using the two different occurrences of 3
    5 + 3 = 8
    None of these sums is an element at the remaining index, so the subarray is valid.
    Every subarray of length 4 contains 2, 3, and 5 at distinct indices, where 2 + 3 = 5. Therefore, no longer valid subarray exists, and the answer is 3.
Example 2:
    Input: nums = [3,4,5,6]
    Output: 4
    Explanation:
    The sums obtained from every pair of elements at distinct indices are 7, 8, 9, 9, 10, and 11. None of these values appears at the remaining index, so the entire array is valid.

Constraints:
    1. 1 <= nums.length <= 1000
    2. 1 <= nums[i] <= 500
'''
# === 9323ms && 58.43MB === #
class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        elems = sorted([(num, i) for i, num in enumerate(nums)])
        pairs = defaultdict(list)
        forbidden = {}
        for i in range(1, n):
            z = elems[i][1]
            for x, y in pairs[elems[i][0]]:
                # print(x, y, z)
                st, ed = min(x, y, z), max(x, y, z)
                if ed in forbidden:
                    forbidden[ed] = max(forbidden[ed], st)
                else:
                    forbidden[ed] = st
            for j in range(i):
                pairs[elems[i][0] + elems[j][0]].append((elems[i][1], elems[j][1]))
        # print(forbidden)
        
        i, j = 0, 0
        ans = 0
        while j < n:
            while i < j and i <= forbidden.get(j, -1):
                i += 1
            ans = max(ans, j-i+1)
            j += 1
        return ans