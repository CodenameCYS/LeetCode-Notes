/*
=== 1008. Construct Binary Search Tree from Preorder Traversal ===

Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
    Input: [8,5,1,7,10,12]
    Output: [8,5,10,1,7,null,12]

Note: 
    1. 1 <= preorder.length <= 100
    2. The values of preorder are distinct.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// === 4ms & 9.4MB === //
struct TreeNode* bstFromPreorder(int* preorder, int preorderSize) {
    if(preorderSize <= 0){
        return NULL;
    }
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root -> val = preorder[0];
    int leftsize = 0;
    for(int i=1; i<preorderSize; ++i){
        if(preorder[i] > root -> val){
            break;
        }
        else{
            ++leftsize;
        }
    }
    int rightsize = preorderSize-1-leftsize;
    root -> left = bstFromPreorder(&preorder[1], leftsize);
    root -> right = bstFromPreorder(&preorder[1+leftsize], rightsize);
    return root;
}