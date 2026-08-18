/*
=== 404. Sum of Left Leaves ===

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// === 8ms(18.6%) && 7.8MB(100%) === //
int sumOfLeftLeaves(struct TreeNode* root){
    if(root == NULL){
        return 0;
    }
    else if(root -> left == NULL && root -> right == NULL){
        return 0;
    }
    else if(root -> left == NULL){
        return sumOfLeftLeaves(root -> right);
    }
    else{
        int ans = 0;
        if(root -> left -> left == NULL && root -> left -> right == NULL){
            ans = root -> left -> val;
        }
        else{
            ans = sumOfLeftLeaves(root -> left);
        }
        ans += sumOfLeftLeaves(root -> right);
        return ans;
    }
}

