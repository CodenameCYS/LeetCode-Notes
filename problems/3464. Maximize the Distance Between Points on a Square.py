'''
=== 3464. Maximize the Distance Between Points on a Square ===

You are given an integer side, representing the edge length of a square with corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.
You are also given a positive integer k and a 2D integer array points, where points[i] = [xi, yi] represents the coordinate of a point lying on the boundary of the square.
You need to select k elements among points such that the minimum Manhattan distance between any two points is maximized.
Return the maximum possible minimum Manhattan distance between the selected k points.
The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

Example 1:
    Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4
    Output: 2
    Explanation:
    Select all four points.
Example 2:
    Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4
    Output: 1
    Explanation:
    Select the points (0, 0), (2, 0), (2, 2), and (2, 1).
Example 3:
    Input: side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5
    Output: 1
    Explanation:
    Select the points (0, 0), (0, 1), (0, 2), (1, 2), and (2, 2).

Constraints:
    1. 1 <= side <= 109
    2. 4 <= points.length <= min(4 * side, 15 * 103)
    3. points[i] == [xi, yi]
    4. The input is generated such that:
        - points[i] lies on the boundary of the square.
        - All points[i] are unique.
    5. 4 <= k <= min(25, points.length)
'''
# === 739ms && 23.4MB === #
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
            # 转换每个点到周长坐标
            sorted_p = []
            for x, y in points:
                if x == 0:
                    coord = y
                elif y == side:
                    coord = side + x
                elif x == side:
                    coord = 3 * side - y
                else:  # y == 0
                    coord = 3 * side + (side - x)
                sorted_p.append(coord)
            sorted_p.sort()
            n = len(sorted_p)

            def is_possible(d):
                if d == 0:
                    return True
                # 扩展数组以处理环形问题
                extended_p = sorted_p + [p + 4 * side for p in sorted_p]
                # 遍历每个可能的起点
                for i in range(n):
                    current = i
                    count = 1
                    for _ in range(k - 1):
                        target = extended_p[current] + d
                        # 查找下一个点的位置
                        j = bisect.bisect_left(extended_p, target, current + 1)
                        if j >= len(extended_p):
                            break
                        current = j
                        count += 1
                    if count >= k:
                        # 计算跨度
                        span = extended_p[current] - extended_p[i]
                        if span <= 4 * side - d:
                            return True
                return False

            # 二分查找
            low = 0
            high = side + 1
            ans = 0
            while low < high-1:
                mid = (low + high) // 2
                if is_possible(mid):
                    low = mid
                else:
                    high = mid
            return low

