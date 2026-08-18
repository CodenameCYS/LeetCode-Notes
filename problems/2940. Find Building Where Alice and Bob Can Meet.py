'''
=== 2940. Find Building Where Alice and Bob Can Meet ===

You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.
If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].
You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.
Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

Example 1:
    Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
    Output: [2,5,-1,5,2]
    Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
    In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
    In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
    In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
    In the fifth query, Alice and Bob are already in the same building.  
    For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
    For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.
Example 2:
    Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
    Output: [7,6,-1,4,6]
    Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
    In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
    In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
    In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
    In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
    For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
    For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

Constraints:
    1. 1 <= heights.length <= 5 * 104
    2. 1 <= heights[i] <= 109
    3. 1 <= queries.length <= 5 * 104
    4. queries[i] = [ai, bi]
    5. 0 <= ai, bi <= heights.length - 1
'''
# === 5336ms && 100.2MB === #
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        buildings = [(idx, h) for idx, h in enumerate(heights)]
        buildings = sorted(buildings, key=lambda x: (x[1], -x[0]), reverse=True)
        indexes = {x[0]: i for i, x in enumerate(buildings)}
        
        res = [-1 for _ in queries]
        queries = [(idx, i, j) for idx, (i, j) in enumerate(queries)]
        for idx, i, j in queries:
            if i == j:
                res[idx] = i
            elif i < j and heights[i] < heights[j]:
                res[idx] = j
            elif i > j and heights[i] > heights[j]:
                res[idx] = i
        
        queries = [(idx, i, j) if indexes[i] < indexes[j] else (idx, j, i) for (idx, i, j) in queries if res[idx] == -1]
        queries = sorted(queries, key=lambda x: indexes[x[2]])
        trigger = defaultdict(list)
        last_seen = defaultdict(int)
        for idx, i, j in queries:
            trigger[j].append((idx, i, j))
            last_seen[i] = idx
            last_seen[j] = idx
        # print(queries)
        # print(last_seen)
            
        def query(i, j):
            if i == j:
                return i
            r1, r2 = can_reach[i], can_reach[j]
            n, m = len(r1), len(r2)
            idx = bisect.bisect_left(r2, r1[0])
            if idx < m and r1[0] == r2[idx]:
                return r1[0]
            i = 0
            idx = bisect.bisect_left(r2, r1[-1])
            if idx >= m or r1[-1] != r2[idx]:
                return -1
            j = n-1
            while i < j-1:
                k = (i+j) // 2
                idx = bisect.bisect_left(r2, r1[k])
                if idx < m and r1[k] == r2[idx]:
                    j = k
                else:
                    i = k
            return r1[j]
            
        s = []
        can_reach = {}
        # res = [0 for _ in queries]
        for i, h in buildings:
            idx = bisect.bisect_left(s, i)
            s.insert(idx, i)
            if i in last_seen:
                can_reach[i] = s[idx:]
                # print(can_reach)
            for idx, i, j in trigger[i]:
                res[idx] = query(i, j)
                if last_seen[i] == idx:
                    can_reach.pop(i)
                if j != i and last_seen[j] == idx:
                    can_reach.pop(j)
        # print("=" * 10)
        return res
    
# === 1682ms && 39.5MB === #
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        m = len(queries)
        res = [-1] * m
        q = []
        left = [[] for _ in heights]
        for k, (i, j) in enumerate(queries):
            if i > j:
                i, j = j, i
            if i == j or heights[i] < heights[j]:
                res[k] = j
            else:
                left[j].append((heights[i], k))
        
        h = []
        for i, x in enumerate(heights):
            while h and h[0][0] < x:
                k = heappop(h)[1]
                res[k] = i
            for p in left[i]:
                heappush(h, p)
        return res