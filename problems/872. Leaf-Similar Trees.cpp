/*
=== 872. Leaf-Similar Trees ===

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
Both of the given trees will have between 1 and 100 nodes.
*/
# include <stdio.h>
# include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2);
void pushleafseq(struct TreeNode* root, int* leafseq, int* leafnum);
bool popleafseq(struct TreeNode* root, int* leafseq, int* leafnum);

int main(){

    system("pause");
    return 1;
}

void pushleafseq(struct TreeNode* root, int* leafseq, int* leafnum){
    if(root == NULL){
        return;
    }
    else if(root -> left == NULL && root -> right == NULL){
        leafseq[*leafnum] = root -> val;
        ++ *leafnum;
        return;
    }
    else{
        pushleafseq(root -> left, leafseq, leafnum);
        pushleafseq(root -> right, leafseq, leafnum);
    }
}

bool popleafseq(struct TreeNode* root, int* leafseq, int* leafnum){
    if(root == NULL){
        return true;
    }
    else if(root -> left == NULL && root -> right == NULL){
        int leaf = root -> val;
        if(leaf == leafseq[*leafnum - 1]){
            -- *leafnum;
            return true;
        }
        else{
            return false;
        }
    }
    else{
        return popleafseq(root -> right, leafseq, leafnum) && popleafseq(root -> left, leafseq, leafnum);
    }
}

bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2){
    int leafseq[100];
    int leafnum = 0;
    bool ans;

    pushleafseq(root1, leafseq, &leafnum);
    ans = popleafseq(root2, leafseq, &leafnum);

    return ans && leafnum == 0;
}