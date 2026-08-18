/*
=== 226. Invert Binary Tree ===

Invert a binary tree.

Example:
    Input:
         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    Output:
         4
       /   \
      7     2
     / \   / \
    9   6 3   1
Trivia:
    This problem was inspired by this original tweet by Max Howell:
    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// === 0ms(100%) === //
struct TreeNode* invertTree(struct TreeNode* root) {
    if(root == NULL){
        return NULL;
    }
    
    struct TreeNode* temp = root -> left;
    root -> left = root -> right;
    root -> right = temp;
    root -> left = invertTree(root -> left);
    root -> right = invertTree(root -> right);
    return root;
}