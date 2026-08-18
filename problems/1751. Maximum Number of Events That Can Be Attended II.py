'''
=== 1751. Maximum Number of Events That Can Be Attended II ===

You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.
You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.
Return the maximum sum of values that you can receive by attending events.

Example 1:
    Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
    Output: 7
    Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:
    Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
    Output: 10
    Explanation: Choose event 2 for a total value of 10.
    Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
Example 3:
    Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
    Output: 9
    Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.

Constraints:
    1. 1 <= k <= events.length
    2. 1 <= k * events.length <= 106
    3. 1 <= startDayi <= endDayi <= 109
    4. 1 <= valuei <= 106
'''
import bisect
# === 876ms(81.30%) && 217.1MB === #
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(events)
        st_list = [x[0] for x in events]
        n = len(events)
        
        @lru_cache(None)
        def dp(idx, k):
            if idx == n:
                return 0
            if k == 0:
                return 0
            ed = events[idx][1]
            nxt = bisect.bisect_left(st_list, ed+1)
            return max(events[idx][2]+dp(nxt, k-1), dp(idx+1, k))
        
        return dp(0, k)