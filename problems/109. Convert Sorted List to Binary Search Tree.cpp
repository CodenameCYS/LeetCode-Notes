/*
=== 109. Convert Sorted List to Binary Search Tree ===

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

- Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* ArrToBST(int* arr, int arr_size){
    if(arr_size <= 0){
        return NULL;
    }
    int mid = (arr_size - 1) / 2;
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node -> val = arr[mid];
    node -> left = ArrToBST(arr, mid);
    node -> right = ArrToBST(&arr[mid + 1], arr_size-mid-1);
    return node;
}
// === 16ms(75.76%) && 22.2MB(100%) === //
struct TreeNode* sortedListToBST(struct ListNode* head){
    int arr[60000], arr_size = 0;
    while(head){
        arr[arr_size] = head -> val;
        ++ arr_size;
        head = head -> next;
    }
    return ArrToBST(arr, arr_size);
}
// ========================================================================================= //
int getLength(struct ListNode* head)
{
    int len = 0;
    struct ListNode* temp = head;
    while(temp!=NULL)
    {
        temp = temp->next;
        len++;
    }
    
    return len;
}
struct TreeNode* BST(struct ListNode** head, int len)
{
    if (len<=0)
        return NULL;
    int mid = (int)floor(len/2);
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    //printf("%d %d %d\n", (*head)->val, len, mid);
    struct TreeNode* left = BST(head, mid);
    root->val = (*head)->val;
    (*head) = (*head)->next;
    //printf("Right: %d %d %d\n", (*head)->val, len, mid);
    struct TreeNode* right = BST(head, len - mid - 1);
    root->left = left;
    root->right = right;
    return root;
}
// === 12ms === //
struct TreeNode* sortedListToBST(struct ListNode* head){
    int len = getLength(head);
    return BST(&head, len);
}