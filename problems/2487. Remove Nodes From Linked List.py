'''
=== 2487. Remove Nodes From Linked List ===

You are given the head of a linked list.
Remove every node which has a node with a strictly greater value anywhere to the right side of it.
Return the head of the modified linked list.

Example 1:
    Input: head = [5,2,13,3,8]
    Output: [13,8]
    Explanation: The nodes that should be removed are 5, 2 and 3.
    - Node 13 is to the right of node 5.
    - Node 13 is to the right of node 2.
    - Node 8 is to the right of node 3.
Example 2:
    Input: head = [1,1,1,1]
    Output: [1,1,1,1]
    Explanation: Every node has value 1, so no nodes are removed.
 
Constraints:
    1. The number of the nodes in the given list is in the range [1, 105].
    2. 1 <= Node.val <= 105
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# === 3748ms && 76.8MB === #
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = []
        while head:
            while s != [] and s[-1] < head.val:
                s.pop()
            s.append(head.val)
            head = head.next
        
        ret = ListNode(s[0])
        p = ret
        for v in s[1:]:
            node = ListNode(v)
            p.next = node
            p = node
        return ret
        