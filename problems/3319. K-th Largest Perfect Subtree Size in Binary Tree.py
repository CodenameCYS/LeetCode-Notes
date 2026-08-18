'''
=== 3319. K-th Largest Perfect Subtree Size in Binary Tree ===

You are given the root of a binary tree and an integer k.
Return an integer denoting the size of the kth largest perfect binary subtree, or -1 if it doesn't exist.
A perfect binary tree is a tree where all leaves are on the same level, and every parent has two children.

Example 1:
    Input: root = [5,3,6,5,2,5,7,1,8,null,null,6,8], k = 2
    Output: 3
    Explanation:
    The roots of the perfect binary subtrees are highlighted in black. Their sizes, in decreasing order are [3, 3, 1, 1, 1, 1, 1, 1].
    The 2nd largest size is 3.
Example 2:
    Input: root = [1,2,3,4,5,6,7], k = 1
    Output: 7
    Explanation:
    The sizes of the perfect binary subtrees in decreasing order are [7, 3, 3, 1, 1, 1, 1]. The size of the largest perfect binary subtree is 7.
Example 3:
    Input: root = [1,2,3,null,4], k = 3
    Output: -1
    Explanation:
    The sizes of the perfect binary subtrees in decreasing order are [1, 1]. There are fewer than 3 perfect binary subtrees.

Constraints:
    1. The number of nodes in the tree is in the range [1, 2000].
    2. 1 <= Node.val <= 2000
    3. 1 <= k <= 1024
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# === 129ms && 17.3MB === #
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        perfect_subtree = []
        
        def dfs(root):
            nonlocal perfect_subtree
            if root is None:
                return True, 0
            left_is_perfect, left_cnt = dfs(root.left)
            right_is_perfect, right_cnt = dfs(root.right)
            if left_is_perfect and right_is_perfect and left_cnt == right_cnt:
                perfect_subtree.append(left_cnt + right_cnt + 1)
                return True, left_cnt + right_cnt + 1
            else:
                return False, left_cnt + right_cnt + 1
            
        dfs(root)
        perfect_subtree = sorted(perfect_subtree, reverse=True)
        return perfect_subtree[k-1] if len(perfect_subtree) >= k else -1