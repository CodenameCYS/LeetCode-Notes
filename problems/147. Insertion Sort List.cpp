/*
=== 147. Insertion Sort List ===

Sort a linked list using insertion sort.

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 
Algorithm of Insertion Sort:
    1. Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
    2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
    3. It repeats until no input elements remain.

Example 1:
    Input: 4->2->1->3
    Output: 1->2->3->4
Example 2:
    Input: -1->5->3->4->0
    Output: -1->0->3->4->5
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* insert_node(struct ListNode* head, struct ListNode* node){
    if(head == NULL){
        return node;
    }
    if(head -> val >= node -> val){
        node -> next = head;
        return node;
    }
    struct ListNode *last_node=head, *tmp_node=head->next;
    while(tmp_node){
        if(tmp_node -> val >= node -> val){
            last_node -> next = node;
            node -> next = tmp_node;
            return head;
        }
        else{
            last_node = tmp_node;
            tmp_node = tmp_node -> next;
        }
    }
    last_node -> next = node;
    return head;
}
// === 36ms(80.85%) && 7.8MB(100%) === //
struct ListNode* insertionSortList(struct ListNode* head){
    if(head == NULL){
        return head;
    }
    struct ListNode* node = head -> next;
    head -> next = NULL;
    while(node){
        struct ListNode* next_node = node -> next;
        node -> next = NULL;
        head = insert_node(head, node);
        node = next_node;
    }
    return head;
}

