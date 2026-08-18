'''
=== 3382. Maximum Area Rectangle With Point Constraints II ===

There are n points on an infinite plane. You are given two integer arrays xCoord and yCoord where (xCoord[i], yCoord[i]) represents the coordinates of the ith point.
Your task is to find the maximum area of a rectangle that:
    - Can be formed using four of these points as its corners.
    - Does not contain any other point inside or on its border.
    - Has its edges parallel to the axes.
Return the maximum area that you can obtain or -1 if no such rectangle is possible.

Example 1:
    Input: xCoord = [1,1,3,3], yCoord = [1,3,1,3]
    Output: 4
    Explanation:
    Example 1 diagram
    We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border. Hence, the maximum possible area would be 4.
Example 2:
    Input: xCoord = [1,1,3,3,2], yCoord = [1,3,1,3,2]
    Output: -1
    Explanation:
    Example 2 diagram
    There is only one rectangle possible is with points [1,1], [1,3], [3,1] and [3,3] but [2,2] will always lie inside it. Hence, returning -1.
Example 3:
    Input: xCoord = [1,1,3,3,1,3], yCoord = [1,3,1,3,2,2]
    Output: 2
    Explanation:
    Example 3 diagram
    The maximum area rectangle is formed by the points [1,3], [1,2], [3,2], [3,3], which has an area of 2. Additionally, the points [1,1], [1,2], [3,1], [3,2] also form a valid rectangle with the same area.

Constraints:
    1. 1 <= xCoord.length == yCoord.length <= 2 * 105
    2. 0 <= xCoord[i], yCoord[i] <= 8 * 107
    3. All the given points are unique.
'''
class SegmentTree:
    def __init__(self, arr):
        self.length = len(arr)
        self.tree = self.build(arr)

    def feature_func(self, *args):
        return max(args)

    def build(self, arr):
        n = len(arr)
        tree = [0 for _ in range(2*n)]
        for i in range(n):
            tree[i+n] = arr[i]
        for i in range(n-1, 0, -1):
            tree[i] = self.feature_func(tree[i<<1], tree[(i<<1) | 1])
        return tree

    def update(self, idx, val):
        idx = idx + self.length
        self.tree[idx] = val
        while idx > 1:
            self.tree[idx>>1] = self.feature_func(self.tree[idx], self.tree[idx ^ 1])
            idx = idx>>1
        return

    def query_range(self, lb, rb):
        lb += self.length 
        rb += self.length
        nodes = []
        while lb < rb:
            if lb & 1 == 1:
                nodes.append(self.tree[lb])
                lb += 1
            if rb & 1 == 0:
                nodes.append(self.tree[rb])
                rb -= 1
            lb = lb >> 1
            rb = rb >> 1
        if lb == rb:
            nodes.append(self.tree[rb])
        return self.feature_func(*nodes)
    
    def query(self, idx):
        return self.tree[idx + self.length]

# === 3270ms && 67.6MB === #
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points = [(x, y) for x, y in zip(xCoord, yCoord)]
        n = len(points)
        points = sorted(points)
        cols = sorted(set(yCoord))
        closest = SegmentTree([-1 for _ in cols])
        
        ans = -1
        for i in range(n-1):
            y1_idx = bisect.bisect_left(cols, points[i][1])
            if points[i][0] == points[i+1][0]:
                y2_idx = bisect.bisect_left(cols, points[i+1][1])
                x1 = closest.query(y1_idx)
                x2 = closest.query(y2_idx)
                if x1 != -1 and x2 != -1 and x1 == x2:
                    S = (points[i+1][1] - points[i][1]) * (points[i][0] - x1)
                    if S >= ans and (y2_idx - y1_idx <= 1 or closest.query_range(y1_idx+1, y2_idx-1) < x1):
                        ans = max(ans, S)
            closest.update(y1_idx, points[i][0])
        return ans
                    