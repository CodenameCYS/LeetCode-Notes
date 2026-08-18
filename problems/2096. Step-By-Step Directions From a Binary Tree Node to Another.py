'''
=== 2096. Step-By-Step Directions From a Binary Tree Node to Another ===

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
    - 'L' means to go from a node to its left child node.
    - 'R' means to go from a node to its right child node.
    - 'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Example 1:
    Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
    Output: "UURL"
    Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:
    Input: root = [2,1], startValue = 2, destValue = 1
    Output: "L"
    Explanation: The shortest path is: 2 → 1.
 
Constraints:
    1. The number of nodes in the tree is n.
    2. 2 <= n <= 105
    3. 1 <= Node.val <= n
    4. All the values in the tree are unique.
    5. 1 <= startValue, destValue <= n
    6. startValue != destValue
'''
# === 1316ms && 160.2MB === #
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        nodes ={}
        def dfs(root, p):
            nonlocal nodes
            if root is None:
                return
            nodes[root.val] = (p, root.left, root.right)
            dfs(root.left, root)
            dfs(root.right, root)
            return
        dfs(root, None)
        
        s, val = [startValue], startValue
        while True:
            u, l, r = nodes[val]
            if u is None:
                break
            s.append(u.val)
            val = u.val
            
        s = {v:idx for idx, v in enumerate(s)}
        t, path = destValue, ""
        while t not in s:
            u, l, r = nodes[t]
            if u.left and u.left.val == t:
                path = "L" + path
            else:
                path = "R" + path
            t = u.val
        return "U" * s[t] + path
