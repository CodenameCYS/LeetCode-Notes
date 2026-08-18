/*
// === 108. Convert Sorted Array to Binary Search Tree === //

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
*/
# include <stdio.h>
# include <stdlib.h>
// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void myBuildBST(int*nums, int start, int end, struct TreeNode** root){
    if(start > end){
        return;
    }
    else{
        root[0] = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        // 存在优先级的问题，root[0] -> val == (*root) -> val != *root -> val
        // ->的优先级比*高一级
        root[0] -> val = nums[(start + end)/2];
        root[0] -> left = NULL;
        root[0] -> right = NULL;
        // printf("%d\t", root[0] -> val);
        myBuildBST(nums, start, (start + end)/2 - 1, & (root[0] -> left));
        myBuildBST(nums, (start + end)/2 + 1, end, & (root[0] -> right));
        return;
    }
}
// === beat 100% === //

struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    struct TreeNode* BST = NULL;
    myBuildBST(nums, 0, numsSize-1, &BST);
    return BST;
}