'''
=== 2203. Minimum Weighted Subgraph With the Required Paths ===

You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.
You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.
Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.
Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.
A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.

Example 1:
    Input: n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5
    Output: 9
    Explanation:
    The above figure represents the input graph.
    The blue edges represent one of the subgraphs that yield the optimal answer.
    Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer. It is not possible to get a subgraph with less weight satisfying all the constraints.
Example 2:
    Input: n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
    Output: -1
    Explanation:
    The above figure represents the input graph.
    It can be seen that there does not exist any path from node 1 to node 2, hence there are no subgraphs satisfying all the constraints.
 
Constraints:
    1. 3 <= n <= 105
    2. 0 <= edges.length <= 105
    3. edges[i].length == 3
    4. 0 <= fromi, toi, src1, src2, dest <= n - 1
    5. fromi != toi
    6. src1, src2, and dest are pairwise distinct.
    7. 1 <= weight[i] <= 105
'''
# === 3477ms && 113.1MB === #
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        edges = sorted(edges, key=lambda x: x[2])
        
        out_graph = defaultdict(list)
        in_graph = defaultdict(list)
        seen = set()
        for u, v, w in edges:
            if (u, v) in seen:
                continue
            seen.add((u,v))
            out_graph[u].append((v, w))
            in_graph[v].append((u, w))
        
        def get_downsteam_distance(src):
            q = [(0, src)]
            distances = {}
            while q:
                dis, u = heapq.heappop(q)
                if u not in distances:
                    distances[u] = dis
                for v, w in out_graph[u]:
                    if v not in distances:
                        heapq.heappush(q, (dis+w, v))
            return distances
        
        def get_upstream_distance(dest):
            q = [(0, dest)]
            distances = {}
            while q:
                dis, u = heapq.heappop(q)
                if u not in distances:
                    distances[u] = dis
                for v, w in in_graph[u]:
                    if v not in distances:
                        heapq.heappush(q, (dis+w, v))
            return distances
        
        src1_to_nodes = get_downsteam_distance(src1)
        src2_to_nodes = get_downsteam_distance(src2)
        nodes_to_dest = get_upstream_distance(dest)
        res = min(nodes_to_dest[v] + src1_to_nodes.get(v, math.inf) + src2_to_nodes.get(v, math.inf) for v in nodes_to_dest)
        return res if res != math.inf else -1