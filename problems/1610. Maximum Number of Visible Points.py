'''
=== 1610. Maximum Number of Visible Points ===

You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.
Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].
You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east direction from your position is in your field of view.
There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.
Return the maximum number of points you can see.

Example 1:
    Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
    Output: 3
    Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.
Example 2:
    Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
    Output: 4
    Explanation: All points can be made visible in your field of view, including the one at your location.
Example 3:
    Input: points = [[0,1],[2,1]], angle = 13, location = [1,1]
    Output: 1
    Explanation: You can only see one of the two points, as shown above.
 
Constraints:
    1. 1 <= points.length <= 105
    2. points[i].length == 2
    3. location.length == 2
    4. 0 <= angle < 360
    5. 0 <= posx, posy, xi, yi <= 109
'''
import math
# === 1948ms && 59.9MB === #
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        delta = 1e-7
        
        def cal_angle(x, y):
            x0, y0 = location
            xd, yd = x - x0, y-y0
            if yd == 0:
                return 0 if xd >= 0 else 180
            elif xd == 0:
                return 90 if yd >= 0 else 270
            theta = 180 * math.acos(xd / math.sqrt(xd**2 + yd **2)) / math.pi
            return theta if yd > 0 else 360 - theta
        
        angle_list = []
        always_seen = 0
        for x, y in points:
            if location[0] == x and location[1] == y:
                always_seen += 1
            else:
                angle_list.append(cal_angle(x, y))
        
        angle_list = sorted(angle_list)
        # print(angle_list)
        n = len(points)
        angle_list += [x+360 for x in angle_list if x + 360 <= angle_list[-1] + angle]
        m = len(angle_list)
        # print(angle_list)
        j = 0
        ans = 0
        for i in range(n):
            while j < m and angle_list[j]-angle_list[i] <= angle + delta:
                j += 1
            ans = max(ans, min(j - i, n))
        return ans + always_seen