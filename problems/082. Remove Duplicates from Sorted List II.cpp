/*
=== 82. Remove Duplicates from Sorted List II ===

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
    Input: 1->2->3->3->4->4->5
    Output: 1->2->5
Example 2:
    Input: 1->1->1->2->3
    Output: 2->3
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// === 8ms(37.33%) && 7.9MB(100%) === //
// === 4ms(92.63%) && 7.5MB(100%) === // 注释掉free()函数
struct ListNode* delete_duplicate_head(struct ListNode* head){
    if(head == NULL || head -> next == NULL){
        return head;
    }
    struct ListNode* next = head -> next;
    if(next -> val != head -> val){
        return head;
    }
    while(next && next->val == head->val){
        struct ListNode* tmp = next;
        next = next -> next;
        free(tmp);
    }
    free(head);
    return delete_duplicate_head(next);
}
struct ListNode* deleteDuplicates(struct ListNode* head){
    head = delete_duplicate_head(head);
    if(head == NULL){
        return head;
    }
    struct ListNode* tmp = head;
    while(tmp && tmp -> next){
        struct ListNode* next = tmp -> next;
        next = delete_duplicate_head(next);
        tmp -> next = next;
        tmp = tmp -> next;
    }
    return head;
}

