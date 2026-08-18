/*
=== 905. Sort Array By Parity ===

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 
Note:
1. 1 <= A.length <= 5000
2. 0 <= A[i] <= 5000
*/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArrayByParity(int* A, int ASize, int* returnSize) {
    int* ans = (int*)malloc(ASize*sizeof(int));
    *returnSize = ASize;
    int start = 0, end = ASize-1;
    for(int i=0; i<ASize; ++i){
        if(A[i] % 2 == 0){
            ans[start] = A[i];
            ++ start;
        }
        else{
            ans[end] = A[i];
            -- end;
        }
    }
    return ans;
}