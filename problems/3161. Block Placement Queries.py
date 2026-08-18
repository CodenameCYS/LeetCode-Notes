'''
=== 3161. Block Placement Queries ===

There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.
You are given a 2D array queries, which contains two types of queries:
    - For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
    - For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

Example 1:
    Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
    Output: [false,true,true]
    Explanation:
    For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.
Example 2:
    Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
    Output: [true,true,false]
    Explanation:
    Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
    Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.
 
Constraints:
    1. 1 <= queries.length <= 15 * 104
    2. 2 <= queries[i].length <= 3
    3. 1 <= queries[i][0] <= 2
    4. 1 <= x, sz <= min(5 * 104, 3 * queries.length)
    5. The input is generated such that for queries of type 1, no obstacle exists at distance x when the query is asked.
    6. The input is generated such that there is at least one query of type 2.
'''
# === 5706ms && 87MB === #
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

    def query(self, lb, rb):
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
    
    
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        n = max(q[1] for q in queries)
        segment_tree = SegmentTree([0 for _ in range(n+1)])
        obstacles = [0]
        
        ans = []
        for query in queries:
            if query[0] == 1:
                x = query[1]
                idx = bisect.bisect_left(obstacles, x)
                prev = obstacles[idx-1]
                segment_tree.update(x, x-prev)
                if idx < len(obstacles):
                    nxt = obstacles[idx]
                    segment_tree.update(nxt, nxt-x)
                bisect.insort(obstacles, x)
            else:
                x, sz = query[1:]
                idx = bisect.bisect_right(obstacles, x)
                prev = obstacles[idx-1]
                _max = max(x-prev, segment_tree.query(0, prev))
                ans.append(sz <= _max)
        return ans
                
        