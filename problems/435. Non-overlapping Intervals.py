'''
=== 435. Non-overlapping Intervals ===

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
    Input: [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
    Input: [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
    Input: [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 
Note:
    1. You may assume the interval's end point is always bigger than its start point.
    2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
'''
# === 464ms && 108.4MB === #
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)   
        n = len(intervals)
        
        @lru_cache(None)
        def dp(idx, last_idx):
            if idx >= n:
                return 0
            if intervals[idx][0] >= intervals[last_idx][1]:
                return dp(idx+1, idx)
            else:
                return 1 + min(dp(idx+1, last_idx), dp(idx+1, idx))
            
        return dp(1, 0)
# === 84ms && 17.1MB === #
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end_sort = sorted(intervals, key=lambda x:x[1])
        last = None
        ans = 0
        for it in end_sort:
            if not last:
                last = it
            else:
                if it[0] >= last[1]:
                    last = it
                else:
                    ans += 1
        return ans