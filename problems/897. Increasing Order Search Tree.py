'''
=== 897. Increasing Order Search Tree ===

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:
    Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:
    Input: root = [5,1,7]
    Output: [1,null,5,null,7]
 
Constraints:
    1. The number of nodes in the given tree will be in the range [1, 100].
    2. 0 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# === 28ms(83.05%) && 14.3MB(21.82%) === #
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        
        def dfs(root):
            nonlocal nodes
            if root is None:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
            return
        
        nodes = []
        dfs(root)
        for i, node in enumerate(nodes[:-1]):
            node.right = nodes[i+1]
            node.left = None
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]