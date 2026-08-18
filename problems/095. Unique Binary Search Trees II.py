'''
=== 95. Unique Binary Search Trees II ===

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# === 48ms(97.88%) && 13.6MB(100%) === #
class Solution:
    def dp(self, st, ed):
        if st > ed:
            return [None]
        if st == ed:
            return [TreeNode(st)]
        if (st, ed) in self.cache.keys():
            return self.cache[(st,ed)]
        ans = []
        for i in range(st, ed+1):
            left_list = self.dp(st, i-1)
            right_list = self.dp(i+1, ed)
            for left in left_list:
                for right in right_list:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    ans.append(root)
        self.cache[(st, ed)] = ans
        return ans
                
        
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        self.cache = {}
        return self.dp(1, n)