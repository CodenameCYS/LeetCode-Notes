/*
=== 1161. Maximum Level Sum of a Binary Tree ===

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
 
Example 1:
    Input: [1,7,0,7,-8,null,null]
    Output: 2
    - Explanation: 
    Level 1 sum = 1.
    Level 2 sum = 7 + 0 = 7.
    Level 3 sum = 7 + -8 = -1.
    So we return the level with the maximum sum which is level 2.
 
Note:
    1. The number of nodes in the given tree is between 1 and 10^4.
    2. -10^5 <= node.val <= 10^5
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void traverse(struct TreeNode* root, int* record, int level){
    if(root == NULL){
        return;
    }
    traverse(root -> left, record, level + 1);
    record[0] = record[0] > level ? record[0] : level;
    record[level] += root -> val;
    traverse(root -> right, record, level + 1);
    return;
}
// === 100ms && 48.1MB === //
int maxLevelSum(struct TreeNode* root){
    int record[10001];
    for(int i=0; i<10001; ++i){
        record[i] = 0;
    }
    traverse(root, record, 1);
    int ans = 1;
    for(int i=1; i<=record[0]; ++i){
        if(record[i] > record[ans]){
            ans = i;
        }
    }
    return ans;
}

