'''
=== 817. Linked List Components ===

We are given head, the head node of a linked list containing unique integer values.
We are also given the list G, a subset of the values in the linked list.
Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:
    Input: 
    head: 0->1->2->3
    G = [0, 1, 3]
    Output: 2
    Explanation: 
    0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:
    Input: 
    head: 0->1->2->3->4
    G = [0, 3, 1, 4]
    Output: 2
    Explanation: 
    0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

Note:
    1. If N is the length of the linked list given by head, 1 <= N <= 10000.
    2. The value of each node in the linked list will be in the range [0, N - 1].
    3. 1 <= G.length <= 10000.
    4. G is a subset of all values in the linked list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# === 116ms(47.46%) && 18MB(25%) === #
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        cache = {g: 0 for g in G}
        is_consective = False
        ans = 0
        while head:
            if head.val in cache.keys() and cache[head.val] == 0:
                cache[head.val] = 1
                if not is_consective:
                    ans += 1
                    is_consective = True
            else:
                is_consective = False
            head = head.next
        return ans