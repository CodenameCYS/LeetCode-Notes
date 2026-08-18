'''
=== 124. Binary Tree Maximum Path Sum ===

Given the root of a binary tree, return the maximum path sum.
For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
    Input: root = [1,2,3]
    Output: 6
Example 2:
    Input: root = [-10,9,20,null,null,15,7]
    Output: 42
 
Constraints:
    1. The number of nodes in the tree is in the range [1, 3 * 104].
    2. -1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# === 100ms(15.35%) && 21.8MB(32.32%) === #
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
    
        res = -math.inf

        def dfs(root):
            nonlocal res
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            res = max(res, root.val + l + r, root.val+l, root.val+r, root.val)
            return root.val + max(l, r, 0)

        dfs(root)
        return res 