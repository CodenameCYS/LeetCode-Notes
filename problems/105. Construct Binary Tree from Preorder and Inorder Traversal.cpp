/*
=== 105. Construct Binary Tree from Preorder and Inorder Traversal ===

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
// === beat 43.28% === //
struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize) {
    struct TreeNode* ans = NULL;
    
    if(preorderSize <= 0){
        return ans;
    }
    ans = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    ans -> val = preorder[0];
    int count = 0;
    while(inorder[count] != preorder[0]){
        ++ count;
    }
    ans -> left = buildTree(&preorder[1], count, inorder, count);
    ans -> right = buildTree(&preorder[count + 1], preorderSize-count-1, &inorder[count+1], inorderSize-count-1);
    
    return ans;
}