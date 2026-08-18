'''
=== 971. Flip Binary Tree To Match Preorder Traversal ===

You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.
Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:
Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.
Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].

Example 1:
    Input: root = [1,2], voyage = [2,1]
    Output: [-1]
    Explanation: It is impossible to flip the nodes such that the pre-order traversal matches voyage.
Example 2:
    Input: root = [1,2,3], voyage = [1,3,2]
    Output: [1]
    Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal matches voyage.
Example 3:
    Input: root = [1,2,3], voyage = [1,2,3]
    Output: []
    Explanation: The tree's pre-order traversal already matches voyage, so no nodes need to be flipped.
 
Constraints:
    1. The number of nodes in the tree is n.
    2. n == voyage.length
    3. 1 <= n <= 100
    4. 1 <= Node.val, voyage[i] <= n
    5. All the values in the tree are unique.
    6. All the values in voyage are unique.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# === 28ms(96.13%) && 14.5MB === #
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        def flip(root, voyage):
            nonlocal res
            if voyage[0] != root.val:
                res.append(-1)
                return 
            if root.left is None and root.right is None:
                if len(voyage) != 1:
                    res.append(-1)
                return
            if len(voyage) == 1:
                res.append(-1)
                return
            if root.left is None:
                flip(root.right, voyage[1:])
                return
            if root.right is None:
                flip(root.left, voyage[1:])
                return
            if root.left.val not in voyage or root.right.val not in voyage:
                res.append(-1)
                return
            if root.left.val == voyage[1]:
                idx = voyage.index(root.right.val)
                flip(root.left, voyage[1:idx])
                flip(root.right, voyage[idx:])
            elif root.right.val == voyage[1]:
                res.append(root.val)
                idx = voyage.index(root.left.val)
                flip(root.right, voyage[1:idx])
                flip(root.left, voyage[idx:])
            else:
                res.append(-1)
            return
        
        flip(root, voyage)
        if any(x == -1 for x in res):
            return [-1]
        return res
        