'''
=== 501. Find Mode in Binary Search Tree ===

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
Assume a BST is defined as follows:
    1. The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    2. The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    3. Both the left and right subtrees must also be binary search trees.
 
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# === 60ms(42.40%) && 16.6MB(100%) === #
class Solution:
    def traverse(self, root, record):
        if root is None:
            return
        if root.val in record.keys():
            record[root.val] += 1
        else:
            record[root.val] = 1
        self.traverse(root.left, record)
        self.traverse(root.right, record)
        
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        record = {}
        self.traverse(root, record)
        record = sorted(record.items(), key = lambda x: x[1], reverse = True)
        ans = []
        for r in record:
            if r[1] == record[0][1]:
                ans.append(r[0])
            else:
                break
        return ans