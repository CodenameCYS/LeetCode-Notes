'''
=== 3380. Maximum Area Rectangle With Point Constraints I ===

You are given an array points where points[i] = [xi, yi] represents the coordinates of a point on an infinite plane.
Your task is to find the maximum area of a rectangle that:
    - Can be formed using four of these points as its corners.
    - Does not contain any other point inside or on its border.
    - Has its edges parallel to the axes.
Return the maximum area that you can obtain or -1 if no such rectangle is possible.

Example 1:
    Input: points = [[1,1],[1,3],[3,1],[3,3]]
    Output: 4
    Explanation:
    Example 1 diagram
    We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border. Hence, the maximum possible area would be 4.
Example 2:
    Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
    Output: -1
    Explanation:
    Example 2 diagram
    There is only one rectangle possible is with points [1,1], [1,3], [3,1] and [3,3] but [2,2] will always lie inside it. Hence, returning -1.
Example 3:
    Input: points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]
    Output: 2
    Explanation:
    Example 3 diagram
    The maximum area rectangle is formed by the points [1,3], [1,2], [3,2], [3,3], which has an area of 2. Additionally, the points [1,1], [1,2], [3,1], [3,2] also form a valid rectangle with the same area.

Constraints:
    1. 1 <= points.length <= 10
    2. points[i].length == 2
    3. 0 <= xi, yi <= 100
    4. All the given points are unique.
'''
# === 7ms && 17.5MB === #
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        points_set = set((x, y) for x, y in points)
        points = sorted(points)
        n = len(points)
        ans = -1
        for i in range(n-3):
            if points[i][0] != points[i+1][0]:
                continue
            for j in range(i+1, n-2):
                if points[j][0] != points[i][0]:
                    break
                for k in range(j+1, n-1):
                    if points[k][0] == points[i][0] or points[k][1] != points[i][1]:
                        continue
                    if (points[k][0], points[j][1]) not in points_set:
                        continue
                    corners = {(points[i][0], points[i][1]), (points[j][0], points[j][1]), (points[k][0], points[k][1]), (points[k][0], points[j][1])}
                    if any(points[i][0] <= x <= points[k][0] and points[i][1] <= y <= points[j][1] and (x, y) not in corners for x, y in points[i+1:] ):
                        continue
                    # print(f"corners = {corners}, S = {(points[k][0]-points[i][0]) * (points[j][1] - points[i][1])}")
                    ans = max(ans, (points[k][0]-points[i][0]) * (points[j][1] - points[i][1]))
        return ans

# === 0ms && 17.3MB === #               
class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        points = sorted(points)
        n = len(points)
        ans = -1
        for i in range(n-3):
            if points[i][0] != points[i+1][0]:
                continue
            if points[i+1][0] != points[i][0]:
                    continue
            for j in range(i+2, n-1):
                if points[j][0] == points[i][0] or points[j][1] != points[i][1]:
                    continue
                if points[j][1] != points[i][1] or points[j+1][1] != points[i+1][1]:
                    continue
                if any(points[i][1] <= y <= points[i+1][1] for x, y in points[i+2:j] ):
                    continue
                # print(f"corners = {corners}, S = {(points[k][0]-points[i][0]) * (points[j][1] - points[i][1])}")
                ans = max(ans, (points[j][0]-points[i][0]) * (points[i+1][1] - points[i][1]))
        return ans
                    