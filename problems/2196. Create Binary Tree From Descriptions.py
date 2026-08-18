'''
=== 2196. Create Binary Tree From Descriptions ===

You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,
    - If isLefti == 1, then childi is the left child of parenti.
    - If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.
The test cases will be generated such that the binary tree is valid.

Example 1:
    Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
    Output: [50,20,80,15,17,19]
    Explanation: The root node is the node with value 50 since it has no parent.
    The resulting binary tree is shown in the diagram.
Example 2:
    Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
    Output: [1,2,null,null,3,4]
    Explanation: The root node is the node with value 1 since it has no parent.
    The resulting binary tree is shown in the diagram.
 
Constraints:
    1. 1 <= descriptions.length <= 104
    2. descriptions[i].length == 3
    3. 1 <= parenti, childi <= 105
    4. 0 <= isLefti <= 1
    5. The binary tree described by descriptions is valid.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# === 3408ms && 35.9MB === #
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = defaultdict(list)
        deg = defaultdict(int)
        for u, v, s in descriptions:
            graph[u].append((v, s))
            deg[v] += 1
        
        def dfs(u):
            root = TreeNode(u)
            for v, s in graph[u]:
                if s == 0:
                    root.right = dfs(v)
                else:
                    root.left = dfs(v)
            return root
        
        root = [u for u in graph if deg[u] == 0][0]
        return dfs(root)
            