'''
=== 3625. Count Number of Trapezoids II ===

You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.
Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.
A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

Example 1:
    Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
    Output: 2
    Explanation:
    There are two distinct ways to pick four points that form a trapezoid:
    The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
    The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.
Example 2:
    Input: points = [[0,0],[1,0],[0,1],[2,1]]
    Output: 1
    Explanation:
    There is only one trapezoid which can be formed.

Constraints:
    1. 4 <= points.length <= 500
    2. –1000 <= xi, yi <= 1000
    3. All points are pairwise distinct.
'''
# === 2392ms && 126.76MB === #
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)

        def cal_line(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            k = (y1-y2)/(x1-x2) if x1 != x2 else 1e9
            b = (x2*y1-x1*y2) / (x1-x2) if x1 != x2 else x1
            return (k, b)

        edges = defaultdict(lambda: defaultdict(int))
        lines = defaultdict(set)
        for i in range(n-1):
            for j in range(i+1, n):
                k, b = cal_line(i, j)
                edges[k][b] += 1
                lines[(k,b)].add(i)
                lines[(k,b)].add(j)
        if len(edges) == 1:
            return 0
        
        ans = 0
        for k, bs in edges.items():
            bs = list(bs.values())
            m = len(bs)
            for i in range(m-1):
                n1 = bs[i]
                for j in range(i+1, m):
                    n2 = bs[j]
                    ans += n1 * n2

        def count_parallelograms(points):
            n = len(points)
            # 哈希表记录每个中点（存储2倍值避免浮点误差）的出现次数
            midpoint_count = defaultdict(int)
            
            # 遍历所有点对 (i, j) 其中 i < j
            for i in range(n):
                x1, y1 = points[i]
                for j in range(i + 1, n):
                    x2, y2 = points[j]
                    # 计算中点*2（整数存储避免除法）
                    mx = x1 + x2
                    my = y1 + y2
                    midpoint_count[(mx, my)] += 1
            
            # 统计平行四边形总数
            total = 0
            for count in midpoint_count.values():
                if count >= 2:
                    # 组合公式 C(count, 2) = count*(count-1)//2
                    total += count * (count - 1) // 2
            return total

        dup = count_parallelograms(points)
        for line in lines.values():
            _points = [points[i] for i in line]
            if len(_points) >= 4:
                dup -= count_parallelograms(_points)
        return ans - dup
