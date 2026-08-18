/*
=== 206. Reverse Linked List ===

Reverse a singly linked list.

Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

Follow up:
    A linked list can be reversed either iteratively or recursively. Could you implement both?
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    if(!head){
        return NULL;
    }
    struct ListNode* p = (struct ListNode*)malloc(sizeof(struct ListNode));
    p -> val = head -> val;
    p -> next = NULL;
    struct ListNode* temp = head -> next;
    struct ListNode* newhead = p;
    while(temp){
        p = (struct ListNode*)malloc(sizeof(struct ListNode));
        p -> val = temp -> val;
        p -> next = newhead;
        newhead = p;
        temp = temp -> next;
    }
    return newhead;
}