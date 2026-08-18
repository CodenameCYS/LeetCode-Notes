'''
=== 687. Longest Univalue Path ===

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:
              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

Example 2:
Input:
              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

- Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# === 440ms(57.14%) && 16MB(100%) === #
class Solution:
    maxlen = 0
    
    def my_solution(self, root):
        if root is None:
            return 0
        l_len = self.my_solution(root.left)
        r_len = self.my_solution(root.right)
        l = 0
        if l_len != 0:
            if root.val == root.left.val:
                self.maxlen = max(l_len+1, self.maxlen)
                l = l_len
            else:
                self.maxlen = max(l_len, self.maxlen)
        if r_len != 0:
            if root.val == root.right.val:
                self.maxlen = max(r_len+1, self.maxlen)
                l = max(l, r_len)
            else:
                self.maxlen = max(r_len, self.maxlen)
        if l_len != 0 and r_len != 0 and root.val == root.left.val and root.val == root.right.val:
            self.maxlen = max(r_len+1+l_len, self.maxlen)
        return l + 1
        
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.maxlen = 1
        self.my_solution(root)
        return self.maxlen-1