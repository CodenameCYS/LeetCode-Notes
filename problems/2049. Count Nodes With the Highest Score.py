'''
=== 2049. Count Nodes With the Highest Score ===

There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.
Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.
Return the number of nodes that have the highest score.

Example 1:
    example-1
    Input: parents = [-1,2,0,2,0]
    Output: 3
    Explanation:
    - The score of node 0 is: 3 * 1 = 3
    - The score of node 1 is: 4 = 4
    - The score of node 2 is: 1 * 1 * 2 = 2
    - The score of node 3 is: 4 = 4
    - The score of node 4 is: 4 = 4
    The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
Example 2:
    example-2
    Input: parents = [-1,2,0]
    Output: 2
    Explanation:
    - The score of node 0 is: 2 = 2
    - The score of node 1 is: 2 = 2
    - The score of node 2 is: 1 * 1 = 1
    The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
 
Constraints:
    1. n == parents.length
    2. 2 <= n <= 105
    3. parents[0] == -1
    4. 0 <= parents[i] <= n - 1 for i != 0
    5. parents represents a valid binary tree.
'''
# === 3107ms && 54.9MB === #
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        cnt = defaultdict(int)
        children = defaultdict(list)
        
        for i, p in enumerate(parents):
            if p == -1:
                continue
            cnt[p] += 1
            children[p].append(i)
            
        subs = [0 for _ in range(n)]
        s = [u for u in range(n) if cnt[u] == 0]
        while s:
            u = s.pop(0)
            subs[u] = 1
            for v in children[u]:
                subs[u] += subs[v]
            p = parents[u]
            cnt[p] -= 1
            if cnt[p] == 0:
                s.append(p)
        # print(children)
        # print(subs)
        
        def cal_score(u):
            k = 1
            res = 1
            for v in children[u]:
                res *= subs[v]
                k += subs[v]
            res = res * (n-k) if k != n else res
            return res
        
        scores = [cal_score(u) for u in range(n)]
        # print(scores)
        max_score = max(scores)
        return len([u for u in range(n) if scores[u] == max_score])
            