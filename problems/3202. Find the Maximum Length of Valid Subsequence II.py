'''
=== 3202. Find the Maximum Length of Valid Subsequence II ===

You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:
    - (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.
 
Example 1:
    Input: nums = [1,2,3,4,5], k = 2
    Output: 5
    Explanation:
    The longest valid subsequence is [1, 2, 3, 4, 5].
Example 2:
    Input: nums = [1,4,2,3,1,4], k = 3
    Output: 4
    Explanation:
    The longest valid subsequence is [1, 4, 1, 4].

Constraints:
    1. 2 <= nums.length <= 103
    2. 1 <= nums[i] <= 107
    3. 1 <= k <= 103
'''
# === 275ms && 16.9MB === #
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        locs = defaultdict(list)
        for i, x in enumerate(nums):
            locs[x%k].append(i)
        ans = max(len(x) for x in locs.values())
        for i in range(k-1):
            if locs[i] == []:
                continue
            for j in range(i+1, k):
                if len(locs[i]) + len(locs[j]) <= ans:
                    continue
                s1, s2 = locs[i], locs[j]
                n, m = len(s1), len(s2)
                a, b = 0, 0
                cnt = 1 if s2[0] < s1[0] else 0
                while a < n:
                    cnt += 1
                    b = bisect.bisect_left(s2, s1[a])
                    if b < m:
                        cnt += 1
                    else:
                        break
                    a = bisect.bisect_left(s1, s2[b])
                # print(s1, s2, cnt)
                ans = max(ans, cnt)
        # print("=" * 10)
        return ans
    
# === 277ms && 16.8MB === #
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        locs = defaultdict(list)
        for i, x in enumerate(nums):
            locs[x%k].append(i)
        ans = max(len(x) for x in locs.values())
        
        def get_max_length(s1, s2):
            n, m = len(s1), len(s2)
            i, j = 0, 0
            cnt = 1 if s2[0] < s1[0] else 0
            while i < n:
                cnt += 1
                j = bisect.bisect_left(s2, s1[i])
                if j < m:
                    cnt += 1
                else:
                    break
                i = bisect.bisect_left(s1, s2[j])
            return cnt
        
        for i in range(k-1):
            if locs[i] == []:
                continue
            for j in range(i+1, k):
                if len(locs[i]) + len(locs[j]) <= ans:
                    continue
                cnt = get_max_length(locs[i], locs[j])
                ans = max(ans, cnt)
        # print("=" * 10)
        return ans