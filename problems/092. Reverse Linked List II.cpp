/*
=== 92. Reverse Linked List II ===

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// === 4ms(54.68%) && 7.2MB(50%) === //
struct ListNode* reverseBetween(struct ListNode* head, int m, int n){
    int count = 1;
    struct ListNode* lastnode = NULL;
    struct ListNode* ans = head;
    while(head){
        if(count < m){
            lastnode = head;
            head = head -> next;
            ++ count;
        }
        else if(count >= m && count <= n){
            struct ListNode* tmphead = NULL;
            struct ListNode* nextlastnode = head;
            while(head && count >= m && count <= n){
                struct ListNode* tmp = head;
                head = head -> next;
                tmp -> next = tmphead;
                tmphead = tmp;
                ++ count;
            }
            if(m == 1){
                ans = tmphead;
            }
            else{
                lastnode -> next = tmphead;
            }
            lastnode = nextlastnode;
        }
        else{
            lastnode -> next = head;
            return ans;
        }
    }
    return ans;
}

