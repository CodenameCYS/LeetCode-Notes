'''
=== 3439. Reschedule Meetings for Maximum Free Time I ===

You are given an integer eventTime denoting the duration of an event, where the event occurs from time t = 0 to time t = eventTime.
You are also given two integer arrays startTime and endTime, each of length n. These represent the start and end time of n non-overlapping meetings, where the ith meeting occurs during the time [startTime[i], endTime[i]].
You can reschedule at most k meetings by moving their start time while maintaining the same duration, to maximize the longest continuous period of free time during the event.
The relative order of all the meetings should stay the same and they should remain non-overlapping.
Return the maximum amount of free time possible after rearranging the meetings.
Note that the meetings can not be rescheduled to a time outside the event.

Example 1:
    Input: eventTime = 5, k = 1, startTime = [1,3], endTime = [2,5]
    Output: 2
    Explanation:
    Reschedule the meeting at [1, 2] to [2, 3], leaving no meetings during the time [0, 2].
Example 2:
    Input: eventTime = 10, k = 1, startTime = [0,2,9], endTime = [1,4,10]
    Output: 6
    Explanation:
    Reschedule the meeting at [2, 4] to [1, 3], leaving no meetings during the time [3, 9].
Example 3:
    Input: eventTime = 5, k = 2, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]
    Output: 0
    Explanation:
    There is no time during the event not occupied by meetings.

Constraints:
    1. 1 <= eventTime <= 109
    2. n == startTime.length == endTime.length
    3. 2 <= n <= 105
    4. 1 <= k <= n
    5. 0 <= startTime[i] < endTime[i] <= eventTime
    6. endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
'''
# === 146ms && 45.8MB === #
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        meetings = sorted([(i, j, j-i) for i, j in zip(startTime, endTime)])
        n = len(meetings)
        ans = max(meetings[0][0], eventTime - meetings[-1][1])
        for i in range(n-1):
            ans = max(ans, meetings[i+1][0] - meetings[i][1])
        
        durations = list(accumulate([x[2] for x in meetings], initial=0))
        # print(f"ans = {ans}, meetings = {meetings}, durations = {durations}")
        
        if k == n:
            return eventTime - durations[-1]
        
        for i in range(n-k+1):
            if i == 0:
                tot = meetings[i+k][0]
            elif i+k == n:
                tot = eventTime - meetings[i-1][1]
            else:
                tot = meetings[i+k][0] - meetings[i-1][1]
            d = durations[i+k] - durations[i]
            ans = max(ans, tot-d)
        return ans