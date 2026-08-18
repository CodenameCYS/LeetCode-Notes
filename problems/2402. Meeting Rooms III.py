'''
=== 2402. Meeting Rooms III ===

You are given an integer n. There are n rooms numbered from 0 to n - 1.
You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.
Meetings are allocated to rooms in the following manner:
    1. Each meeting will take place in the unused room with the lowest number.
    2. If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
    3. When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.
A half-closed interval [a, b) is the interval between a and b including a and not including b.

Example 1:
    Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
    Output: 0
    Explanation:
    - At time 0, both rooms are not being used. The first meeting starts in room 0.
    - At time 1, only room 1 is not being used. The second meeting starts in room 1.
    - At time 2, both rooms are being used. The third meeting is delayed.
    - At time 3, both rooms are being used. The fourth meeting is delayed.
    - At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
    - At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
    Both rooms 0 and 1 held 2 meetings, so we return 0. 
Example 2:
    Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    Output: 1
    Explanation:
    - At time 1, all three rooms are not being used. The first meeting starts in room 0.
    - At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
    - At time 3, only room 2 is not being used. The third meeting starts in room 2.
    - At time 4, all three rooms are being used. The fourth meeting is delayed.
    - At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
    - At time 6, all three rooms are being used. The fifth meeting is delayed.
    - At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
    Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 
 
Constraints:
    1. 1 <= n <= 100
    2. 1 <= meetings.length <= 105
    3. meetings[i].length == 2
    4. 0 <= starti < endi <= 5 * 105
    5. All the values of starti are unique.
'''
# === 4237ms && 60.4MB === #
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted([(st, i, ed) for i, (st, ed) in enumerate(meetings)])
        # print(meetings)
        avail = [(0, i) for i in range(n)]
        cnt = [0 for _ in range(n)]
        for st, _, ed in meetings:
            t, idx = heapq.heappop(avail)
            while t < st:
                t = st
                heapq.heappush(avail, (t, idx))
                t, idx = heapq.heappop(avail)
            cnt[idx] += 1
            heapq.heappush(avail, (max(t, st) + ed-st, idx))
        #     print(avail, cnt)
        # print("=" * 10)
        _max = max(cnt)
        for i in range(n):
            if cnt[i] == _max:
                return i
        return -1

# === 2596ms && 60.5MB === #
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings = sorted([(st, i, ed) for i, (st, ed) in enumerate(meetings)])
        busy = []
        avail = [i for i in range(n)]
        heapq.heapify(avail)
        cnt = [0 for _ in range(n)]
        for st, _, ed in meetings:
            while busy != [] and busy[0][0] <= st:
                t, idx = heapq.heappop(busy)
                heapq.heappush(avail, idx)
            if avail:
                idx = heapq.heappop(avail)
                heapq.heappush(busy, (ed, idx))
            else:
                t, idx = heapq.heappop(busy)
                heapq.heappush(busy, (t + ed-st, idx))
            cnt[idx] += 1
        _max = max(cnt)
        for i in range(n):
            if cnt[i] == _max:
                return i
        return -1