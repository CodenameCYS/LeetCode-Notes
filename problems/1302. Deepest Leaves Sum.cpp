/*
=== 1302. Deepest Leaves Sum ===

Given a binary tree, return the sum of values of its deepest leaves.
 
Example 1:
    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15
 
Constraints:
    1. The number of nodes in the tree is between 1 and 10^4.
    2. The value of nodes is between 1 and 100.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void dfs(struct TreeNode* root, int depth, int* cache, int* size){
    if(root == NULL){
        return;
    }
    if(depth >= *size){
        ++ *size;
        cache[depth] = root -> val;
    }
    else{
        cache[depth] += root -> val;
    }
    dfs(root->left, depth+1, cache, size);
    dfs(root->right, depth+1, cache, size);
}
// === 28ms(77.27%) && 15.5MB(38.64) === //
int deepestLeavesSum(struct TreeNode* root){
    int cache[10000], depth=0;
    dfs(root, 0, cache, &depth);
    return cache[depth-1];
}