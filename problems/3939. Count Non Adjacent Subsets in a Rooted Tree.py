'''
=== 3939. Count Non Adjacent Subsets in a Rooted Tree ===

You are given a rooted tree with n nodes labeled from 0 to n - 1, represented by an integer array parent of length n, where:
    - parent[0] = -1 (node 0 is the root).
    - For each 1 <= i < n, parent[i] is the parent of node i (0 <= parent[i] < i).
You are also given an integer array nums of length n, where nums[i] is the value of node i, and an integer k.
A non-empty subset of nodes is called valid if:
    - The sum of the values of the selected nodes is divisible by k.
    - No two selected nodes are adjacent in the tree (no node and its direct parent are both included in the subset).
Return the number of valid subsets modulo 109 + 7.

Example 1:
    Input: parent = [-1,0,1], nums = [1,2,3], k = 3
    Output: 1
    Explanation:
    The only valid subset is {2}. It contains node 2 with value 3, which is divisible by 3.
Example 2:
    Input: parent = [-1,0,0,0], nums = [2,1,2,1], k = 3
    Output: 2
    Explanation:
    The valid subsets are:
    {1, 2}: Nodes 1 and 2 are both children of node 0 and not directly connected to each other. Their values sum to 1 + 2 = 3, which is divisible by 3.
    {2, 3}: Nodes 2 and 3 are also non-adjacent. Their values sum to 2 + 1 = 3, which is divisible by 3.
    No other subset satisfies both conditions. Therefore, the answer is 2.

Constraints:
    1. n == parent.length == nums.length
    2. 1 <= n <= 1000
    3. parent[0] == -1
    4. For all 1 <= i < n:
        - 0 <= parent[i] < i
    5. 1 <= nums[i] <= 109
    6. 1 <= k <= 100​​​​​​​​​​​​​​​​​​​​​
    7. parent describes a valid rooted tree.
'''
MOD = 10**9+7
# === 3749ms && 21.56MB === #
class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for u, p in enumerate(parent):
            graph[p].append(u)

        def dfs(u):
            f0, f1 = [0 for _ in range(k)], [0 for _ in range(k)]
            f0[0] = 1
            f1[nums[u] % k] = 1
            for v in graph[u]:
                nf0, nf1 = [0 for _ in range(k)], [0 for _ in range(k)]
                g0, g1 = dfs(v)
                for i in range(k):
                    if f0[i] == 0:
                        continue
                    for j in range(k):
                        nf0[(i+j) % k] = (nf0[(i+j) % k] + f0[i] * g0[j] + f0[i] * g1[j]) % MOD
                for i in range(k):
                    if f1[i] == 0:
                        continue
                    for j in range(k):
                        nf1[(i+j) % k] = (nf1[(i+j) % k] + f1[i] * g0[j]) % MOD
                f0, f1 = nf0, nf1
            return f0, f1

        f0, f1 = dfs(0)
        return (f0[0] + f1[0] - 1) % MOD
