'''
=== 3311. Construct 2D Grid Matching Graph Layout ===

You are given a 2D integer array edges representing an undirected graph having n nodes, where edges[i] = [ui, vi] denotes an edge between nodes ui and vi.
Construct a 2D grid that satisfies these conditions:
    - The grid contains all nodes from 0 to n - 1 in its cells, with each node appearing exactly once.
    - Two nodes should be in adjacent grid cells (horizontally or vertically) if and only if there is an edge between them in edges.
It is guaranteed that edges can form a 2D grid that satisfies the conditions.
Return a 2D integer array satisfying the conditions above. If there are multiple solutions, return any of them.

Example 1:
    Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]]
    Output: [[3,1],[2,0]]
    Explanation:
Example 2:
    Input: n = 5, edges = [[0,1],[1,3],[2,3],[2,4]]
    Output: [[4,2,3,1,0]]
    Explanation:
Example 3:
    Input: n = 9, edges = [[0,1],[0,4],[0,5],[1,7],[2,3],[2,4],[2,5],[3,6],[4,6],[4,7],[6,8],[7,8]]
    Output: [[8,6,3],[7,4,2],[1,0,5]]
    Explanation:

Constraints:
    1. 2 <= n <= 5 * 104
    2. 1 <= edges.length <= 105
    3. edges[i] = [ui, vi]
    4. 0 <= ui < vi < n
    5. All the edges are distinct.
    6. The input is generated such that edges can form a 2D grid that satisfies the conditions.
'''
# === 5791ms && 712.5MB === #
class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def classify_points(points, edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            cnt = min(len(graph[u]) for u in points)
            corners = {u for u in points if len(graph[u]) == cnt}
            sides = {u for u in points if len(graph[u]) == cnt+1}
            inners = {u for u in points if len(graph[u]) == cnt+2}
            return graph, corners, sides, inners
        
        def construct_grid_sides(graph, corners, sides):
            if len(sides) == 0:
                u = list(corners)[0]
                grid_sides = [[u, graph[u][0]]]
                if len(graph[u]) > 1:
                    v = graph[u][1]
                    w = [i for i in graph[v] if i != u][0]
                    grid_sides.append([v, w])
                return grid_sides
            elif any(u in corners for c in corners for u in graph[c]):
                u = list(corners)[0]
                v = [i for i in graph[u] if i in corners][0]
                unext = [i for i in graph[u] if i != v][0]
                vnext = [i for i in graph[v] if i != u][0]
                grid_sides = [[u, unext], [v, vnext]]
                u, v = unext, vnext
                # print(grid_sides)
                while True:
                    unext = [i for i in graph[u] if i != grid_sides[0][-2] and i != v]
                    vnext = [i for i in graph[v] if i != grid_sides[1][-2] and i != u]
                    if len(unext) == 0:
                        break
                    grid_sides[0].append(unext[0])
                    grid_sides[1].append(vnext[0])
                    u, v = unext[0], vnext[0]
                    # print(grid_sides)
            else:
                grid_sides = []
                u0 = list(corners)[0]
                for u in graph[u0]:
                    side = [u0, u]
                    v = [i for i in graph[u] if i in sides and i != side[-2]]
                    while v:
                        u = v[0]
                        side.append(u)
                        v = [i for i in graph[u] if i in sides and i != side[-2]]
                    u = [i for i in graph[u] if i in corners and i != side[-2]][0]
                    side.append(u)
                    grid_sides.append(side)
                    
                    v = [i for i in graph[u] if i != side[-2]]
                    if v:
                        v = v[0]
                        side = [u, v]
                        u = v
                        v = [i for i in graph[u] if i in sides and i != side[-2]]
                        while v:
                            u = v[0]
                            side.append(u)
                            v = [i for i in graph[u] if i in sides and i != side[-2]]
                        u = [i for i in graph[u] if i in corners and i != side[-2]][0]
                        side.append(u)
                        grid_sides.append(side)
            return grid_sides
        
        def merge_grid(graph, grid_sides, inner_grid):
            lu, ld, ru, rd = inner_grid[0][0], inner_grid[-1][0], inner_grid[0][-1], inner_grid[-1][-1]
            for side in grid_sides:
                if lu in graph[side[1]] and ru in graph[side[-2]]:
                    up = side
                    break
                if lu in graph[side[-2]] and ru in graph[side[1]]:
                    up = side[::-1]
                    break
            for side in grid_sides:
                if side[0] == up[0] and side[-1] != up[-1]:
                    left = side
                    break
                if side[-1] == up[0] and side[0] != up[-1]:
                    left = side[::-1]
                    break
            for side in grid_sides:
                if side[0] == up[-1] and side[-1] != up[0]:
                    right = side
                    break
                if side[-1] == up[-1] and side[0] != up[0]:
                    right = side[::-1]
                    break
            for side in grid_sides:
                if side[0] == left[-1] and side[-1] == right[-1]:
                    down = side
                    break
                if side[-1] == left[-1] and side[0] == right[-1]:
                    down = side[::-1]
                    break
            # print(f"up = {up}")
            # print(f"left = {left}")
            # print(f"right = {right}")
            # print(f"down = {down}")
            grid = [up] + [[l] + side + [r] for l, side, r in zip(left[1:-1], inner_grid, right[1:-1])] + [down]
            return grid
        
        def construct(points, edges):
            if len(points) <= 1:
                return [list(points)]
            graph, corners, sides, inners = classify_points(points, edges)
            # print(f"graph = {graph}")
            # print(f"corners = {corners}")
            # print(f"sides = {sides}")
            # print(f"inners = {inners}")
            
            grid_sides = construct_grid_sides(graph, corners, sides)
            # print(f"grid_sides = {grid_sides}")
            if len(inners) == 0:
                return grid_sides
            
            inner_edges = [[u, v] for u, v in edges if u in inners and v in inners]
            inner_grid = construct(inners, inner_edges)
            # print(f"inner_grid = {inner_grid}")
            
            grid = merge_grid(graph, grid_sides, inner_grid)
            # print(f"grid = {grid}")
            
            # grid = [[]]
            return grid
        
        points = [i for i in range(n)]
        return construct(points, edges)