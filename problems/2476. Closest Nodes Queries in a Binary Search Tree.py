'''
=== 2476. Closest Nodes Queries in a Binary Search Tree ===

You are given the root of a binary search tree and an array queries of size n consisting of positive integers.
Find a 2D array answer of size n where answer[i] = [mini, maxi]:
    - mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
    - maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
Return the array answer.

Example 1:
    Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
    Output: [[2,2],[4,6],[15,-1]]
    Explanation: We answer the queries in the following way:
    - The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
    - The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
    - The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].
Example 2:
    Input: root = [4,null,9], queries = [3]
    Output: [[-1,4]]
    Explanation: The largest number that is smaller or equal to 3 in the tree does not exist, and the smallest number that is greater or equal to 3 is 4. So the answer for the query is [-1,4].
 
Constraints:
    1. The number of nodes in the tree is in the range [2, 105].
    2. 1 <= Node.val <= 106
    3. n == queries.length
    4. 1 <= n <= 105
    5. 1 <= queries[i] <= 106
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# === 1540ms && 157.6MB === #
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals = []
        
        def dfs(root):
            nonlocal vals
            if root is None:
                return
            dfs(root.left)
            vals.append(root.val)
            dfs(root.right)
            return
        
        dfs(root)
        
        def query(q):
            idx = bisect.bisect_left(vals, q)
            if idx == len(vals):
                return [vals[-1], -1]
            elif vals[idx] == q:
                return [q, q]
            elif idx == 0:
                return [-1, vals[0]]
            else:
                return [vals[idx-1], vals[idx]]
        
        return [query(q) for q in queries]
        