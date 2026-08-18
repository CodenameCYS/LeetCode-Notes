/* === 107. Binary Tree Level Order Traversal II ===
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
*/
# include <stdlib.h>
// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void TDSearch(struct TreeNode* root, int** columnSizes, int* returnSize, int*** ans, int level){
    if(root == NULL){
        return;
    }
    if(*returnSize == level){
        ++ *returnSize;
        if(*returnSize == 1){
            *ans = (int**)malloc(sizeof(int*));
            *columnSizes = (int*)malloc(sizeof(int));
        }
        else{
            *ans = (int**)realloc(*ans, *returnSize * sizeof(int*));
            *columnSizes = (int*)realloc(*columnSizes, *returnSize * sizeof(int));
        }
        *(*ans + level) = (int*)malloc(sizeof(int));
        **(*ans + level) = root -> val;
        *(*columnSizes + level) = 1;
    }
    else{
        ++ *(*columnSizes + level);
        *(*ans + level) = (int*)realloc(*(*ans + level), *(*columnSizes + level) * sizeof(int));
        *(*(*ans + level) + *(*columnSizes + level) -1) = root -> val;
    }
    TDSearch(root -> left, columnSizes, returnSize, ans, level + 1);
    TDSearch(root -> right, columnSizes, returnSize, ans, level + 1);
}
// === beat 100% ===
int** levelOrderBottom(struct TreeNode* root, int** columnSizes, int* returnSize) {
    int** ans = NULL;
    
    *returnSize = 0;
    TDSearch(root, columnSizes, returnSize, &ans, 0);
    
    for(int i=0; i<*returnSize/2 ; ++i){
        int* tempans = ans[i];
        ans[i] = ans[*returnSize-1-i];
        ans[*returnSize-1-i] = tempans;
        int tempsize = columnSizes[0][i];
        columnSizes[0][i] = columnSizes[0][*returnSize-1-i];
        columnSizes[0][*returnSize-1-i] = tempsize;
    }
    
    return ans;
}