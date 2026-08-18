/*
=== 543. Diameter of Binary Tree ===

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int traverse(struct TreeNode* root, int* diameter){
    if(root == NULL){
        return -1;
    }
    int ldepth = traverse(root -> left, diameter);
    int rdepth = traverse(root -> right, diameter);
    int tmp_diameter = ldepth + rdepth + 2;
    *diameter = *diameter > tmp_diameter ? *diameter : tmp_diameter;
    return ldepth > rdepth ? ldepth + 1 : rdepth + 1;
}
// === 4ms(95.70%) && 9.3MB(100%) === //
int diameterOfBinaryTree(struct TreeNode* root){
    int diameter = 0;
    traverse(root, &diameter);
    return diameter;
}

