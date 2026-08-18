'''
=== 1815. Maximum Number of Groups Getting Fresh Donuts ===

There is a donuts shop that bakes donuts in batches of batchSize. They have a rule where they must serve all of the donuts of a batch before serving any donuts of the next batch. You are given an integer batchSize and an integer array groups, where groups[i] denotes that there is a group of groups[i] customers that will visit the shop. Each customer will get exactly one donut.
When a group visits the shop, all customers of the group must be served before serving any of the following groups. A group will be happy if they all get fresh donuts. That is, the first customer of the group does not receive a donut that was left over from the previous group.
You can freely rearrange the ordering of the groups. Return the maximum possible number of happy groups after rearranging the groups.

Example 1:
    Input: batchSize = 3, groups = [1,2,3,4,5,6]
    Output: 4
    Explanation: You can arrange the groups as [6,2,4,5,1,3]. Then the 1st, 2nd, 4th, and 6th groups will be happy.
Example 2:
    Input: batchSize = 4, groups = [1,3,2,5,2,2,1,6]
    Output: 4
 
Constraints:
    1. 1 <= batchSize <= 9
    2. 1 <= groups.length <= 30
    3. 1 <= groups[i] <= 109
'''
# === 1200ms(25.69%) && 48.8MB(26.08%) === #
class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        cnt = [0 for _ in range(batchSize)]
        for g in groups:
            cnt[g % batchSize] += 1
            
        @lru_cache(None)
        def dp(status, remain):
            if all(x == 0 for x in status[1:]):
                return 0
            nxt = list(status)
            res = 0
            for i in range(1, batchSize):
                if status[i] == 0:
                    continue
                nxt[i] -= 1
                res = max(res, dp(tuple(nxt), (remain+i)%batchSize))
                nxt[i] += 1
            return res if remain != 0 else res + 1
        
        return cnt[0] + dp(tuple(cnt), 0)
        