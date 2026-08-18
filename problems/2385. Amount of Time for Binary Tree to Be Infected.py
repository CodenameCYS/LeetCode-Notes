'''
=== 2385. Amount of Time for Binary Tree to Be Infected === 

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
Each minute, a node becomes infected if:
    - The node is currently uninfected.
    - The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

Example 1:
    Input: root = [1,5,3,null,4,10,6,9,2], start = 3
    Output: 4
    Explanation: The following nodes are infected during:
    - Minute 0: Node 3
    - Minute 1: Nodes 1, 10 and 6
    - Minute 2: Node 5
    - Minute 3: Node 4
    - Minute 4: Nodes 9 and 2
    It takes 4 minutes for the whole tree to be infected so we return 4.
Example 2:
    Input: root = [1], start = 1
    Output: 0
    Explanation: At minute 0, the only node in the tree is infected so we return 0.
 
Constraints:
    1. The number of nodes in the tree is in the range [1, 105].
    2. 1 <= Node.val <= 105
    3. Each node has a unique value.
    4. A node with a value of start exists in the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# === 1214ms && 144.2MB === #
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = {root: None}
        u0 = None
        def dfs(root):
            nonlocal parents, u0
            if root.val == start:
                u0 = root
            if root.left:
                parents[root.left] = root
                dfs(root.left)
            if root.right:
                parents[root.right] = root
                dfs(root.right)
            return
        
        dfs(root)
        
        dis = {u0: 0}
        s = [u0]
        res = 0
        while s:
            u = s.pop(0)
            res = max(res, dis[u])
            if u.left and u.left not in dis:
                dis[u.left] = dis[u] + 1
                s.append(u.left)
            if u.right and u.right not in dis:
                dis[u.right] = dis[u] + 1
                s.append(u.right)
            if parents[u] and parents[u] not in dis:
                dis[parents[u]] = dis[u] + 1
                s.append(parents[u])
        return res
                
                
                
        