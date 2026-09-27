'''
=== 4068. Maximize Meeting Earnings with Idle Gaps ===

You are given a 2D integer array meetings, where meetings[i] = [starti, endi, revenuei] represents a meeting starting at time starti, ending at time endi, with revenue revenuei.
All meetings use half-open intervals [start, end), so meetings that only touch at endpoints do not overlap.
You may select any non-empty subset of meetings such that no two selected meetings overlap. You earn the revenue of each selected meeting.
Arrange the selected meetings in increasing order of their start times. For each pair of adjacent meetings in this order, you also earn 1 unit of revenue per unit of idle time between them. This idle time equals the later meeting's start time minus the earlier meeting's end time.
No idle revenue is earned before the earliest selected meeting starts or after the latest selected meeting ends. If only one meeting is selected, no idle revenue is earned.
Return the maximum total earnings achievable.
A subset of an array is a selection of elements of the array.

Example 1:
    Input: meetings = [[2,5,4],[6,8,3]]
    Output: 8
    Explanation:
    Select both meetings. They do not overlap and earn 4 + 3 = 7 units of meeting revenue.
    The first meeting ends at time 5, and the second starts at time 6. This idle gap earns 6 - 5 = 1 additional unit.
    The maximum total earnings are 7 + 1 = 8.
Example 2:
    Input: meetings = [[3,5,4],[4,7,8],[8,10,3]]
    Output: 12
    Explanation:
    Select the meetings at indices 1 and 2. They do not overlap and earn 8 + 3 = 11 units of meeting revenue.
    In chronological order, these meetings run from time 4 to 7 and from time 8 to 10. The idle gap earns 8 - 7 = 1 additional unit.
    The maximum total earnings are 11 + 1 = 12.
Example 3:
    Input: meetings = [[1,2,2],[4,5,2],[7,9,3]]
    Output: 11
    Explanation:
    Select all three meetings. They do not overlap and earn 2 + 2 + 3 = 7 units of meeting revenue.
    The idle gap from time 2 to 4 earns 4 - 2 = 2 additional units.
    The idle gap from time 5 to 7 earns 7 - 5 = 2 additional units.
    The maximum total earnings are 7 + 2 + 2 = 11.
 
Constraints
    1. 1 <= meetings.length <= 105
    2. meetings[i] = [starti, endi, revenuei]
    3. 0 <= starti < endi <= 109
    4. 1 <= revenuei <= 109
'''
# === 1036ms && 215.34MB === #
class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings = sorted(meetings)
        # print(meetings)
        n = len(meetings)

        @cache
        def dp(idx, is_start, need_select):
            if idx >= n:
                ans = 0 if not need_select else -math.inf
                # print(idx, is_start, need_select, ans)
                return ans
            if not is_start and not need_select:
                # print(idx, is_start, need_select, 0)
                return 0
            st, ed, rev = meetings[idx]
            nxt = bisect.bisect_left(meetings, [ed, ed, 0])
            if is_start:
                ans1 = dp(idx+1, True, False)
                ans2 = rev
                if nxt < n:
                    ans3 = rev + dp(nxt, False, True) + meetings[nxt][0]-ed
                else:
                    ans3 = -math.inf
            else:
                ans1 = meetings[idx+1][0]-st + dp(idx+1, False, True) if idx+1 < n else -math.inf
                ans2 = rev
                if nxt < n:
                    ans3 = rev + dp(nxt, False, True) + meetings[nxt][0]-ed
                else:
                    ans3 = -math.inf
            ans = max(ans1, ans2, ans3)
            # print(idx, is_start, need_select, ans)
            return ans
        
        return dp(0, True, False)

