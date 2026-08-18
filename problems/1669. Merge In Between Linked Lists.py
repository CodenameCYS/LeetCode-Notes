'''
=== 1669. Merge In Between Linked Lists ===

You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
The blue edges and nodes in the following figure incidate the result:
Build the result list and return its head.

Example 1:
    Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
    Output: [0,1,2,1000000,1000001,1000002,5]
    Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
Example 2:
    Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
    Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
    Explanation: The blue edges and nodes in the above figure indicate the result.
 
Constraints:
    1. 3 <= list1.length <= 104
    2. 1 <= a <= b < list1.length - 1
    3. 1 <= list2.length <= 104
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# === 476ms && 20.2MB === #
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p0 = list1
        counter = 0
        while p0:
            if counter == a-1:
                p_st = p0
            elif counter == b+1:
                p_ed = p0
                break
            p0 = p0.next
            counter += 1
            
        p_st.next = list2
        p0 = list2
        while p0.next:
            p0 = p0.next
        p0.next = p_ed
        return list1
        
        