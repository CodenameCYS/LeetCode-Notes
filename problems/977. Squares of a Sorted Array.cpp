/*
=== 977. Squares of a Sorted Array ===

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
    Input: [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
Example 2:
    Input: [-7,-3,2,3,11]
    Output: [4,9,9,49,121]
 
Note:
    1. 1 <= A.length <= 10000
    2. -10000 <= A[i] <= 10000
    3. A is sorted in non-decreasing order.
*/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 36 ms === //
int* sortedSquares(int* A, int ASize, int* returnSize) {
    *returnSize = ASize;
    int* ans = (int*)malloc(ASize*sizeof(int));
    int pivot = 0;
    for(int i=1; i<ASize; ++i){
        if(abs(A[i]) > abs(A[pivot])){
            break;
        }
        else{
            pivot = i;
        }
    }
    ans[0] = A[pivot]*A[pivot];
    int negloc = pivot-1;
    int posloc = pivot+1;
    for(int i=1; i<ASize; ++i){
        if(negloc < 0){
            ans[i] = A[posloc]*A[posloc];
            ++posloc;
        }
        else if(posloc >= ASize){
            ans[i] = A[negloc]*A[negloc];
            --negloc;
        }
        else if(abs(A[negloc]) < abs(A[posloc])){
            ans[i] = A[negloc]*A[negloc];
            --negloc;
        }
        else{
            ans[i] = A[posloc]*A[posloc];
            ++posloc;
        }
    }
    return ans;
}