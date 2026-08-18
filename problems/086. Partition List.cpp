/*
=== 86. Partition List ===

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// === 4ms(84.48%) && 7.1MB(100%) === //
struct ListNode* partition(struct ListNode* head, int x){
    struct ListNode* lhead;
    struct ListNode* lend;
    struct ListNode* ghead;
    struct ListNode* gend;
    lhead = NULL;
    ghead = NULL;
    while(head){
        struct ListNode* tmp = head;
        head = head -> next;
        if(tmp -> val < x){
            if(lhead == NULL){
                lhead = tmp;
                lhead -> next = NULL;
                lend = lhead;
            }
            else{
                lend -> next = tmp;
                lend = tmp;
                tmp -> next = NULL;
            }
        }
        else{
            if(ghead == NULL){
                ghead = tmp;
                ghead -> next = NULL;
                gend = ghead;
            }
            else{
                gend -> next = tmp;
                gend = tmp;
                tmp -> next = NULL;
            }
        }
    }
    if(lhead){
        lend -> next = ghead;
        return lhead;
    }
    else{
        return ghead;
    }
}

