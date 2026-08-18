/*
=== 222. Count Complete Tree Nodes ===

Given a complete binary tree, count the number of nodes.

Note:
    Definition of a complete binary tree from Wikipedia:
    In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:
    Input: 
        1
       / \
      2   3
     / \  /
    4  5 6
    Output: 6
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// === 296ms(7.32%) === //
int countHeight(struct TreeNode* root, char state){
    if(root == NULL){
        return 0;
    }
    if(state == 'l'){
        return 1+countHeight(root->left, state);
    }
    else{
        return 1+countHeight(root->right, state);
    }
}
int countNodes(struct TreeNode* root) {
    if(root == NULL){
        return 0;
    }
    int lheight = countHeight(root, 'l');
    int rheight = countHeight(root, 'r');
    int ans = pow(2, rheight)-1;
    if(lheight == rheight){
        return ans;
    }
    return 1 + countNodes(root->left) + countNodes(root->right);
}
// === 202ms(7.32%) === //
int countNodes(struct TreeNode* root) {
    if(root == NULL){
        return 0;
    }
    int lheight = 1;
    int rheight = 1;
    for(struct TreeNode* lt = root->left; lt!=NULL ;lt = lt->left){
        ++ lheight;
    }
    for(struct TreeNode* rt = root->right; rt!=NULL;rt = rt->right){
        ++ rheight;
    }
    int ans = pow(2, rheight)-1;
    if(lheight == rheight){
        return ans;
    }
    return 1 + countNodes(root->left) + countNodes(root->right);
}
// === 12ms(100%) === //
int countNodes(struct TreeNode* root) {
    if (root == NULL || root->val == -1)  return 0;
    root->val = -1;
    return 1 + countNodes(root->left) + countNodes(root->right);
}