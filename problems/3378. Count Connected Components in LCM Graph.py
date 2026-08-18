'''
=== 3378. Count Connected Components in LCM Graph ===

You are given an array of integers nums of size n and a positive integer threshold.
There is a graph consisting of n nodes with the ith node having a value of nums[i]. Two nodes i and j in the graph are connected via an undirected edge if lcm(nums[i], nums[j]) <= threshold.
Return the number of connected components in this graph.
A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
The term lcm(a, b) denotes the least common multiple of a and b.

Example 1:
    Input: nums = [2,4,8,3,9], threshold = 5
    Output: 4
    Explanation: 
    The four connected components are (2, 4), (3), (8), (9).
Example 2:
    Input: nums = [2,4,8,3,9,12], threshold = 10
    Output: 2
    Explanation: 
    The two connected components are (2, 3, 4, 8, 9), and (12).

Constraints:
    1. 1 <= nums.length <= 105
    2. 1 <= nums[i] <= 109
    3. All elements of nums are unique.
    4. 1 <= threshold <= 2 * 105
'''
class DSU:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.cluster_num = N
        
    def find(self, k):
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            self.root[y] = x
            self.cluster_num -= 1
        return
# === 1126ms && 42.4MB === #
class Solution:
    def countComponents(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        dsu = DSU(n)
        nums = sorted(nums)
        index = {x: i for i, x in enumerate(nums)}
        status = [0 for _ in range(threshold+1)]
        cores = []
        for i, x in enumerate(nums):
            if x > threshold:
                break
            if status[x] == 1:
                continue
            for c in cores:
                if math.lcm(c, x) <= threshold:
                    dsu.union(index[c], i)
            cores.append(x)
            for j in range(x, threshold+1, x):
                status[j] = 1
                if j in index:
                    dsu.union(i, index[j])
        return dsu.cluster_num
        