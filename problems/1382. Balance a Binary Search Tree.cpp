/*
=== 1382. Balance a Binary Search Tree === 

Given a binary search tree, return a balanced binary search tree with the same node values.
A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.
If there is more than one answer, return any of them.

Example 1:
    Input: root = [1,null,2,null,3,null,4,null,null]
    Output: [2,1,3,null,null,null,4]
    Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 
Constraints:
    1. The number of nodes in the tree is between 1 and 10^4.
    2. The tree nodes will have distinct values between 1 and 10^5.
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void traverse(struct TreeNode* root, int* val, int* size){
    if(root == NULL){
        return;
    }
    traverse(root->left, val, size);
    val[*size] = root -> val;
    ++ *size;
    traverse(root->right, val, size);
    return;
}

struct TreeNode* buildBST(int* val, int size){
    if(size <= 0){
        return NULL;
    }
    int mid = size / 2;
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root -> val = val[mid];
    root -> left = buildBST(val, mid);
    root -> right = buildBST(&(val[mid+1]), size-mid-1);
    return root;
}
// === 80ms && 43.1MB === //
struct TreeNode* balanceBST(struct TreeNode* root){
    int vallist[10000]; 
    int size=0;
    traverse(root, vallist, &size);
    return buildBST(vallist, size);
}

