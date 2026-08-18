/*
=== 1448. Count Good Nodes in Binary Tree ===

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: Nodes in blue are good.
    Root Node (3) is always a good node.
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    Node 5 -> (3,4,5) is the maximum value in the path
    Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:
    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:
    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.
 
Constraints:
    1. The number of nodes in the binary tree is in the range [1, 10^5].
    2. Each node's value is between [-10^4, 10^4].
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
void my_solution(struct TreeNode* root, int max, int* answer){
    if(root == NULL){
        return;
    }
    if(root -> val >= max){
        ++ *answer;
        my_solution(root -> left, root -> val, answer);
        my_solution(root -> right, root -> val, answer);
    }
    else{
        my_solution(root -> left, max, answer);
        my_solution(root -> right, max, answer);
    }
}
// === 84ms && 37.6MB === //
int goodNodes(struct TreeNode* root){
    int ans = 0;
    my_solution(root, root -> val, &ans);
    return ans;
}