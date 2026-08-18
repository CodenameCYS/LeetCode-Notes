/*
=== 5296. All Elements in Two Binary Search Trees ===

Given two binary search trees root1 and root2.
Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
    Input: root1 = [2,1,4], root2 = [1,0,3]
    Output: [0,1,1,2,3,4]
Example 2:
    Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
    Output: [-10,0,0,1,2,5,7,10]
Example 3:
    Input: root1 = [], root2 = [5,1,7,0,2]
    Output: [0,1,2,5,7]
Example 4:
    Input: root1 = [0,-10,10], root2 = []
    Output: [-10,0,10]
Example 5:
    Input: root1 = [1,null,8], root2 = [8,1]
    Output: [1,1,8,8]
 
Constraints:
    1. Each tree has at most 5000 nodes.
    2. Each node's value is between [-10^5, 10^5].
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void traverse(struct TreeNode* root, int* l1, int* l1_size){
    if(root == NULL){
        return;
    }
    traverse(root -> left, l1, l1_size);
    l1[*l1_size] = root -> val;
    ++ *l1_size;
    traverse(root -> right, l1, l1_size);
}

int* merge(int* l1, int* l2, int l1_size, int l2_size, int* returnSize){
    *returnSize = l1_size + l2_size;
    int* ans = (int*) malloc(*returnSize * sizeof(int));
    int n1=0, n2=0;
    int flag = 0;
    while(n1<l1_size && n2<l2_size){
        if(l1[n1] < l2[n2]){
            ans[flag] = l1[n1];
            ++ n1;
        }
        else{
            ans[flag] = l2[n2];
            ++ n2;
        }
        ++ flag;
    }
    while(n1<l1_size){
        ans[flag] = l1[n1];
        ++ n1;
        ++ flag;
    }
    while(n2 < l2_size){
        ans[flag] = l2[n2];
        ++ n2;
        ++ flag;
    }
    return ans;
}
// === 192ms && 57.5MB === //
int* getAllElements(struct TreeNode* root1, struct TreeNode* root2, int* returnSize){
    int l1_size=0, l2_size=0;
    int l1[5000], l2[5000];
    traverse(root1, l1, &l1_size);
    traverse(root2, l2, &l2_size);
    int* ans = merge(l1, l2, l1_size, l2_size, returnSize);
    return ans;
}

