/*
=== 114. Flatten Binary Tree to Linked List ===

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// === 12ms(7.41%) && 7.9MB(100%) === //
void flatten(struct TreeNode* root){
    if(root == NULL){
        return;
    }
    else if(root -> left == NULL){
        flatten(root -> right);
        return;
    }
    else if(root -> right == NULL){
        flatten(root -> left);
        root -> right = root -> left;
        root -> left = NULL;
        return;
    }
    else{
        flatten(root -> right);
        flatten(root -> left);
        struct TreeNode* tmp = root -> right;
        root -> right = root -> left;
        root -> left = NULL;
        struct TreeNode* flag = root;
        while(flag -> right){
            flag = flag -> right;
        }
        flag -> right = tmp;
    }
}
// === 4ms(96.3%) && 8.2MB(100%) === //
void flatten(struct TreeNode* root){
    if(root == NULL){
        return;
    }
    flatten(root -> right);
    flatten(root -> left);
    struct TreeNode* tmp = root -> right;
    root -> right = root -> left;
    root -> left = NULL;
    struct TreeNode* flag = root;
    while(flag -> right){
        flag = flag -> right;
    }
    flag -> right = tmp;
}