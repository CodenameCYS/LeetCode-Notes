'''
=== 3948. Lexicographically Maximum MEX Array ===

You are given an integer array nums.
You want to construct an array result by repeatedly performing the following operation until nums becomes empty:
    - Choose an integer k such that 1 <= k <= len(nums).
    - Compute the MEX of the first k elements of nums.
    - Append this MEX to result.
    - Remove the first k elements from nums.
Return the lexicographically maximum array result that can be obtained after performing the operations.
The MEX of an array is the smallest non-negative integer not present in the array.
An array a is lexicographically greater than an array b if in the first position where a and b differ, array a has an element that is greater than the corresponding element in b. If the first min(a.length, b.length) elements do not differ, then the longer array is the lexicographically greater one.

Example 1:
    Input: nums = [0,1,0]
    Output: [2,1]
    Explanation:
    Take the first k = 2 elements [0, 1] which has MEX = 2. Current result = [2].
    Remaining array [0] has MEX = 1. Thus, the final result = [2, 1].
Example 2:
    Input: nums = [1,0,2]
    Output: [3]
    Explanation:
    Take the first k = 3 elements [1, 0, 2] which has MEX = 3.
    nums is now empty. Thus, the final result = [3].
Example 3:
    Input: nums = [3,1]
    Output: [0,0]
    Explanation:​​​​​​​
    Take k = 1, first element [3] has MEX = 0. Current result = [0].
    Remaining array [1] has MEX = 0. Thus, the final result = [0, 0].
 
Constraints:
    1. 1 <= nums.length <= 105
    2. 0 <= nums[i] <= 105
'''
# === 7856ms && 30.27MB === #
class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = Counter(nums)

        idx = 0
        ans = []
        while idx < n:
            # cnt = Counter(nums[idx:])
            for i in range(n-idx+1):
                if cnt[i] == 0:
                    tgt = i
                    break
            if tgt == 0:
                ans.append(0)
                cnt[nums[idx]] -= 1
                idx += 1
                continue
            elif tgt == n-idx:
                ans.append(tgt)
                break
            # print(idx, tgt)
            
            status = [0 for _ in range(tgt)]
            _cnt = 0
            nxt = -1
            for i, x in enumerate(nums[idx:]):
                if _cnt == tgt:
                    ans.append(tgt)
                    nxt = idx + i
                    break
                if x < tgt:
                    _cnt += 1-status[x]
                    status[x] = 1
            # print(nxt, _cnt, status)
            if nxt == -1:
                ans.append(tgt)
                break
            for i in range(idx, nxt):
                cnt[nums[i]] -= 1
            idx = nxt
        return ans
        