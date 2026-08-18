'''
=== 3486. Longest Special Path II ===

You are given an undirected tree rooted at node 0, with n nodes numbered from 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi, lengthi] indicates an edge between nodes ui and vi with length lengthi. You are also given an integer array nums, where nums[i] represents the value at node i.
A special path is defined as a downward path from an ancestor node to a descendant node in which all node values are distinct, except for at most one value that may appear twice.
Return an array result of size 2, where result[0] is the length of the longest special path, and result[1] is the minimum number of nodes in all possible longest special paths.

Example 1:
    Input: edges = [[0,1,1],[1,2,3],[1,3,1],[2,4,6],[4,7,2],[3,5,2],[3,6,5],[6,8,3]], nums = [1,1,0,3,1,2,1,1,0]
    Output: [9,3]
    Explanation:
    The longest special paths are 1 -> 2 -> 4 and 1 -> 3 -> 6 -> 8, both having a length of 9. The minimum number of nodes across all longest special paths is 3.
Example 2:
    Input: edges = [[1,0,3],[0,2,4],[0,3,5]], nums = [1,1,0,2]
    Output: [5,2]
    Explanation:
    The longest path is 0 -> 3 consisting of 2 nodes with a length of 5.

Constraints:
    1. 2 <= n <= 5 * 104
    2. edges.length == n - 1
    3. edges[i].length == 3
    4. 0 <= ui, vi < n
    5. 1 <= lengthi <= 103
    6. nums.length == n
    7. 0 <= nums[i] <= 5 * 104
    8. The input is generated such that edges represents a valid tree.
'''
# === Time Limit Exceeded === #
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        # print(graph)
        
        ans = [0, math.inf]
        
        def dfs(parent, root, path, length, nodes, cnt, have_dual):
            # print("> ", root, path, length, nodes, cnt, have_dual)
            nonlocal ans
            cnt[nums[root]] += 1
            if cnt[nums[root]] == 2 and have_dual:
                while True:
                    v, w = path.pop(0)
                    cnt[nums[v]] -= 1
                    length -= w
                    nodes -= 1
                    if cnt[nums[v]] == 1:
                        break
                have_dual = True
            elif cnt[nums[root]] == 3:
                while True:
                    v, w = path.pop(0)
                    cnt[nums[v]] -= 1
                    length -= w
                    nodes -= 1
                    if cnt[nums[v]] == 2:
                        break
                have_dual = True
            elif cnt[nums[root]] == 2:
                have_dual = True
                
            # print(path, length, nodes, cnt)
            if length > ans[0]:
                ans = [length, nodes]
            elif length == ans[0]:
                ans[1] = min(ans[1], nodes)
                
            for u, w in graph[root]:
                if u == parent:
                    continue
                dfs(root, u, path + [(root, w)], length + w, nodes + 1, deepcopy(cnt), have_dual)
            return
        
        cnt = defaultdict(int)
        dfs(-1, 0, [], 0, 1, cnt, False)
        # print("=" * 10)
        return ans
