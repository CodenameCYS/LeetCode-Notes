/*
=== 102. Binary Tree Level Order Traversal === 

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
*/
# include <stdlib.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void PushInAns(struct TreeNode* root, int*** ans, int** columnSizes, int* returnSize, int level);
void LevelOrderSearch(struct TreeNode* root, int*** ans, int** columnSizes, int* returnSize, int level);
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** levelOrder(struct TreeNode* root, int** columnSizes, int* returnSize) {
    if(root == NULL){
        *returnSize = 0;
        *columnSizes = NULL;
        return NULL;
    }
    else{
        int** ans = NULL;
        *returnSize = 0;
        LevelOrderSearch(root, &ans, columnSizes, returnSize, 0);
        return ans;
    }
}

void PushInAns(struct TreeNode* root, int*** ans, int** columnSizes, int* returnSize, int level){
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
            *ans =(int**)realloc(*ans, *returnSize*sizeof(int*));
            // printf("finished step 02\n");
            *(*ans + level) = (int*)malloc(sizeof(int));
            // printf("finished step 03\n");
            *(*(*ans + level) + *(*columnSizes + level) - 1) = root -> val;
        }
        else{
            *(*columnSizes + level) += 1;
            *(*ans + level) = (int*)realloc(*(*ans + level), *(*columnSizes + level) * sizeof(int));
            *(*(*ans + level) + *(*columnSizes + level) - 1) = root -> val;
        }
    }
    return;
}

void LevelOrderSearch(struct TreeNode* root, int*** ans, int** columnSizes, int* returnSize, int level){
    PushInAns(root, ans, columnSizes, returnSize, level);
    if(root -> left){
        LevelOrderSearch(root->left, ans, columnSizes, returnSize, level+1);
    }
    if(root -> right){
        LevelOrderSearch(root->right, ans, columnSizes, returnSize, level+1);
    }
    return;
}