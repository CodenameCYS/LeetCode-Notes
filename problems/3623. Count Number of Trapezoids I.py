'''
=== 3623. Count Number of Trapezoids I ===

You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.
A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.
Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
    Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
    Output: 3
    Explanation:
    There are three distinct ways to pick four points that form a horizontal trapezoid:
    Using points [1,0], [2,0], [3,2], and [2,2].
    Using points [2,0], [3,0], [3,2], and [2,2].
    Using points [1,0], [3,0], [3,2], and [2,2].
Example 2:
    Input: points = [[0,0],[1,0],[0,1],[2,1]]
    Output: 1
    Explanation:
    There is only one horizontal trapezoid that can be formed.

Constraints:
    1. 4 <= points.length <= 105
    2. –108 <= xi, yi <= 108
    3. All points are pairwise distinct.
'''
MOD = 10**9+7
# === 128ms && 63.46MB === #
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        groups = defaultdict(int)
        for x, y in points:
            groups[y] += 1
        ys = sorted(groups.keys())
        cnt = [(groups[y]*(groups[y]-1)//2) % MOD for y in ys]
        n = len(cnt)
        ans, s = 0, 0
        for i in range(n):
            ans = (ans + cnt[i] * s) % MOD
            s += cnt[i]
        return ans