/*
=== 143. Reorder List ===

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
    Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:
    Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// === 16ms(89.52%) && 10.6MB(33.33%) === //
void reorderList(struct ListNode* head){
    struct ListNode* record[100000];
    int size = 0;
    struct ListNode* flag = head;
    while(flag){
        record[size] = flag;
        flag = flag -> next;
        ++ size;
    }
    // for(int i=0; i<size; ++i){
    //     printf("%d\t", record[i]->val);
    // }
    // printf("\n");
    for(int i=0; i<(size+1)/2-1; ++i){
        struct ListNode* s1 = record[i];
        struct ListNode* s2 = record[i+1];
        struct ListNode* s3 = record[size-i-1];
        s1 -> next = s3;
        s3 -> next = s2;
    }
    record[size/2] -> next = NULL;
}

