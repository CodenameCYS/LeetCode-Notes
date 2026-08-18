/*
=== 1053. Previous Permutation With One Swap ===

Given an array A of positive integers (not necessarily distinct), return the lexicographically largest permutation that is smaller than A, that can be made with one swap (A swap exchanges the positions of two numbers A[i] and A[j]).  If it cannot be done, then return the same array.

Example 1:
    Input: [3,2,1]
    Output: [3,1,2]
    - Explanation: Swapping 2 and 1.
Example 2:
    Input: [1,1,5]
    Output: [1,1,5]
    - Explanation: This is already the smallest permutation.
Example 3:
    Input: [1,9,4,6,7]
    Output: [1,7,4,6,9]
    - Explanation: Swapping 9 and 7.
Example 4:
    Input: [3,1,1,3]
    Output: [1,3,1,3]
    - Explanation: Swapping 1 and 3.

Note:
    1. 1 <= A.length <= 10000
    2. 1 <= A[i] <= 10000
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 76ms && 16.7MB === //
int* prevPermOpt1(int* A, int ASize, int* returnSize){
    int* ans = (int*)malloc(ASize*sizeof(int));
    *returnSize = ASize;
    ans[ASize-1] = A[ASize-1];
    int i=ASize-2;
    for(; i>=0; --i){
        if(A[i] <= A[i+1]){
            ans[i] = A[i];
            continue;
        }
        else{
            for(int j=ASize-1; j>i; --j){
                if(A[j]<A[i]){
                    while(j > i && A[j-1] == A[j]){
                        --j;
                    }
                    ans[j] = A[i];
                    ans[i] = A[j];
                    break;
                }
            }
            --i;
            break;
        }
    }
    for(; i>=0; --i){
        ans[i] = A[i];
    }
    return ans;
}

