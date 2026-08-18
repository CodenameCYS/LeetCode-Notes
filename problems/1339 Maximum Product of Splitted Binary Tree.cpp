/*
=== 5330. Maximum Product of Splitted Binary Tree ===

Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
    Input: root = [1,2,3,4,5,6]
    Output: 110
    Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:
    Input: root = [1,null,2,3,4,null,null,5,6]
    Output: 90
    Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
Example 3:
    Input: root = [2,3,9,10,7,8,6,5,4,11,1]
    Output: 1025
Example 4:
    Input: root = [1,1]
    Output: 1
 
Constraints:
    1. Each tree has at most 50000 nodes and at least 2 nodes.
    2. Each node's value is between [1, 10000].
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int cal_sum(struct TreeNode* root){
    if(root == NULL){
        return 0;
    }
    return root -> val + cal_sum(root -> left) + cal_sum(root -> right);
}

long my_sum_v2(struct TreeNode* root, int sum, long* max){
    if(root == NULL){
        return 0;
    }
    long tmp;
    long s1 = my_sum_v2(root -> left, sum, max);
    tmp = s1 * (sum-s1);
    *max = tmp > *max ? tmp : *max;
    long s2 = my_sum_v2(root -> right, sum, max);
    tmp = s2 * (sum-s2);
    *max = tmp > *max ? tmp : *max;
    return root -> val + s1 + s2;
}
// === 92ms && 44.7MB === //
int maxProduct(struct TreeNode* root){
    int sum = cal_sum(root);
    long max = 0;
    my_sum_v2(root, sum, &max);
    return max % 1000000007;
}

