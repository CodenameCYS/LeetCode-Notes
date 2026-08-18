/*
=== 203. Remove Linked List Elements ===

Remove all elements from a linked list of integers that have value val.

Example:
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    while(head && head -> val == val){
        struct ListNode* p = head -> next;
        free(head);
        head = p;
    }
    if(!head){
        return head;
    }
    struct ListNode *last, *p;
    last = head;
    p = head -> next;
    while(p){
        if(p -> val != val){
            last = p;
            p = p->next;
        }
        else{
            last -> next = p -> next;
            free(p);
            p = last -> next;
        }
    }
    return head;
}