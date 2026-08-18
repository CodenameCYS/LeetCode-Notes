'''
=== 3414. Maximum Score of Non-overlapping Intervals ===

You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.
Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.
Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.
An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b.
If the first min(a.length, b.length) elements do not differ, then the shorter array is the lexicographically smaller one.

Example 1:
    Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
    Output: [2,3]
    Explanation:
    You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.
Example 2:
    Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]
    Output: [1,3,5,6]
    Explanation:
    You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

Constraints:
    1. 1 <= intevals.length <= 5 * 104
    2. intervals[i].length == 3
    3. intervals[i] = [li, ri, weighti]
    4. 1 <= li <= ri <= 109
    5. 1 <= weighti <= 109
'''
# === 1899ms && 134MB === #
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = [[l,r,w,i] for i, (l,r,w) in enumerate(intervals)]
        intervals = sorted(intervals)
        n = len(intervals)
        
        @lru_cache(None)
        def dp(idx, k):
            if k == 0 or idx == n:
                return 0, []
            s1, elems1 = dp(idx+1, k)
            l, r, w, i = intervals[idx]
            nxt = bisect.bisect_left(intervals, [r+1, r+1, 0, 0])
            s2, elems2 = dp(nxt, k-1)
            s2, elems2 = s2+w, sorted([i] + elems2)
            if s1 > s2 or (s1 == s2 and elems1 < elems2):
                return s1, elems1
            else:
                return s2, elems2
            
        score, elems = dp(0, 4)
        return elems