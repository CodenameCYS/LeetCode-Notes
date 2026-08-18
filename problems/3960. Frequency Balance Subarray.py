'''
=== 3960. Frequency Balance Subarray ===

You are given an integer array ​​​​​​​nums.
Define a frequency balance subarray as follows:
    - If the subarray contains only one distinct value, it is frequency balanced.
    - Otherwise, there must exist a positive integer f such that every distinct value in the subarray occurs either f or 2 * f times, and both frequencies occur among the distinct values.
Return an integer denoting the length of the longest frequency balance subarray.

Example 1:
    Input: nums = [1,2,2,1,2,3,3,3]
    Output: 5
    Explanation:
    The longest frequency balance subarray is [2, 1, 2, 3, 3].
    The elements that appear most frequently are 2 and 3, both appearing twice.
    The remaining element 1 appears once, meeting the requirements.
Example 2:
    Input: nums = [5,5,5,5]
    Output: 4
    Explanation:
    The longest frequency balance subarray is [5, 5, 5, 5].
    The element that appears most frequently is 5.
    There are no other elements meeting the requirements.
Example 3:
    Input: nums = [1,2,3,4]
    Output: 1
    Explanation:
    Since all elements appear only once, the length of the longest frequency balance subarray is 1.

Constraints:
    1. 1 <= nums.length <= 10​​​​​​​3
    2. 1 <= nums[i] <= 10​​​​​​​9
'''
# === 312ms && 19.50MB === #
class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter(nums)
        if max(cnt.values()) == 1:
            return 1

        def is_balanced(cnt):
            if len(cnt) == 1:
                return True
            m = max(cnt.values())
            if m % 2 == 1:
                return False
            return any(x == m // 2 for x in cnt.values()) and all(x == m or x == m // 2 for x in cnt.values())
            

        ans = 1
        for i in range(n-1):
            if n-i <= ans:
                break
            _cnt = deepcopy(cnt)
            for j in range(n-1, i, -1):
                if j-i+1 <= ans:
                    break
                _max = max(_cnt.values())
                if _max == 1:
                    break
                if is_balanced(_cnt):
                    ans = j-i+1
                    break
                _cnt[nums[j]] -= 1
                if _cnt[nums[j]] == 0:
                    _cnt.pop(nums[j])
            cnt[nums[i]] -= 1
            if cnt[nums[i]] == 0:
                cnt.pop(nums[i])
        return ans