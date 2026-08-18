/*
=== 1104. Path In Zigzag Labelled Binary Tree ===

In an infinite binary tree where every node has two children, the nodes are labelled in row order.
In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.
Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

Example 1:
    Input: label = 14
    Output: [1,3,4,14]
Example 2:
    Input: label = 26
    Output: [1,2,6,10,26]
 
Constraints:
    1. 1 <= label <= 10^6
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 0ms & 7MB === //
int* pathInZigZagTree(int label, int* returnSize){
    *returnSize = (int)(log(label)/log(2.0)) + 1;
    int* ans = (int*)malloc(*returnSize*sizeof(int));
    int rev = (1.5*pow(2, *returnSize)-1-label)/2;
    // printf("rev = %d\n", rev);
    for(int i=*returnSize-1; i>=0; i-=2){
        ans[i] = label;
        label /= 4;
    }
    for(int i=*returnSize-2; i>=0; i-=2){
        ans[i] = rev;
        rev /= 4;
    }
    return ans;
}