'''
=== 3440. Reschedule Meetings for Maximum Free Time II ===

You are given an integer eventTime denoting the duration of an event. You are also given two integer arrays startTime and endTime, each of length n.
These represent the start and end times of n non-overlapping meetings that occur during the event between time t = 0 and time t = eventTime, where the ith meeting occurs during the time [startTime[i], endTime[i]].
You can reschedule at most one meeting by moving its start time while maintaining the same duration, such that the meetings remain non-overlapping, to maximize the longest continuous period of free time during the event.
Return the maximum amount of free time possible after rearranging the meetings.
Note that the meetings can not be rescheduled to a time outside the event and they should remain non-overlapping.
Note: In this version, it is valid for the relative ordering of the meetings to change after rescheduling one meeting.

Example 1:
    Input: eventTime = 5, startTime = [1,3], endTime = [2,5]
    Output: 2
    Explanation:
    Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].
Example 2:
    Input: eventTime = 10, startTime = [0,7,9], endTime = [1,8,10]
    Output: 7
    Explanation:
    Reschedule the meeting at [0, 1] to [8, 9], leaving no meetings during the time [0, 7].
Example 3:
    Input: eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]
    Output: 6
    Explanation:
    Reschedule the meeting at [3, 4] to [8, 9], leaving no meetings during the time [1, 7].
Example 4:
    Input: eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
    Output: 0
    Explanation:
    There is no time during the event not occupied by meetings.

Constraints:
    1. 1 <= eventTime <= 109
    2. n == startTime.length == endTime.length
    3. 2 <= n <= 105
    4. 0 <= startTime[i] < endTime[i] <= eventTime
    5. endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
'''
class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = self.build(arr)

    def feature_func(self, *args):
        return max(args)

    def build(self, arr):
        n = len(arr)
        tree = [0 for _ in range(2*n)]
        for i in range(n):
            tree[i+n] = arr[i]
        for i in range(n-1, 0, -1):
            tree[i] = self.feature_func(tree[i<<1], tree[(i<<1) | 1])
        return tree

    def update(self, idx, val):
        idx = idx + self.length
        self.tree[idx] = val
        while idx > 1:
            self.tree[idx>>1] = self.feature_func(self.tree[idx], self.tree[idx ^ 1])
            idx = idx>>1
        return

    def query(self, lb, rb):
        if rb < lb:
            return 0
        lb += self.length 
        rb += self.length
        nodes = []
        while lb < rb:
            if lb & 1 == 1:
                nodes.append(self.tree[lb])
                lb += 1
            if rb & 1 == 0:
                nodes.append(self.tree[rb])
                rb -= 1
            lb = lb >> 1
            rb = rb >> 1
        if lb == rb:
            nodes.append(self.tree[rb])
        return self.feature_func(*nodes)
# === 2361ms && 51.1MB === #
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        meetings = [(i, j, j-i) for i, j in zip(startTime, endTime)]
        n = len(meetings)
        freeTimes = [meetings[0][0]] + [meetings[i+1][0] - meetings[i][1] for i in range(n-1)] + [eventTime - meetings[-1][1]]
        ans = max(freeTimes)
        segment_tree = SegmentTree(freeTimes)
        
        durations = list(accumulate([x[2] for x in meetings], initial=0))
        # print(f"ans = {ans}, meetings = {meetings}, durations = {durations}")
        
        for i in range(n):
            if i == 0:
                tot = meetings[i+1][0]
            elif i+1 == n:
                tot = eventTime - meetings[i-1][1]
            else:
                tot = meetings[i+1][0] - meetings[i-1][1]
            d = durations[i+1] - durations[i]
            gap = max(segment_tree.query(0, i-1), segment_tree.query(i+2, n))
            # print(f"i={i}, tot={tot}, duration={d}, gap={gap}")
            if d > gap:
                ans = max(ans, tot-d)
            else:
                ans = max(ans, tot)
        # print("=" * 10)
        return ans