'''
=== 3997. Count Dominant Nodes in a Binary Tree ===

You are given the root of a complete binary tree.
A node x is called dominant if its value is equal to the maximum value among all nodes in the subtree rooted at x.
Return the number of dominant nodes in the tree.

Example 1:
    Input: root = [5,3,8,2,4,7,1]
    Output: 5
    Explanation:
    The leaf nodes with values 2, 4, 7, and 1 are dominant.
    The node with value 8 is dominant because its value is the maximum value in its subtree [8, 7, 1].
    Thus, the answer is 5.
Example 2:
    Input: root = [1,2,3,1,2]
    Output: 4
    Explanation:
    The leaf nodes with values 1, 2, and 3 are dominant.
    The node with value 2 whose subtree is [2, 1, 2] is dominant because its value is the maximum value in its subtree.
    Thus, the answer is 4.
 
Constraints:
    1. The number of nodes in the tree is in the range [1, 105].
    2. 1 <= Node.val <= 109
    3. The tree is guaranteed to be a complete binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# === 191ms && 49.36MB === #
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        
        def dfs(node):
            cnt, val = 0, node.val
            if node.left:
                _cnt, _val = dfs(node.left)
                val = max(_val, val)
                cnt += _cnt
            if node.right:
                _cnt, _val = dfs(node.right)
                val = max(_val, val)
                cnt += _cnt
            if val == node.val:
                cnt += 1
            return cnt, val
        
        ans, _ = dfs(root)
        return ans