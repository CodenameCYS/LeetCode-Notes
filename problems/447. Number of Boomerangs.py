'''
=== 447. Number of Boomerangs ===

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
    Input:
    [[0,0],[1,0],[2,0]]
    Output:
    2
    Explanation:
    The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''
# === 1272ms(50.61%) && 12.8MB(100%) === #
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return 0;
        ans = 0
        for i, p1 in enumerate(points):
            record = {}
            for j, p2 in enumerate(points):
                if i == j:
                    continue
                distance = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
                if distance in record.keys():
                    record[distance] += 1
                else:
                    record[distance] = 1
            # print(record)
            for v in record.values():
                ans += v*(v-1)
        return ans