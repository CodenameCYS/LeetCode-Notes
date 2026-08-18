/*
=== 110. Balanced Binary Tree ===

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:
    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
 Return false.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool myisBalanced(struct TreeNode* root, int* height){
    if(root == NULL){
        *height = 0;
        return true;
    }
    else if(root -> left == NULL && root -> right == NULL){
        *height=1;
        return true;
    }
    else if(root -> left == NULL){
        int rheight = 0;
        bool rstate = myisBalanced(root -> right, &rheight);
        *height = rheight + 1;
        return rstate && (rheight <= 1);
    }
    else if(root -> right == NULL){
        int lheight = 0;
        bool lstate = myisBalanced(root -> left, &lheight);
        *height = lheight + 1;
        return lstate && (lheight <= 1);
    }
    else{
        int rheight = 0, lheight = 0;
        bool lstate = myisBalanced(root -> left, &lheight);
        bool rstate = myisBalanced(root -> right, &rheight);
        *height = lheight > rheight? lheight+1 : rheight+1;
        return lstate && rstate && (abs(lheight-rheight) <= 1);
    }
}
bool isBalanced(struct TreeNode* root) {
    int height = 0;
    return myisBalanced(root, &height);
}