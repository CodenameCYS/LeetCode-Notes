'''
=== 429. N-ary Tree Level Order Traversal ===

Given an n-ary tree, return the level order traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [[1],[3,2,4],[5,6]]
Example 2:
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 
Constraints:
    1. The height of the n-ary tree is less than or equal to 1000
    2. The total number of nodes is between [0, 10^4]
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# === 64ms(17.64%) && 14.4MB(100%) === #
class Solution:
    def traverse(self, root, level, ans):
        if root is None:
            return
        if level >= len(ans) :
            ans += [[] for i in range(len(ans) - level + 1)]
        ans[level].append(root.val)
        for c in root.children:
            self.traverse(c, level+1, ans)
            
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        self.traverse(root, 0, ans)
        return ans