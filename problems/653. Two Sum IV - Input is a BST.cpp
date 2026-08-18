/*
=== 653. Two Sum IV - Input is a BST ===

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
Output: True

Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7
Target = 28
Output: False
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void traverse(struct TreeNode* root, int* nums, int* size){
    if(root == NULL){
        return;
    }
    traverse(root->left, nums, size);
    nums[*size] = root -> val;
    ++ *size;
    traverse(root->right, nums, size);
}
// === 24ms(80%) && 13.9MB(100%) === //
bool findTarget(struct TreeNode* root, int k){
    int nums[50000], size=0;
    traverse(root, nums, &size);
    for(int i=0, j=size-1;i<j;){
        if(nums[i] + nums[j] == k){
            return true;
        }
        else if(nums[i] + nums[j] < k){
            ++ i;
        }
        else{
            -- j;
        }
    }
    return false;
}

