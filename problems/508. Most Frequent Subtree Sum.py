'''
=== 508. Most Frequent Subtree Sum ===

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:
  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:
  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import statistics
# === 60ms(19.53%) && 16.7MB(100%) === #
class Solution:
    def traverse(self, root):
        if root is None:
            return 0
        ans = root.val + self.traverse(root.left) + self.traverse(root.right)
        self.counter.append(ans)
        return ans
        
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.counter = []
        self.traverse(root)
        return statistics.multimode(self.counter)