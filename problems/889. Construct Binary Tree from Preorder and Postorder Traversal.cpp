/*
=== 889. Construct Binary Tree from Preorder and Postorder Traversal ===

Return any binary tree that matches the given preorder and postorder traversals.
Values in the traversals pre and post are distinct positive integers. 

Example 1:
Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 
Note:
1. 1 <= pre.length == post.length <= 30
2. pre[] and post[] are both permutations of 1, 2, ..., pre.length.
3. It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
*/
# include <stdlib.h>
// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct TreeNode* constructFromPrePost(int* pre, int preSize, int* post, int postSize) {
    if(preSize <= 0){
        return NULL;
    }
    else if(preSize == 1){
        struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        root -> val = pre[0];
        root -> left = NULL;
        root -> right = NULL;
        return root;
    }
    else{
        struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        int count = 0;
        while(post[count] != pre[1]){
            ++ count;
        }
        root -> val = pre[0];
        root -> left = constructFromPrePost(&pre[1], count+1, post, count+1);
        root -> right = constructFromPrePost(&pre[count+2], preSize-count-2, &post[count+1], postSize-count-2);
        return root;
    }
}