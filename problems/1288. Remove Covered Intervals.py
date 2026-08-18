'''
=== 1288. Remove Covered Intervals ===

Given a list of intervals, remove all intervals that are covered by another interval in the list.
Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
After doing so, return the number of remaining intervals.

Example 1:
    Input: intervals = [[1,4],[3,6],[2,8]]
    Output: 2
    Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:
    Input: intervals = [[1,4],[2,3]]
    Output: 1
Example 3:
    Input: intervals = [[0,10],[5,12]]
    Output: 2
Example 4:
    Input: intervals = [[3,10],[4,10],[5,11]]
    Output: 2
Example 5:
    Input: intervals = [[1,2],[1,4],[3,4]]
    Output: 1
 
Constraints:
    1. 1 <= intervals.length <= 1000
    2. intervals[i].length == 2
    3. 0 <= intervals[i][0] < intervals[i][1] <= 10^5
    4. All the intervals are unique.
'''
# === 100ms(69.88%) && 14.5MB(11.57%) === #
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        # print(intervals)
        i = 0
        while i < len(intervals)-1:
            j = i+1
            while j < len(intervals):
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    intervals.pop(j)
                elif intervals[j][0] >= intervals[i][1]:
                    break
                else:
                    j += 1
            i += 1
        # print(intervals)
        return len(intervals)
                