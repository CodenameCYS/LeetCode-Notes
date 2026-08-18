/*
=== 1028. Recover a Tree From Preorder Traversal ===

We run a preorder depth first search on the root of a binary tree.
At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)
If a node has only one child, that child is guaranteed to be the left child.
Given the output S of this traversal, recover the tree and return its root.

Example 1:
    Input: "1-2--3--4-5--6--7"
    Output: [1,2,5,3,4,6,7]
Example 2:
    Input: "1-2--3---4-5--6---7"
    Output: [1,2,5,3,null,6,null,4,null,7]
Example 3:
    Input: "1-401--349---90--88"
    Output: [1,401,null,349,88,90]
 
Note:
    1. The number of nodes in the original tree is between 1 and 1000. 
    2. Each node will have a value between 1 and 10^9.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// === 12ms & 9.9MB === //
struct TreeNode* recoverFromPreorder(char* S) {
    struct TreeNode* parents[1000];
    int level = 0;
    int val = 0;
    bool need_recount = true;
    for(int i=0; S[i]!='\0'; ++i){
        if(S[i] >= '0' && S[i] <= '9'){
            val = 10*val + S[i]-'0';
            need_recount = true;
        }
        else if(S[i] == '-'){
            if(need_recount){
                struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
                node -> val = val;
                node -> left = NULL;
                node -> right = NULL;
                parents[level] = node;
                val = 0;
                
                if(level != 0 && parents[level-1] -> left == NULL){
                    parents[level-1] -> left = node;
                }
                else if(level != 0 && parents[level-1] -> right == NULL){
                    parents[level-1] -> right = node;
                }
                
                level = 1;
                need_recount = false;
            }
            else{
                ++ level;
            }
        }
    }
    // 给最后一个节点赋值
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node -> val = val;
    node -> left = NULL;
    node -> right = NULL;
    parents[level] = node;

    if(level != 0 && parents[level-1] -> left == NULL){
        parents[level-1] -> left = node;
    }
    else if(level != 0 && parents[level-1] -> right == NULL){
        parents[level-1] -> right = node;
    }

    return parents[0];
}