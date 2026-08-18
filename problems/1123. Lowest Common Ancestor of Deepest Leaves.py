'''
=== 1123. Lowest Common Ancestor of Deepest Leaves ===

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
Recall that:
    - The node of a binary tree is a leaf if and only if it has no children
    - The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
    - The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

Note: This question is the same as 865: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]
    Explanation: We return the node with value 2, colored in yellow in the diagram.
    The nodes coloured in blue are the deepest leaf-nodes of the tree.
    Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.
Example 2:
    Input: root = [1]
    Output: [1]
    Explanation: The root is the deepest node in the tree, and it's the lca of itself.
Example 3:
    Input: root = [0,1,3,null,2]
    Output: [2]
    Explanation: The deepest leaf node in the tree is 2, the lca of one node is itself.
 
Constraints:
    1. The number of nodes in the tree will be in the range [1, 1000].
    2. 0 <= Node.val <= 1000
    3. The values of the nodes in the tree are unique.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# === 56ms(21.23%) && 14.8MB(17.24%) === #
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        depth = {}
        
        def dfs1(root):
            if root is None:
                depth[None] = 0
                return 0
            depth[root] = 1 + max(dfs1(root.left), dfs1(root.right))
            return depth[root]
        
        def dfs2(root):
            if root is None:
                return root
            if depth[root.left] == depth[root.right]:
                return root
            elif depth[root.left] > depth[root.right]:
                return dfs2(root.left)
            else:
                return dfs2(root.right)
            
        dfs1(root)
        return dfs2(root)