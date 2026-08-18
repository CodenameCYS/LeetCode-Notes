/*
=== 572. Subtree of Another Tree ===

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
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

bool is_equal(struct TreeNode* s, struct TreeNode* t){
    if(t == NULL && s == NULL){
        return true;
    }
    else if(s == NULL || t == NULL){
        return false;
    }
    // printf("%d, %d\n", s->val, t->val);
    return s->val == t->val && is_equal(s->left, t->left) && is_equal(s->right, t->right);
}
// === 20ms(70.3%) && 12.6MB(100%) === //
bool isSubtree(struct TreeNode* s, struct TreeNode* t){
    if(is_equal(s,t)){
        return true;
    }
    else if(s == NULL || t == NULL){
        return false;
    }
    else{
        return isSubtree(s->left, t) || isSubtree(s->right, t);
    }
}

