/*
=== 530. Minimum Absolute Difference in BST ===

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:
Input:

   1
    \
     3
    /
   2

Output:
1
Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 
Note: There are at least two nodes in this BST.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void traverse(struct TreeNode* root, int* last_val, int* min_diff){
    if(root == NULL){
        return;
    }
    traverse(root->left, last_val, min_diff);
    if(*last_val >= 0){
        *min_diff = *min_diff < root->val - *last_val ? *min_diff : root->val - *last_val;
    }
    *last_val = root -> val;
    traverse(root->right, last_val, min_diff);
}
// === 12ms(73.91%) && 11.4MB(100%) === //
int getMinimumDifference(struct TreeNode* root){
    int last_val = -1, min_diff = INT_MAX;
    traverse(root, &last_val, &min_diff);
    return min_diff;
}

