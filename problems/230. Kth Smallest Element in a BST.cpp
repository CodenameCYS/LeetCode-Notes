/*
=== 230. Kth Smallest Element in a BST ===

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
    - You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void traverse(struct TreeNode* root, int* arr, int* size, int k){
    if(root == NULL){
        return;
    }
    traverse(root -> left, arr, size, k);
    if(*size >= k){
        return;
    }
    arr[*size] = root -> val;
    ++ *size;
    // printf("%d:%d\t", *size, root->val);
    traverse(root -> right, arr, size, k);
    return;
}
// === 16ms(25%) && 11.6MB(33.33%) === //
int kthSmallest(struct TreeNode* root, int k){
    int arr[k], size=0;
    traverse(root, arr, &size, k);
    return arr[k-1];
}

// =================================================================================== //
void traverse(struct TreeNode* root, int* num, int *k){
    if(root == NULL){
        return;
    }
    traverse(root -> left, num, k);
    if(*k == 1){
        *num = root->val;
        -- *k;
        return;
    }
    -- *k;
    traverse(root -> right, num, k);
    return;
}
// === 12ms(75.96%) && 11.5MB(33.33%) === //
int kthSmallest(struct TreeNode* root, int k){
    int num;
    traverse(root, &num, &k);
    return num;
}

