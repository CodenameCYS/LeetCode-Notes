'''
=== 3143. Maximum Points Inside the Square ===

You are given a 2D array points and a string s where, points[i] represents the coordinates of point i, and s[i] represents the tag of point i.
A valid square is a square centered at the origin (0, 0), has edges parallel to the axes, and does not contain two points with the same tag.
Return the maximum number of points contained in a valid square.
Note:
- A point is considered to be inside the square if it lies on or within the square's boundaries.
- The side length of the square can be zero.
 
Example 1:
    Input: points = [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]], s = "abdca"
    Output: 2
    Explanation:
    The square of side length 4 covers two points points[0] and points[1].
Example 2:
    Input: points = [[1,1],[-2,-2],[-2,2]], s = "abb"
    Output: 1
    Explanation:
    The square of side length 2 covers one point, which is points[0].
Example 3:
    Input: points = [[1,1],[-1,-1],[2,-2]], s = "ccd"
    Output: 0
    Explanation:
    It's impossible to make any valid squares centered at the origin such that it covers only one point among points[0] and points[1].

Constraints:
    1. 1 <= s.length, points.length <= 105
    2. points[i].length == 2
    3. -109 <= points[i][0], points[i][1] <= 109
    4. s.length == points.length
    5. points consists of distinct coordinates.
    6. s consists only of lowercase English letters.
'''
# === 882ms && 59.9MB === #
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        dis = {}
        bound = math.inf
        for point, tag in zip(points, s):
            x, y = abs(point[0]), abs(point[1])
            d = max(x, y)
            if tag not in dis:
                dis[tag] = [d, 1]
            else:
                if dis[tag][0] > d:
                    bound = min(bound, dis[tag][0])
                    dis[tag] = [d, 1]
                elif dis[tag][0] == d:
                    dis[tag][1] += 1
                    bound = min(bound, d)
                else:
                    bound = min(bound, d)
        #     print(point, tag, dis, bound)
        # print(dis, bound)
        dis = sorted(dis.values(), key=lambda x: (x[0], -x[1]))
        ans = 0
        for d, cnt in dis:
            if d >= bound or cnt > 1:
                break
            ans += cnt
        return ans