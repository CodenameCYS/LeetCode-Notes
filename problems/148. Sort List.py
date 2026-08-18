'''
=== 148. Sort List ===

Given the head of a linked list, return the list after sorting it in ascending order.
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]
Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]
Example 3:
    Input: head = []
    Output: []
 
Constraints:
    1. The number of nodes in the list is in the range [0, 5 * 104].
    2. -105 <= Node.val <= 105
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# === 80ms(99.30%) && 21.3MB === #
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def countlen(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length
        
        n = countlen(head)
        vals = [0 for _ in range(n)]
        p = head
        for i in range(n):
            vals[i] = p.val
            p = p.next
        vals = sorted(vals)
        p = head
        for i in range(n):
            p.val = vals[i]
            p = p.next
        return head