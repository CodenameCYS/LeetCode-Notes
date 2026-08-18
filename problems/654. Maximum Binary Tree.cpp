/*
=== 654. Maximum Binary Tree ===

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
    1. The root is the maximum number in the array.
    2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
    Input: [3,2,1,6,0,5]
    Output: return the tree root node representing the following tree:
      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

Note:
    - The size of the given array will be in the range [1,1000].
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// === 48ms(7.59%) & 29.2MB(100%) === //
struct TreeNode* constructMaximumBinaryTree(int* nums, int numsSize) {
    if(numsSize == 0){
        return NULL;
    }
    struct TreeNode* root = NULL;
    for(int i=0; i<numsSize; ++i){
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node -> val = nums[i];
        node -> left = NULL;
        node -> right = NULL;
        if(root == NULL || root->val < node->val){
            node->left = root;
            root = node;
        }
        else{
            struct TreeNode* temp = root;
            while(temp->right && temp->right->val > node->val){
                temp = temp -> right;
            }
            node -> left = temp -> right;
            temp -> right =node;
        }
    }
    return root;
}