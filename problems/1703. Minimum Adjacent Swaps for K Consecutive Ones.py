'''
=== 1703. Minimum Adjacent Swaps for K Consecutive Ones ===

You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.
Return the minimum number of moves required so that nums has k consecutive 1's.

Example 1:
    Input: nums = [1,0,0,1,0,1], k = 2
    Output: 1
    Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.
Example 2:
    Input: nums = [1,0,0,0,0,0,1,1], k = 3
    Output: 5
    Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].
Example 3:
    Input: nums = [1,1,0,1], k = 2
    Output: 0
    Explanation: nums already has 2 consecutive 1's.
 
Constraints:
    1. 1 <= nums.length <= 105
    2. nums[i] is 0 or 1.
    3. 1 <= k <= sum(nums)
'''
# === 1356ms && 25.5MB === #
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = [idx for idx, i in enumerate(nums) if i == 1]
        cumsum = [0] + list(accumulate(ones))
        # print(ones)
        # print(cumsum)
        
        def cal_delta(k):
            t1 = k // 2
            t2 = k-1-t1
            return t1*(t1+1) // 2 + t2*(t2+1) // 2
        
        n = len(ones)
        delta = cal_delta(k)
        # print(delta)
        idx = 0
        res = math.inf
        while idx + k <= n:
            mid = idx+(k-1)//2
            dis = (cumsum[idx+k] - cumsum[mid+1]) - (cumsum[mid] - cumsum[idx]) - delta
            dis = dis if k % 2 == 1 else dis - ones[mid]
            res = min(dis, res)
            idx += 1
            # print(idx, mid, dis, res)
            # print("=" * 10)
        # print("=" * 20)
        return res
            
        