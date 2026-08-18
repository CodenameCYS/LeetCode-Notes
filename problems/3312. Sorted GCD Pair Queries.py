'''
=== 3312. Sorted GCD Pair Queries ===

You are given an integer array nums of length n and an integer array queries.
Let gcdPairs denote an array obtained by calculating the GCD of all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these values in ascending order.
For each query queries[i], you need to find the element at index queries[i] in gcdPairs.
Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.
The term gcd(a, b) denotes the greatest common divisor of a and b.

Example 1:
    Input: nums = [2,3,4], queries = [0,2,2]
    Output: [1,2,2]
    Explanation:
    gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1].
    After sorting in ascending order, gcdPairs = [1, 1, 2].
    So, the answer is [gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2].
Example 2:
    Input: nums = [4,4,2,1], queries = [5,3,1,0]
    Output: [4,2,1,1]
    Explanation:
    gcdPairs sorted in ascending order is [1, 1, 1, 2, 2, 4].
Example 3:
    Input: nums = [2,2], queries = [0,0]
    Output: [2,2]
    Explanation:
    gcdPairs = [2].

Constraints:
    1. 2 <= n == nums.length <= 105
    2. 1 <= nums[i] <= 5 * 104
    3. 1 <= queries.length <= 105
    4. 0 <= queries[i] < n * (n - 1) / 2
'''
# === 1627ms && 42.2MB === #
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        cnt = Counter(nums)
        nums = sorted(cnt.keys())
        m = max(nums)
        s = [0 for _ in range(m+1)]
        
        for i in range(m,0,-1):
            vc = sum(cnt[x] for x in range(i,m+1,i))
            vc = vc*(vc-1)//2 - sum(s[x] for x in range(i,m+1,i))
            s[i]=vc
        s = list(accumulate(s))
        
        # n = len(nums)
        # for i in range(n):
        #     x = nums[i]
        #     s[x] += cnt[x] * (cnt[x]-1) // 2
        #     for j in range(i+1, n):
        #         y = nums[j]
        #         c = gcd(x, y)
        #         s[c] += cnt[x] * cnt[y]
        # # print(s)
        # s = list(accumulate(s))
        # print(s)
        return [bisect.bisect_right(s, q) for q in queries]