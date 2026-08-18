'''
=== 449. Serialize and Deserialize BST ===

Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.

Example 1:
    Input: root = [2,1,3]
    Output: [2,1,3]
Example 2:
    Input: root = []
    Output: []
 
Constraints:
    1. The number of nodes in the tree is in the range [0, 104].
    2. 0 <= Node.val <= 104
    3. The input tree is guaranteed to be a binary search tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# === 76ms(80.19%) && 18.2MB === #
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(root):
            if root is None:
                return []
            return [root.val] + dfs(root.left) + dfs(root.right)
        
        return " ".join([str(val) for val in dfs(root)])
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nodes = [int(val) for val in data.split()]
        
        def build(nodes):
            if len(nodes) == 0:
                return None
            root = TreeNode(nodes[0])
            i = bisect.bisect(nodes[1:], nodes[0]) + 1
            root.left = build(nodes[1:i])
            root.right = build(nodes[i:])
            return root
        
        return build(nodes)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans