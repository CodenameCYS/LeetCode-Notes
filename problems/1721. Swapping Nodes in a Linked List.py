'''
=== 1721. Swapping Nodes in a Linked List ===

You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [1,4,3,2,5]
Example 2:
    Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
    Output: [7,9,6,6,8,7,3,0,9,5]
Example 3:
    Input: head = [1], k = 1
    Output: [1]
Example 4:
    Input: head = [1,2], k = 1
    Output: [2,1]
Example 5:
    Input: head = [1,2,3], k = 2
    Output: [1,2,3]
 
Constraints:
    1. The number of nodes in the list is n.
    2. 1 <= k <= n <= 105
    3. 0 <= Node.val <= 100
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# === 1144ms && 48.9MB === #
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        def count_len(head):
            l = 0
            while head:
                l += 1
                head = head.next
            return l
        # print(head)
        n = count_len(head)
        i, j = k, n-k+1
        # nodei, nodej = None, None
        if i == j:
            return head
        p = head
        for k in range(1, n+1):
            if k == i:
                nodei = p
            if k == j:
                nodej = p
            if k > max(i, j):
                break
            p = p.next
        nodei.val, nodej.val = nodej.val, nodei.val
        return head
            