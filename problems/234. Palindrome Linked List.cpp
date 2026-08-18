/*
=== 234. Palindrome Linked List ===

Given a singly linked list, determine if it is a palindrome.

Example 1:
    Input: 1->2
    Output: false
Example 2:
    Input: 1->2->2->1
    Output: true

Follow up:
    Could you do it in O(n) time and O(1) space?
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// === 12ms(90.53%) & 11.3MB(38.64%) === //
bool isPalindrome(struct ListNode* head){
    int size = 0;
    int mem[100000];
    while(head){
        mem[size] = head->val;
        head = head -> next;
        ++size;
    }
    for(int i=0; i<size/2; ++i){
        if(mem[i] != mem[size-1-i]){
            return false;
        }
    }
    return true;
}

