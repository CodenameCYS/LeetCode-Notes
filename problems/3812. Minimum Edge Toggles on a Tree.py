'''
=== 3812. Minimum Edge Toggles on a Tree ===

You are given an undirected tree with n nodes, numbered from 0 to n - 1. It is represented by a 2D integer array edges​​​​​​​ of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
You are also given two binary strings start and target of length n. For each node x, start[x] is its initial color and target[x] is its desired color.
In one operation, you may pick an edge with index i and toggle both of its endpoints. That is, if the edge is [u, v], then the colors of nodes u and v each flip from '0' to '1' or from '1' to '0'.
Return an array of edge indices whose operations transform start into target. Among all valid sequences with minimum possible length, return the edge indices in increasing​​​​​​​ order.
If it is impossible to transform start into target, return an array containing a single element equal to -1.

Example 1:
    Input: n = 3, edges = [[0,1],[1,2]], start = "010", target = "100"
    Output: [0]
    Explanation:
    Toggle edge with index 0, which flips nodes 0 and 1.
    ​​​​​​The string changes from "010" to "100", matching the target.
Example 2:
    Input: n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[3,5],[1,6]], start = "0011000", target = "0010001"
    Output: [1,2,5]
    Explanation:
    Toggle edge with index 1, which flips nodes 1 and 2.
    Toggle edge with index 2, which flips nodes 2 and 3.
    Toggle edge with index 5, which flips nodes 1 and 6.
    After these operations, the resulting string becomes "0010001", which matches the target.
Example 3:
    Input: n = 2, edges = [[0,1]], start = "00", target = "01"
    Output: [-1]
    Explanation:
    There is no sequence of edge toggles that transforms "00" into "01". Therefore, we return [-1].

Constraints:
    1. 2 <= n == start.length == target.length <= 105
    2. edges.length == n - 1
    3. edges[i] = [ai, bi]
    4. 0 <= ai, bi < n
    5. start[i] is either '0' or '1'.
    6. target[i] is either '0' or '1'.
    7. The input is generated such that edges represents a valid tree.
'''
# === 453ms && 156.9MB === #
class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        g = [[] for _ in range(n)]
        for i, (x, y) in enumerate(edges):
            g[x].append((y, i))
            g[y].append((x, i))

        ans = []

        # 返回是否需要翻转 x-fa 这条边
        def dfs(x: int, fa: int) -> bool:
            rev = start[x] != target[x]  # x-fa 是否要翻转
            for y, i in g[x]:
                if y != fa and dfs(y, x):
                    ans.append(i)  # 需要翻转 y-x
                    rev = not rev  # x 被翻转了
            return rev

        if dfs(0, -1):  # 只剩下一个根节点需要翻转，无法操作
            return [-1]

        ans.sort()
        return ans
