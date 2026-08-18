'''
=== 2641. Cousins in Binary Tree II ===

Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Return the root of the modified tree.
Note that the depth of a node is the number of edges in the path from the root node to it.

Example 1:
    Input: root = [5,4,9,1,10,null,7]
    Output: [0,0,0,7,7,null,11]
    Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
    - Node with value 5 does not have any cousins so its sum is 0.
    - Node with value 4 does not have any cousins so its sum is 0.
    - Node with value 9 does not have any cousins so its sum is 0.
    - Node with value 1 has a cousin with value 7 so its sum is 7.
    - Node with value 10 has a cousin with value 7 so its sum is 7.
    - Node with value 7 has cousins with values 1 and 10 so its sum is 11.
Example 2:
    Input: root = [3,1,2]
    Output: [0,0,0]
    Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
    - Node with value 3 does not have any cousins so its sum is 0.
    - Node with value 1 does not have any cousins so its sum is 0.
    - Node with value 2 does not have any cousins so its sum is 0.
 
Constraints:
    1. The number of nodes in the tree is in the range [1, 105].
    2. 1 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# === 1526ms && 192.2MB === #
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = defaultdict(int)
        nodes = defaultdict(int)
        
        def dfs(root, depth):
            nonlocal nodes, s
            if root is None:
                return 0
            s[depth] += root.val
            lval = dfs(root.left, depth+1)
            rval = dfs(root.right, depth+1)
            nodes[root] = lval + rval
            return root.val
        
        dfs(root, 0)
        
        def rep(root, depth, parent):
            if root is None:
                return
            if parent is None:
                root.val = 0
            else:
                root.val = s[depth] - nodes[parent]
            rep(root.left, depth+1, root)
            rep(root.right, depth+1, root)
            return
        
        rep(root, 0, None)
        return root
        