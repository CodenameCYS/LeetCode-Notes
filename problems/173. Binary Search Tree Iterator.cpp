/*
=== 173. Binary Search Tree Iterator ===

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Example:
    BSTIterator iterator = new BSTIterator(root);
    iterator.next();    // return 3
    iterator.next();    // return 7
    iterator.hasNext(); // return true
    iterator.next();    // return 9
    iterator.hasNext(); // return true
    iterator.next();    // return 15
    iterator.hasNext(); // return true
    iterator.next();    // return 20
    iterator.hasNext(); // return false
 
Note:
    1. next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
    2. You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
// ====================================================================================================================== //
// === 44ms(80.95%) && 24.2MB(100%) === //
typedef struct {
    int stack[100000];
    int size;
    int flag;
} BSTIterator;

void fill(struct TreeNode* root, BSTIterator* obj){
    if(root == NULL){
        return;
    }
    fill(root -> left, obj);
    obj -> stack[obj -> size] = root -> val;
    ++ obj -> size;
    fill(root -> right, obj);
}

BSTIterator* bSTIteratorCreate(struct TreeNode* root) {
    BSTIterator* obj = (BSTIterator*)malloc(sizeof(BSTIterator));
    obj -> flag = 0;
    fill(root, obj);
    return obj;
}

/** @return the next smallest number */
int bSTIteratorNext(BSTIterator* obj) {
    if(obj -> flag < obj -> size){
        int ans = obj -> stack[obj -> flag];
        ++ obj -> flag;
        return ans;
    }
    return -1;
}

/** @return whether we have a next smallest number */
bool bSTIteratorHasNext(BSTIterator* obj) {
    return obj -> flag < obj -> size;
}

void bSTIteratorFree(BSTIterator* obj) {
    free(obj);
}

/**
 * Your BSTIterator struct will be instantiated and called as such:
 * BSTIterator* obj = bSTIteratorCreate(root);
 * int param_1 = bSTIteratorNext(obj);
 
 * bool param_2 = bSTIteratorHasNext(obj);
 
 * bSTIteratorFree(obj);
*/