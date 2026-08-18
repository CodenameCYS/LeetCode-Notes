'''
=== 778. Swim in Rising Water ===

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).
Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.
You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:
    Input: [[0,2],[1,3]]
    Output: 3
    Explanation:
    At time 0, you are in grid location (0, 0).
    You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
    You cannot reach point (1, 1) until time 3.
    When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:
    Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    Output: 16
    Explanation:
        0  1  2  3   4
        24 23 22 21  5
        12 13 14 15 16
        11 17 18 19 20
        10  9  8  7  6
    The final route is marked in bold.
    We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Note:
    1. 2 <= N <= 50.
    2. grid[i][j] is a permutation of [0, ..., N*N - 1].
'''
# === 4504ms(5.23%) && 13.6MB(100%) === #
class Solution:
    def remove_internal_point(self, edge, have_seen):
        new_edge = []
        for x,y in edge:
            if not ((x, y-1) in have_seen and (x-1, y) in have_seen and \
               (x+1, y) in have_seen and (x, y+1) in have_seen):
                new_edge.append((x, y))
        return new_edge
    
    def update_edge(self, grid, edge, time, have_seen, N):
        tmp = deepcopy(edge)
        while edge != []:
            x, y = edge.pop(0)
            if x>0 and  (x-1, y) not in have_seen and grid[x-1][y] <= time:
                have_seen.add((x-1,y))
                edge.append((x-1,y))
                tmp.append((x-1, y))
            if x<N-1 and  (x+1, y) not in have_seen and grid[x+1][y] <= time:
                have_seen.add((x+1,y))
                edge.append((x+1,y))
                tmp.append((x+1,y))
            if y>0 and (x, y-1) not in have_seen and grid[x][y-1] <= time:
                have_seen.add((x,y-1))
                edge.append((x,y-1))
                tmp.append((x,y-1))
            if y<N-1 and (x, y+1) not in have_seen and grid[x][y+1] <= time:
                have_seen.add((x,y+1))
                edge.append((x,y+1))
                tmp.append((x,y+1))
        # print(tmp)
        new_edge = self.remove_internal_point(tmp, have_seen)
        # print(new_edge)
        return new_edge
    
    def swimInWater(self, grid: List[List[int]]):
        N = len(grid)
        have_seen = set()
        edge = [(N-1, N-1)]
        time = max(grid[N-1][N-1], grid[0][0], 2*N-2)
        edge = self.update_edge(grid, edge, time, have_seen, N)
        # print(edge)
        while (0,0) not in edge:
            time += 1
            edge = self.update_edge(grid, edge, time, have_seen, N)
            # print(edge)
        return time
# === 84ms(100%) && 14.5MB(25.40%) === #
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        have_visited = set()
        have_seen = {(0, 0)}
        q = [(grid[0][0], 0, 0)]
        while q != []:
            w, r, c = heapq.heappop(q)
            have_visited.add((r,c))
            ans = max(ans, w)
            if r == n-1 and c == n-1:
                break
            if r-1 >= 0 and (r-1, c) not in have_seen:
                heapq.heappush(q, (grid[r-1][c], r-1, c))
                have_seen.add((r-1, c))
            if r+1 < n and (r+1, c) not in have_seen:
                heapq.heappush(q, (grid[r+1][c], r+1, c))
                have_seen.add((r+1, c))
            if c-1 >= 0 and (r, c-1) not in have_seen:
                heapq.heappush(q, (grid[r][c-1], r, c-1))
                have_seen.add((r, c-1))
            if c+1 < n and (r, c+1) not in have_seen:
                heapq.heappush(q, (grid[r][c+1], r, c+1))
                have_seen.add((r, c+1))
        return ans
            
            
                
        
        