'''
=== 968. Binary Tree Cameras ===

Given a binary tree, we install cameras on the nodes of the tree. 
Each camera at a node can monitor its parent, itself, and its immediate children.
Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:
    Input: [0,0,null,0,0]
    Output: 1
    Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:
    Input: [0,0,null,0,null,0,null,null,0]
    Output: 2
    Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:
    1. The number of nodes in the given tree will be in the range [1, 1000].
    2. Every node has value 0.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
# === 88ms(13.74%) && 15.1MB(5.06%) === #
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:    

        @lru_cache(None)
        def dfs(root, state):
            if root is None:
                return 0
            if state == 2:
                return 1 + dfs(root.left, 0) + dfs(root.right, 0)
            elif state == 0:
                return min(1 + dfs(root.left, 0) + dfs(root.right, 0), dfs(root.left, 1) + dfs(root.right, 1))
            elif state == 1:
                ans = 1 + dfs(root.left, 0) + dfs(root.right, 0)
                if root.left:
                    ans = min(ans, dfs(root.left, 2) + dfs(root.right, 1))
                if root.right:
                    ans = min(ans, dfs(root.left, 1) + dfs(root.right, 2))
                return ans
            
        return dfs(root, 1)