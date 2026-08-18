/*
=== 106. Construct Binary Tree from Inorder and Postorder Traversal ===

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
*/
// Definition for a binary tree node.
# include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
}
// === beat 100% === //
struct TreeNode* buildTree(int* inorder, int inorderSize, int* postorder, int postorderSize) {
    struct TreeNode* ans = NULL;
    
    if(postorderSize <= 0){
        return ans;
    }
    ans = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    ans -> val = postorder[postorderSize-1];
    int count = 0;
    while(inorder[inorderSize-1-count] != postorder[postorderSize-1]){
        ++ count;
    }
    ans -> left = buildTree(inorder, postorderSize-count-1, postorder, postorderSize-count-1);
    ans -> right = buildTree(inorder+postorderSize-count, count, postorder+postorderSize-count-1, count);
    
    return ans;
}