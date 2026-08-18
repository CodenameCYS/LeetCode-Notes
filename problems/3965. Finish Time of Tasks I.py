'''
=== 3965. Finish Time of Tasks I ===

You are given an integer n representing the number of tasks in a project, numbered from 0 to n - 1. These tasks are connected as a tree rooted at task 0. This is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that task ui is the parent of task vi.
You are also given an array baseTime of length n, where baseTime[i] represents the time to complete task i.
The finish time of each task is calculated as follows:
    - Leaf task: The finish time is baseTime[i].
    - Non-leaf task:
        - Let earliest be the minimum finish time among its children, and latest be the maximum finish time among its children.
        - Let ownDuration be (latest - earliest) + baseTime[i].
        - The finish time of task i is latest + ownDuration.
Return the finish time of the root task 0.

Example 1:
    Input: n = 3, edges = [[0,1],[1,2]], baseTime = [9,5,3]
    Output: 17
    Explanation:
    Task 2 is a leaf, so its finish time is baseTime[2] = 3.
    Task 1 has one child task 2:
    earliest = latest = 3
    ownDuration = (latest - earliest) + baseTime[1] = 5
    Finish time of task 1 is 3 + 5 = 8
    Task 0 has one child with finish time 8:
    earliest = latest = 8
    ownDuration = (latest - earliest) + baseTime[0] = 9
    Finish time of task 0 is 8 + 9 = 17
Example 2:
    Input: n = 3, edges = [[0,1],[0,2]], baseTime = [4,7,6]
    Output: 12
    Explanation:
    Task 1 is a leaf, so its finish time is baseTime[1] = 7.
    Task 2 is a leaf, so its finish time is baseTime[2] = 6.
    Task 0 has two children with finish times 7 and 6:
    earliest = 6, latest = 7
    ownDuration = (latest - earliest) + baseTime[0] = (7 - 6) + 4 = 5
    Finish time of task 0 is latest + ownDuration = 7 + 5 = 12
Example 3:
    Input: n = 4, edges = [[0,1],[0,2],[2,3]], baseTime = [5,8,2,1]
    Output: 18 
    Explanation:
    Task 1 is a leaf, so its finish time is baseTime[1] = 8.
    Task 3 is a leaf, so its finish time is baseTime[3] = 1.
    Task 2 has one child task 3:
    earliest = latest = 1
    ownDuration = (latest - earliest) + baseTime[2] = 0 + 2 = 2
    Finish time of task 2 is latest + ownDuration = 1 + 2 = 3
    Task 0 has two children with finish times 8 and 3:
    earliest = 3, latest = 8
    ownDuration = (latest - earliest) + baseTime[0] = (8 - 3) + 5 = 10
    Finish time of task 0 is latest + ownDuration = 8 + 10 = 18

Constraints:
    1. 1 <= n <= 105
    2. edges.length = n - 1
    3. edges[i] == [ui, vi]
    4. 0 <= ui, vi <= n - 1
    5. ui != vi
    6. The input is generated such that edges represents a valid tree.
    7. baseTime.length == n
    8. 1 <= baseTime[i] <= 105​​​​​​​
'''
# === 291ms && 129.34MB === #
class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        def dfs(u):
            if graph[u] == []:
                return baseTime[u]
            _min, _max = math.inf, -math.inf
            for v in graph[u]:
                t = dfs(v)
                _min, _max = min(_min, t), max(_max, t)
            return _max-_min+baseTime[u] + _max

        return dfs(0)