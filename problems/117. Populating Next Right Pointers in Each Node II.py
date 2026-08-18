'''
=== 117. Populating Next Right Pointers in Each Node II ===

Given a binary tree
    struct Node {
        int val;
        Node *left;
        Node *right;
        Node *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Follow up:
    - You may only use constant extra space.
    - Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 
Example 1:
    Input: root = [1,2,3,4,5,null,7]
    Output: [1,#,2,3,#,4,5,7,#]
    Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Constraints:
    1. The number of nodes in the given tree is less than 6000.
    2. -100 <= node.val <= 100
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# === 48ms(84.10%) && 15.1MB(10.04%) === #
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        last_node = None
        queue = [root]
        next_queue = []
        while queue != []:
            node = queue.pop(0)
            node.next = last_node
            if node.right:
                next_queue.append(node.right)
            if node.left:
                next_queue.append(node.left)
            if queue == []:
                last_node = None
                queue = next_queue
                next_queue = []
            else:
                last_node = node
        return root
