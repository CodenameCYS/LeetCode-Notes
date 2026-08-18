/*
=== 515. Find Largest Value in Each Tree Row ===

You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void traverse(struct TreeNode* root, int* returnSize, int* ans, int level){
    if(root == NULL){
        return;
    }
    if(level == *returnSize){
        ans[*returnSize] = root -> val;
        ++ *returnSize;
    }
    else{
        ans[level] = ans[level] > root->val ? ans[level] : root->val;
    }
    traverse(root->left, returnSize, ans, level+1);
    traverse(root->right, returnSize, ans, level+1);
}
// === 12ms(46.15%) && 10.8MB(100%) === //
int* largestValues(struct TreeNode* root, int* returnSize){
    int* ans = (int*)malloc(1000*sizeof(int));
    *returnSize = 0;
    traverse(root, returnSize, ans, 0);
    return ans;
}

