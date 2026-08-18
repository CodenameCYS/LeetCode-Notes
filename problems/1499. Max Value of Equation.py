'''
=== 1499. Max Value of Equation ===

Given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.
Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length. It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

Example 1:
    Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
    Output: 4
    Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
    No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:
    Input: points = [[0,0],[3,0],[9,2]], k = 3
    Output: 3
    Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
 
Constraints:
    1. 2 <= points.length <= 10^5
    2. points[i].length == 2
    3. -10^8 <= points[i][0], points[i][1] <= 10^8
    4. 0 <= k <= 2 * 10^8
    5. points[i][0] < points[j][0] for all 1 <= i < j <= points.length
    6. xi form a strictly increasing sequence.
'''
import math
# === 1748ms(27.25%) && 60.1MB === #
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -math.inf
        n = len(points)
        ed = 1
        max_loc = 0
        window_max = -math.inf
        for st in range(n-1):
            if max_loc > st:
                window_max = window_max + points[st-1][0]-points[st-1][1] + points[st][1]-points[st][0]
            else:
                ed = st+1
                window_max = -math.inf
            while ed < n and points[ed][0]-points[st][0] <= k:
                if points[st][1]+points[ed][1]+points[ed][0]-points[st][0] >= window_max:
                    window_max = points[st][1]+points[ed][1]+points[ed][0]-points[st][0]
                    max_loc = ed
                ed += 1
            # print("window: i: {}, j: {}, sum: {}".format(st, max_loc, window_max))
            ans = max(ans, window_max)
            # print(ans, st, ed, max_loc)
        return ans