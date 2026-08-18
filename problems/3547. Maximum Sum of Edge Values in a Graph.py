'''
=== 3547. Maximum Sum of Edge Values in a Graph ===

You are given an undirected graph of n nodes, numbered from 0 to n - 1. Each node is connected to at most 2 other nodes.
The graph consists of m edges, represented by a 2D array edges, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi.
You have to assign a unique value from 1 to n to each node. The value of an edge will be the product of the values assigned to the two nodes it connects.
Your score is the sum of the values of all edges in the graph.
Return the maximum score you can achieve.

Example 1:
    Input: n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6]]
    Output: 130
    Explanation:
    The diagram above illustrates an optimal assignment of values to nodes. The sum of the values of the edges is: (7 * 6) + (7 * 5) + (6 * 5) + (1 * 3) + (3 * 4) + (4 * 2) = 130.
Example 2:
    Input: n = 6, edges = [[0,3],[4,5],[2,0],[1,3],[2,4],[1,5]]
    Output: 82
    Explanation:
    The diagram above illustrates an optimal assignment of values to nodes. The sum of the values of the edges is: (1 * 2) + (2 * 4) + (4 * 6) + (6 * 5) + (5 * 3) + (3 * 1) = 82.

Constraints:
    1. 1 <= n <= 5 * 104
    2. m == edges.length
    3. 1 <= m <= n
    4. edges[i].length == 2
    5. 0 <= ai, bi < n
    6. ai != bi
    7. There are no repeated edges.
    8. Each node is connected to at most 2 other nodes.
'''
# === 325ms && 44.2MB === #
class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        # print("=" * 10)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # starters = [u for u in range(n) if len(graph[u]) <= 1]
        nodes = [u for u in range(n) if len(graph[u]) == 1] + [u for u in range(n) if len(graph[u]) == 2]
            
        def get_max(m, k, is_circle):
            if k == 1:
                return 0
            nums = [m-i for i in range(k)]
            nums = nums[1::2][::-1] + nums[::2] 
            ans = sum([nums[i] * nums[i+1] for i in range(k-1)])
            return ans if not is_circle else ans + nums[0] * nums[-1]
        
        ans = 0
        lines = []
        status = [0 for _ in range(n)]
        for i in nodes:
            if status[i] == 1:
                continue
            u = i
            length = 0
            while status[u] == 0:
                status[u] = 1
                length += 1
                for v in graph[u]:
                    if status[v] == 0:
                        u = v
                        break
            # print(i, length)
            if i in graph[u] and length > 2:
                ans += get_max(n, length, True)
                n -= length
            else:
                lines.append(length)
        
        # print(lines)
        lines = sorted(lines, reverse=True)
        for length in lines:
            ans += get_max(n, length, False)
            n -= length
        return ans
                
        
        
        