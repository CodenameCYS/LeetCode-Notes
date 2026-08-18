'''
=== 3164. Find the Number of Good Pairs II ===

You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.
A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).
Return the total number of good pairs.

Example 1:
    Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1
    Output: 5
    Explanation:
    The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
Example 2:
    Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3
    Output: 2
    Explanation:
    The 2 good pairs are (3, 0) and (3, 1).

Constraints:
    1. 1 <= n, m <= 105
    2. 1 <= nums1[i], nums2[j] <= 106
    3. 1 <= k <= 103
'''
# === 4433ms && 44.3MB === #
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = Counter(nums2)
        
        @lru_cache(None)
        def count(n):
            k = int(sqrt(n))
            status = [0 for _ in range(k+1)]
            ans = cnt[1] + cnt[n] if n != 1 else cnt[1]
            for i in range(2, k+1):
                if status[i] == 1:
                    continue
                if n % i != 0:
                    for j in range(i, k+1, i):
                        status[j] = 1
                else:
                    if n == i*i:
                        ans += cnt[i]
                    else:
                        ans += cnt[i] + cnt[n//i]
            return ans
        
        return sum([0 if num % k != 0 else count(num // k) for num in nums1])
            