/*
=== 103. Binary Tree Zigzag Level Order Traversal ===

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
*/
# include <stdlib.h>
// === ver 1.0 beat 100% === //

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
 // Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool TraverseLayer(struct TreeNode** QueueIn, int QueueInSize, struct TreeNode*** QueueOut, int* QueueOutSize, 
                  int*** ans, int** columnSizes, int* returnSize){
    *QueueOutSize = 0;
    free(*QueueOut);
    *QueueOut = (struct TreeNode **)malloc(2 * QueueInSize * sizeof(struct TreeNode *));
    ++ *returnSize;
    if(*returnSize == 1){
        *columnSizes = (int*)malloc(*returnSize * sizeof(int));
        *(*columnSizes + *returnSize - 1) = QueueInSize;
        *ans = (int**)malloc(*returnSize * sizeof(int*));
        *(*ans + *returnSize -1) = (int *)malloc(QueueInSize * sizeof(int));
    }
    else{
        *columnSizes = (int*)realloc(*columnSizes, *returnSize * sizeof(int));
        *(*columnSizes + *returnSize - 1) = QueueInSize;
        *ans = (int**)realloc(*ans, *returnSize * sizeof(int*));
        *(*ans + *returnSize -1) = (int *)malloc(QueueInSize * sizeof(int));
    }
    for(int i=0; i<QueueInSize; ++i){
        ans[0][*returnSize-1][i] = QueueIn[i] -> val;
        if(*returnSize % 2 == 0){
            if(QueueIn[QueueInSize-1-i] -> left){
                ++ *QueueOutSize;
                QueueOut[0][*QueueOutSize - 1] = QueueIn[QueueInSize-1-i] -> left;
            }
            if(QueueIn[QueueInSize-1-i] -> right){
                ++ *QueueOutSize;
                QueueOut[0][*QueueOutSize - 1] = QueueIn[QueueInSize-1-i] -> right;
            }
        }
        else{
            if(QueueIn[QueueInSize-1-i] -> right){
                ++ *QueueOutSize;
                QueueOut[0][*QueueOutSize - 1] = QueueIn[QueueInSize-1-i] -> right;
            }
            if(QueueIn[QueueInSize-1-i] -> left){
                ++ *QueueOutSize;
                QueueOut[0][*QueueOutSize - 1] = QueueIn[QueueInSize-1-i] -> left;
            }
        }
    }
    if(*QueueOutSize == 0){
        return false;
    }
    else{
        return true;
    }
}

int** zigzagLevelOrder(struct TreeNode* root, int** columnSizes, int* returnSize) {
    if(root == NULL){
        return NULL;
    }
    int** ans = NULL;
    struct TreeNode** LtoRQueue = NULL;
    struct TreeNode** RtoLQueue = NULL;
    int LtoRSize = 1;
    int RtoLSize = 0;
    LtoRQueue = (struct TreeNode **)malloc(sizeof(struct TreeNode *));
    LtoRQueue[0] = root;
    
    *returnSize = 0;
    bool state = true;
    while(state){
        if(*returnSize % 2 == 0){
            state = TraverseLayer(LtoRQueue, LtoRSize, &RtoLQueue, &RtoLSize, &ans, columnSizes, returnSize);
        }
        else{
            state = TraverseLayer(RtoLQueue, RtoLSize, &LtoRQueue, &LtoRSize, &ans, columnSizes, returnSize);
        }
    }
    free(LtoRQueue);
    free(RtoLQueue);
    return ans;
}