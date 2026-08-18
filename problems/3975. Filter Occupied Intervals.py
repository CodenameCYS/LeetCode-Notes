'''
=== 3975. Filter Occupied Intervals ===

You are given a 2D integer array occupiedIntervals, where occupiedIntervals[i] = [starti, endi] represents a time interval during which you are occupied. Each interval starts at starti and ends at endi, inclusive. These intervals may overlap.
You are also given two integers freeStart and freeEnd, which define a free time interval from freeStart to freeEnd, inclusive.
Your task is to merge all occupied intervals that overlap or touch, then remove all integer points in the free interval from the merged occupied intervals.
Two intervals touch if the second interval starts immediately after the first one ends. For example, [1, 1] and [2, 2] touch and should be merged into [1, 2].
Return the remaining occupied intervals in sorted order. The returned intervals must be non-overlapping and must contain the minimum number of intervals possible. If there are no remaining occupied points, return an empty list.

Example 1:
    Input: occupiedIntervals = [[2,6],[4,8],[10,10],[10,12],[14,16]], freeStart = 7, freeEnd = 11
    Output: [[2,6],[12,12],[14,16]]
    Explanation:
    After merging, the occupied intervals are [2, 8], [10, 12], and [14, 16].
    Excluding the free interval [7, 11] results in [2, 6], [12, 12], and [14, 16].
Example 2:
    Input: occupiedIntervals = [[1,5],[2,3]], freeStart = 3, freeEnd = 8
    Output: [[1,2]]
    Explanation:
    After merging, the occupied interval is [1, 5].
    Excluding the free interval [3, 8] results in [1, 2].
 
Constraints:
    1. 1 <= occupiedIntervals.length <= 5 * 104
    2. occupiedIntervals[i].length == 2
    3. 1 <= starti <= endi <= 109
    4. 1 <= freeStart <= freeEnd <= 109
'''
# === 223ms && 40.12MB === #
class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals = sorted(occupiedIntervals)
        
        intervals = []
        _st, _ed = occupiedIntervals[0]
        for st, ed in occupiedIntervals[1:]:
            if st > _ed+1:
                intervals.append([_st, _ed])
                _st, _ed = st, ed
            else:
                _ed = max(_ed, ed)
        intervals.append([_st, _ed])
        # print(intervals)

        ans = []
        for i, (st, ed) in enumerate(intervals):
            # print(i, st, ed, ans)
            if ed < freeStart:
                ans.append([st, ed])
            elif st < freeStart and ed <= freeEnd:
                ans.append([st, freeStart-1])
            elif st < freeStart and ed > freeEnd:
                ans.append([st, freeStart-1])
                ans.append([freeEnd+1, ed])
            elif st <= freeEnd and ed > freeEnd:
                ans.append([freeEnd+1, ed])
            elif st > freeEnd:
                ans += intervals[i:]
                break
        return ans
            