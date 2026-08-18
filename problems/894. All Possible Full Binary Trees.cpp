/*
=== 894. All Possible Full Binary Trees ===

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.
Each node of each tree in the answer must have node.val = 0.
You may return the final list of trees in any order.

Example 1:
Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Note:
1. 1 <= N <= 20
*/
# include <stdio.h>
# include <stdlib.h>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct TreeNode** allPossibleFBT(int N, int* returnSize) {
    if(N % 2 == 0){
        *returnSize = 0;
        return NULL;
    }
    else if(N == 1){
        *returnSize = 1;
        struct TreeNode** ans = (struct TreeNode**)malloc(sizeof(struct TreeNode*));
        ans[0] = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        ans[0] -> val = 0;
        ans[0] -> left = NULL;
        ans[0] -> right = NULL;
        return ans;
    }
    else{
        *returnSize = 0;
        struct TreeNode** ans = (struct TreeNode**)malloc(sizeof(struct TreeNode*));
        for(int i=1; i<N; i+=2){
            int leftChildNum, rightChildNum;
            struct TreeNode** leftChildList = allPossibleFBT(i, &leftChildNum);
            struct TreeNode** rightChildList = allPossibleFBT(N-i-1, &rightChildNum);
            int newsize = *returnSize + leftChildNum * rightChildNum;
            ans = (struct TreeNode**)realloc(ans, newsize*sizeof(struct TreeNode*));
            for(int ii=0; ii<leftChildNum; ++ii){
                for(int jj=0; jj<rightChildNum; ++jj){
                    int loc = *returnSize + ii*rightChildNum + jj;
                    ans[loc] = (struct TreeNode*)malloc(sizeof(struct TreeNode));
                    ans[loc] -> val = 0;
                    ans[loc] -> left = leftChildList[ii];
                    ans[loc] -> right = rightChildList[jj];
                }
            }
            *returnSize += leftChildNum * rightChildNum;
        }
        return ans;
    }
}