/*
=== 559. Maximum Depth of N-ary Tree ===

Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note:
1. The depth of the tree is at most 1000.
2. The total number of nodes is at most 5000.
*/
// Definition for a Node.
# include <stdlib.h>
# include <vector>

using namespace std;

class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
// === beat 93.74% === //
class Solution {
public:
    int maxDepth(Node* root) {
        if(root == NULL){
            return 0;
        }
        else if(root -> children.size() == 0){
            return 1;
        }
        int max = 0;
        for(int i=0; i < root -> children.size(); ++i){
            int depth = maxDepth(root->children[i]);
            max = max > depth ? max : depth;
        }
        return max + 1;
    }
};