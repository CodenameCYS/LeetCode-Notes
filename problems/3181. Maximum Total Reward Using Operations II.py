'''
=== 3181. Maximum Total Reward Using Operations II ===

You are given an integer array rewardValues of length n, representing the values of rewards.
Initially, your total reward x is 0, and all indices are unmarked. You are allowed to perform the following operation any number of times:
    - Choose an unmarked index i from the range [0, n - 1].
    - If rewardValues[i] is greater than your current total reward x, then add rewardValues[i] to x (i.e., x = x + rewardValues[i]), and mark the index i.
Return an integer denoting the maximum total reward you can collect by performing the operations optimally.

Example 1:
    Input: rewardValues = [1,1,3,3]
    Output: 4
    Explanation:
    During the operations, we can choose to mark the indices 0 and 2 in order, and the total reward will be 4, which is the maximum.
Example 2:
    Input: rewardValues = [1,6,4,3,2]
    Output: 11
    Explanation:
    Mark the indices 0, 2, and 1 in order. The total reward will then be 11, which is the maximum.

Constraints:
    1. 1 <= rewardValues.length <= 5 * 104
    2. 1 <= rewardValues[i] <= 5 * 104
'''
# === 716ms && 25.1MB === #
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        prev = [0]
        unseen = [i+1 for i in range(max(rewardValues))]
        
        def in_sorted_list(nums, val):
            idx = bisect.bisect_left(nums, val)
            return idx if idx <= len(nums) and nums[idx] == val else -1
        
        ans = 0
        for reward in rewardValues:
            if reward != rewardValues[-1] - reward-1 and in_sorted_list(rewardValues, rewardValues[-1] - reward-1) != -1:
                return 2*rewardValues[-1]-1
            
            idx = bisect.bisect_left(prev, reward)-1
            ans = max(ans, reward + prev[idx])
            
            i = bisect.bisect_left(unseen, reward)
            while i < len(unseen):
                if unseen[i] >= 2 * reward:
                    break
                k = in_sorted_list(prev, unseen[i]-reward)
                if k == -1:
                    i += 1
                else:
                    bisect.insort(prev, unseen[i])
                    unseen.pop(i)
        return ans