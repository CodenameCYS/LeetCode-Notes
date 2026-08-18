/*
=== 199. Binary Tree Right Side View ===
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

*/
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
// === beat 100% === //
int* rightSideView(struct TreeNode* root, int* returnSize) {
    int* ans = NULL;
    *returnSize = 0;
    
    if(root == NULL){
        return NULL;
    }
    
    int maxlen = 128;
    ans = (int*)malloc(maxlen*sizeof(int));
    
    struct TreeNode** stack1;
    struct TreeNode** stack2;
    int maxstacklen1 = 1024, maxstacklen2 = 1024;
    stack1 = (struct TreeNode**)malloc(maxstacklen1 * sizeof(struct TreeNode*));
    stack2 = (struct TreeNode**)malloc(maxstacklen2 * sizeof(struct TreeNode*));
    int stack1len = 0,  stack2len = 0;
    stack1[0] = root;
    stack1len = 1;
    
    while(stack1len != 0 || stack2len != 0){
        if(stack1len != 0){
            ans[*returnSize] = stack1[0] -> val;
            ++ *returnSize;
            if(*returnSize == maxlen){
                ans = (int*)realloc(ans, (maxlen+128)*sizeof(int));
                maxlen += 128;
            }
            
            for(int i=0; i<stack1len; ++i){
                if(stack1[i] -> right != NULL){
                    stack2[stack2len] = stack1[i] -> right;
                    ++ stack2len;
                    if(stack2len == maxstacklen2){
                        stack2 = (struct TreeNode**)realloc(stack2, (maxstacklen2+1024)*sizeof(struct TreeNode*));
                        maxstacklen2 += 1024;
                    }
                }
                if(stack1[i] -> left != NULL){
                    stack2[stack2len] = stack1[i] -> left;
                    ++ stack2len;
                    if(stack2len == maxstacklen2){
                        stack2 = (struct TreeNode**)realloc(stack2, (maxstacklen2+1024)*sizeof(struct TreeNode*));
                        maxstacklen2 += 1024;
                    }
                }
            }
            stack1len = 0;
        }
        else{
            ans[*returnSize] = stack2[0] -> val;
            ++ *returnSize;
            if(*returnSize == maxlen){
                ans = (int*)realloc(ans, (maxlen+128)*sizeof(int));
                maxlen += 128;
            }
            
            for(int i=0; i<stack2len; ++i){
                if(stack2[i] -> right != NULL){
                    stack1[stack1len] = stack2[i] -> right;
                    ++ stack1len;
                    if(stack1len == maxstacklen1){
                        stack1 = (struct TreeNode**)realloc(stack1, (maxstacklen1+1024)*sizeof(struct TreeNode*));
                        maxstacklen1 += 1024;
                    }
                }
                if(stack2[i] -> left != NULL){
                    stack1[stack1len] = stack2[i] -> left;
                    ++ stack1len;
                    if(stack1len == maxstacklen1){
                        stack1 = (struct TreeNode**)realloc(stack1, (maxstacklen1+1024)*sizeof(struct TreeNode*));
                        maxstacklen1 += 1024;
                    }
                }
            }
            stack2len = 0;
        }
    }
    
    ans = (int*)realloc(ans, *returnSize * sizeof(int));
    return ans;
}