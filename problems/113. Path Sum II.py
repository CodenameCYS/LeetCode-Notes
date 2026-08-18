'''
=== 113. Path Sum II ===

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# === 44ms(83.22%) && 17.4MB(37.93%) === #
class Solution:
    def traverse(self, root: TreeNode, sum: int, tmp_sum: int, stack: List[int], ans: List[List[int]]):
        if root is None:
            return
        elif root.left is None and root.right is None:
            if tmp_sum + root.val == sum:
                ans.append(stack + [root.val])
        else:
            self.traverse(root.left, sum, tmp_sum + root.val, stack+[root.val], ans)
            self.traverse(root.right, sum, tmp_sum + root.val, stack+[root.val], ans)
        return
                
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        self.traverse(root, sum, 0, [], ans)
        return ans