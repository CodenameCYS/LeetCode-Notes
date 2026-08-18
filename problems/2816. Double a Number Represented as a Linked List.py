'''
=== 2816. Double a Number Represented as a Linked List ===

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
Return the head of the linked list after doubling it.

Example 1:
    Input: head = [1,8,9]
    Output: [3,7,8]
    Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.
Example 2:
    Input: head = [9,9,9]
    Output: [1,9,9,8]
    Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
 
Constraints:
    1. The number of nodes in the list is in the range [1, 104]
    2. 0 <= Node.val <= 9
    3. The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# === 971ms && 22.1MB === #
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        
        new_nodes = []
        remain = 0
        for v in nodes[::-1]:
            val = (v * 2 + remain) % 10
            remain = (v * 2 + remain) // 10
            new_nodes.insert(0, val)
        if remain != 0:
            new_nodes.insert(0, remain)
            
        new_nodes = [ListNode(val) for val in new_nodes]
        n = len(new_nodes)
        for i in range(n-1):
            new_nodes[i].next = new_nodes[i+1]
        return new_nodes[0]