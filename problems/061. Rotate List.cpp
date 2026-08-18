/*
=== 61. Rotate List ===

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    if(!head){
        return NULL;
    }
    
    int len = 0;
    struct ListNode* p = head;
    while(p){
        p = p->next;
        ++ len;
    }
    k = k % len;
    
    struct ListNode* ans = NULL;
    struct ListNode* rpart = NULL;
    struct ListNode* pa;
    p = head;
    for(int i=0; i<len-k; ++i){
        struct ListNode* temp = (struct ListNode*)malloc(sizeof(struct ListNode));
        temp -> val = p -> val;
        temp -> next = NULL;
        if(rpart == NULL){
            rpart = temp;
            pa = rpart;
        }
        else{
            pa->next = temp;
            pa = pa->next;
        }
        p = p->next;
    }
    if(k == 0){
        return rpart;
    }
    for(int i=0; i<k; ++i){
        struct ListNode* temp = (struct ListNode*)malloc(sizeof(struct ListNode));
        temp -> val = p -> val;
        temp -> next = NULL;
        if(ans == NULL){
            ans = temp;
            pa = ans;
        }
        else{
            pa->next = temp;
            pa = pa->next;
        }
        p = p->next;
    }
    pa -> next = rpart;
    return ans;
}