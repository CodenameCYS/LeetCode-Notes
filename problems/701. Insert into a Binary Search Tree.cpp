/*
=== 701. Insert into a Binary Search Tree ===

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:
         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// === 48ms(62.41%) && 22.3MB(100%) === //
struct TreeNode* insertIntoBST(struct TreeNode* root, int val){
    if(root == NULL){
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node -> val = val;
        node -> left = NULL;
        node -> right = NULL;
        return node;
    }
    if(root -> val <= val){
        if(root -> right == NULL){
            struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
            node -> val = val;
            node -> left = NULL;
            node -> right = NULL;
            root -> right = node;
        }
        else{
            root -> right = insertIntoBST(root->right, val);
        }
    }
    else{
        if(root -> left == NULL){
            struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
            node -> val = val;
            node -> left = NULL;
            node -> right = NULL;
            root -> left = node;
        }
        else{
            root -> left = insertIntoBST(root->left, val);
        }
    }
    return root;
}

