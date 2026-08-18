/*
=== 993. Cousins in Binary Tree ===

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false
Example 2:
    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true
Example 3:
    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false
 
Note:
    - The number of nodes in the tree will be between 2 and 100.
    - Each node has a unique integer value from 1 to 100.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// === 8ms & 8MB === //
bool findNodeInfo(struct TreeNode* root, int x, int level, int father, int* l, int* f){
    if(root == NULL){
        return false;
    }
    if(root -> val == x){
        *l = level;
        *f = father;
        return true;
    }
    return findNodeInfo(root->left, x, level+1, root->val, l, f) || findNodeInfo(root->right, x, level+1, root->val, l, f);
}
bool isCousins(struct TreeNode* root, int x, int y) {
    int x_level, x_father, y_level, y_father;
    findNodeInfo(root, x, 0, 0, &x_level, &x_father);
    findNodeInfo(root, y, 0, 0, &y_level, &y_father);
    return x_level == y_level && x_father != y_father;
}