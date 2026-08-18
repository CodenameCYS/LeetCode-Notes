'''
=== 1893. Check if All the Integers in a Range Are Covered ===

You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.
Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.
An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

Example 1:
    Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
    Output: true
    Explanation: Every integer between 2 and 5 is covered:
    - 2 is covered by the first range.
    - 3 and 4 are covered by the second range.
    - 5 is covered by the third range.
Example 2:
    Input: ranges = [[1,10],[10,20]], left = 21, right = 21
    Output: false
    Explanation: 21 is not covered by any range.
 
Constraints:
    1. 1 <= ranges.length <= 50
    2. 1 <= starti <= endi <= 50
    3. 1 <= left <= right <= 50
'''
# === 40ms && 14.3MB === #
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges = sorted([x for x in ranges if x[1] >= left and x[0] <= right])
        n = len(ranges)
        if n == 0:
            return False
        _min, _max = ranges[0][0], ranges[0][1]
        for bg, ed in ranges[1:]:
            if bg > _max+1:
                return False
            _max = max(_max, ed)
        return _min <= left and _max >= right
        