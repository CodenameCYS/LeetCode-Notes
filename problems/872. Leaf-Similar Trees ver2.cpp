/*
=== 872. Leaf-Similar Trees ===

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
    - Both of the given trees will have between 1 and 100 nodes.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void searchleaves(struct TreeNode* root, int* leafs, int* leafnum){
    if(root == NULL){
        return;
    }
    if(root -> left == NULL && root -> right == NULL){
        leafs[*leafnum] = root -> val;
        ++ *leafnum;
    }
    else{
        searchleaves(root -> left, leafs, leafnum);
        searchleaves(root -> right, leafs, leafnum);
    }
}
// === 4ms(94.78%) && 7.4MB === //
bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2){
    int leafs_1[1000], leafs_2[1000];
    int leafnum_1 = 0, leafnum_2 = 0;
    searchleaves(root1, leafs_1, &leafnum_1);
    searchleaves(root2, leafs_2, &leafnum_2);
    if(leafnum_1 != leafnum_2){
        return false;
    }
    for(int i=0; i<leafnum_1; ++i){
        if(leafs_1[i] != leafs_2[i]){
            return false;
        }
    }
    return true;
}

