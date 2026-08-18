'''
=== 1787. Make the XOR of All Segments Equal to Zero ===

You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].
Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.

Example 1:
    Input: nums = [1,2,0,3,0], k = 1
    Output: 3
    Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].
Example 2:
    Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
    Output: 3
    Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].
Example 3:
    Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
    Output: 3
    Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].
 
Constraints:
    1. 1 <= k <= nums.length <= 2000
    ​2. ​​​​​0 <= nums[i] < 2^10
'''
# === 5792ms && 343.1MB === #
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        cnt = [defaultdict(int) for _ in range(k)]
        for i, x in enumerate(nums):
            cnt[i % k][x] += 1
            
        def get_max(counter):
            _max = max(counter.values())
            return [x for x in counter if counter[x] == _max]
        
        cand = [get_max(c) for c in cnt]
        tot = sum([c[x[0]] for c, x in zip(cnt, cand)])
        n = len(nums)
        res = n-k+1
        
        @lru_cache(None)
        def dp(i, idx, s):
            nonlocal res
            if i == k:
                if idx != -1:
                    res = min(res, n - (tot - cnt[idx][cand[idx][0]] + cnt[idx][s]))
                    # print(f"update res to {res}")
                return
            if idx == -1:
                dp(i+1, i, s)
            else:
                if n - (tot - cnt[idx][cand[idx][0]]) >= res:
                    return
            for c in cand[i]:
                dp(i+1, idx, s^c)
            return
        
        dp(0, -1, 0)
        return res