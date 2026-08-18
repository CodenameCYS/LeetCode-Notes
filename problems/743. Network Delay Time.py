'''
=== 743. Network Delay Time ===

There are N network nodes, labelled 1 to N.
Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example 1:
    Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
    Output: 2
 
Note:
    1. N will be in the range [1, 100].
    2. K will be in the range [1, N].
    3. The length of times will be in the range [1, 6000].
    4. All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
'''
# === 520ms(50.03%) && 14.8MB(46.15%) === #
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        link = {i:[] for i in range(1, N+1)}
        for it in times:
            st, ed, time = it
            link[st].append((ed, time))
        
        delay_time = [0 if i==K or i==0 else -1 for i in range(N+1)]
        stack = [K]
        while stack != []:
            node = stack.pop(0)
            for nd, time in link.get(node, []):
                if delay_time[nd] == -1 or delay_time[nd] > delay_time[node] + time:
                    delay_time[nd] = delay_time[node] + time
                    stack.append(nd)
        if any(time == -1 for time in delay_time):
            return -1
        else:
            return max(delay_time)