'''
=== 3357. Minimize the Maximum Adjacent Element Difference ===

You are given an array of integers nums. Some values in nums are missing and are denoted by -1.
You can choose a pair of positive integers (x, y) exactly once and replace each missing element with either x or y.
You need to minimize the maximum absolute difference between adjacent elements of nums after replacements.
Return the minimum possible difference.

Example 1:
    Input: nums = [1,2,-1,10,8]
    Output: 4
    Explanation:
    By choosing the pair as (6, 7), nums can be changed to [1, 2, 6, 10, 8].
    The absolute differences between adjacent elements are:
    |1 - 2| == 1
    |2 - 6| == 4
    |6 - 10| == 4
    |10 - 8| == 2
Example 2:
    Input: nums = [-1,-1,-1]
    Output: 0
    Explanation:
    By choosing the pair as (4, 4), nums can be changed to [4, 4, 4].
Example 3:
    Input: nums = [-1,10,-1,8]
    Output: 1
    Explanation:
    By choosing the pair as (11, 9), nums can be changed to [11, 10, 9, 8].

Constraints:
    1. 2 <= nums.length <= 105
    2. nums[i] is either -1 or in the range [1, 109].
'''
# === 4481ms && 33.3MB === #
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        def filter_nums(nums):
            ans = []
            cnt = 0
            pre = -1
            for num in nums:
                if num != -1:
                    if num != pre:
                        ans.append(num)
                        cnt = 0
                elif cnt < 2:
                    ans.append(num)
                    cnt += 1
                pre = num
            if len(ans) >= 2 and ans[0] == -1 and ans[1] == -1:
                ans.pop(0)
            if len(ans) >= 2 and ans[-1] == -1 and ans[-2] == -1:
                ans.pop()
            return ans
        
        nums = filter_nums(nums)
        if len(nums) == 1:
            return 0
        # print(nums)
        n = len(nums)
        if Counter(nums)[-1] == 0:
            return max(abs(nums[i] - nums[i+1]) for i in range(n-1))
        
        def is_possible(k):
            ranges = []
            two_gap = []
            for i, x in enumerate(nums):
                if x != -1:
                    if i-1 >= 0 and nums[i-1] != -1 and abs(x - nums[i-1]) > k:
                        return False
                    if i+1 < n and nums[i+1] != -1 and abs(x - nums[i+1]) > k:
                        return False
                if x == -1:
                    _min, _max = 1, math.inf
                    if i-1 >= 0 and nums[i-1] != -1:
                        _min = max(_min, nums[i-1] - k)
                        _max = min(_max, nums[i-1] + k)
                    if i+1 < n and nums[i+1] != -1:
                        _min = max(_min, nums[i+1] - k)
                        _max = min(_max, nums[i+1] + k)
                    if _min > _max:
                        return False
                    ranges.append([_min, _max])
                    if i-1 >= 0 and nums[i-1] == -1:
                        two_gap.append(sorted([nums[i-2], nums[i+1]]))
            ranges = sorted(ranges)
            # print(k, ranges, two_gap)
            
            candidates = []
            _min, _max = ranges[0]
            for l, r in ranges:
                if l > _max:
                    candidates.append([_min, _max])
                    _min, _max = l, r
                    if len(candidates) >= 2:
                        return False
                else:
                    _min = max(_min, l)
                    _max = min(_max, r)
            candidates.append([_min, _max])
            # print(candidates, two_gap)
            for x, y in two_gap:
                if any(y-k <= x+k and (x+k >= l or y-k <= r) for l, r in candidates):
                    continue
                elif len(candidates) == 2 and candidates[0][1] <= x+k and candidates[1][0] >= y-k and candidates[1][0] - candidates[0][1] <= k:
                    continue
                else:
                    return False
            return True
                        
        
        if is_possible(0):
            return 0
        
        i, j = 0, max(nums) - min(nums)
        while j - i > 1:
            m = (i+j) // 2
            if is_possible(m):
                j = m
            else:
                i = m
        # print("=" * 10)
        return j