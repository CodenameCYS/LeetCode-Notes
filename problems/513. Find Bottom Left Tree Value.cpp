/*
=== 513. Find Bottom Left Tree Value ===

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:
    2
   / \
  1   3
Output:
1
Example 2:
Input:
        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7
Output:
7

Note: You may assume the tree (i.e., the given root node) is not NULL.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// === 8ms(76%) && 10.2MB(100%) === // 
void traverse(struct TreeNode* root, int* bottomleft, int* tmplevel, int level){
    if(root == NULL){
        return;
    }
    traverse(root -> left, bottomleft, tmplevel, level+1);
    traverse(root -> right, bottomleft, tmplevel, level+1);
    if(level > *tmplevel){
        *bottomleft = root->val;
        *tmplevel = level;
    }
}
int findBottomLeftValue(struct TreeNode* root){
    int bottomleft=0, tmplevel=-1;
    traverse(root, &bottomleft, &tmplevel, 0);
    return bottomleft;
}

