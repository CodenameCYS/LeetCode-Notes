'''
=== 3287. Find the Maximum Sequence Value of Array ===

You are given an integer array nums and a positive integer k.
The value of a sequence seq of size 2 * x is defined as:
    - (seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1]).
Return the maximum value of any subsequence of nums having size 2 * k.

Example 1:
    Input: nums = [2,6,7], k = 1
    Output: 5
    Explanation:
    The subsequence [2, 7] has the maximum value of 2 XOR 7 = 5.
Example 2:
    Input: nums = [4,2,5,6,7], k = 2
    Output: 2
    Explanation:
    The subsequence [4, 5, 6, 7] has the maximum value of (4 OR 5) XOR (6 OR 7) = 2.

Constraints:
    1. 2 <= nums.length <= 400
    2. 1 <= nums[i] < 27
    3. 1 <= k <= nums.length / 2
'''
# === 11887ms && 547.7MB === #
class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prefix = defaultdict(lambda: defaultdict(set))
        for i in range(n):
            for j in range(1, k+1):
                prefix[i][j] = deepcopy(prefix[i-1][j])
                if j == 1:
                    prefix[i][j].add(nums[i])
                else:
                    for elem in prefix[i-1][j-1]:
                        prefix[i][j].add(elem | nums[i])
        # print(f"prefix: {prefix}")
        
        suffix = defaultdict(lambda: defaultdict(set))
        for i in range(n-1, -1, -1):
            for j in range(1, k+1):
                suffix[i][j] = deepcopy(suffix[i+1][j])
                if j == 1:
                    suffix[i][j].add(nums[i])
                else:
                    for elem in suffix[i+1][j-1]:
                        suffix[i][j].add(elem | nums[i])
        # print(f"suffix: {suffix}")
                        
        ans = 0
        for i in range(k-1, n-k):
            for left in prefix[i][k]:
                for right in suffix[i+1][k]:
                    ans = max(ans, left^right)
        return ans