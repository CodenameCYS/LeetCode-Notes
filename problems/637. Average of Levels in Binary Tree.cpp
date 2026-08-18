/*
=== 637. Average of Levels in Binary Tree ===

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
*/
# include <stdio.h>
# include <stdlib.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
void PushInAns(struct TreeNode* root, double** ans, int** columnSizes, int* returnSize, int level){
    if(root == NULL){
        return;
    }
    else{
        // printf("%d\t", root -> val);
        if(level == *returnSize){
            *returnSize += 1;
            *columnSizes = (int*)realloc(*columnSizes, *returnSize * sizeof(int));
            *(*columnSizes + level) = 1;
            // printf("finished step 01\n");
            *ans = (double*)realloc(*ans, *returnSize*sizeof(double));
            // printf("finished step 02\n");
            *(*ans + level) = root -> val;
        }
        else{
            *(*columnSizes + level) += 1;
            *(*ans + level) += root -> val;
        }
    }
    return;
}

void LevelOrderSearch(struct TreeNode* root, double** ans, int** columnSizes, int* returnSize, int level){
    PushInAns(root, ans, columnSizes, returnSize, level);
    if(root -> left){
        LevelOrderSearch(root->left, ans, columnSizes, returnSize, level+1);
    }
    if(root -> right){
        LevelOrderSearch(root->right, ans, columnSizes, returnSize, level+1);
    }
    return;
}

double* averageOfLevels(struct TreeNode* root, int* returnSize) {
    if(root == NULL){
        *returnSize = 0;
        return NULL;
    }
    else{
        double* ans = NULL;
        int* columnSizes = NULL;
        *returnSize = 0;
        LevelOrderSearch(root, &ans, &columnSizes, returnSize, 0);
        for(int i=0; i<*returnSize; ++i){
            ans[i] /= columnSizes[i];
        }
        
        return ans;
    }
    return NULL;
}