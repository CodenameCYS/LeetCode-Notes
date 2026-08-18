/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool isSymmetricTrees(struct TreeNode* root1, struct TreeNode* root2){
    if(root1 == NULL && root2 == NULL){
        return true;
    }
    else if(root1 == NULL || root2 == NULL){
        return false;
    }
    else{
        return root1 -> val == root2 -> val && isSymmetricTrees(root1->left, root2->right) && isSymmetricTrees(root1->right, root2->left);
    }
}

bool isSymmetric(struct TreeNode* root) {
    if(root == NULL){
        return true;
    }
    else{
        return isSymmetricTrees(root->left, root->right);
    }
}
