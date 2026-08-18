/*
=== 888. Fair Candy Swap ===

Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.
Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)
Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.
If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

Example 1:
Input: A = [1,1], B = [2,2]
Output: [1,2]

Example 2:
Input: A = [1,2], B = [2,3]
Output: [1,2]

Example 3:
Input: A = [2], B = [1,3]
Output: [2,3]

Example 4:
Input: A = [1,2,5], B = [2,4]
Output: [5,4]
 
Note:
1. 1 <= A.length <= 10000
2. 1 <= B.length <= 10000
3. 1 <= A[i] <= 100000
4. 1 <= B[i] <= 100000
5. It is guaranteed that Alice and Bob have different total amounts of candy.
6. It is guaranteed there exists an answer.
*/
# include <stdlib.h>
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
void QuickSort(int* arr, int start, int end){
    if(start >= end){
        return;
    }
    int i = start, j= end;
    int temp = arr[start];
    while(i < j){
        while(i < j && arr[j] >= temp){
            -- j;
        }
        if(i < j){
            arr[i] = arr[j];
            ++ i;
        }
        while(i < j && arr[i] <= temp){
            ++ i;
        }
        if(i < j){
            arr[j] = arr[i];
            -- j;
        }
    }
    arr[i] = temp;
    QuickSort(arr, start, i-1);
    QuickSort(arr, i+1, end);
}

int* fairCandySwap(int* A, int ASize, int* B, int BSize, int* returnSize) {
    int* ans = (int*)malloc(2*sizeof(int));
    *returnSize = 2;
    // printf("=== cal delta ===");
    long sumA = 0,  sumB = 0;
    for(int i=0; i<ASize; ++i){
        sumA += A[i];
    }
    for(int i=0; i<BSize; ++i){
        sumB += B[i];
    }
    int delta = (sumA + sumB)/2 - sumA;
    // printf("=== begin quick sort ===\n");
    QuickSort(A, 0, ASize-1);
    QuickSort(B, 0, BSize-1);
    
    int j = 0;
    for(int i=0; i<ASize; ++i){
        if(A[i] + delta <= 0){
            continue;
        }
        while(B[j] < A[i] + delta){
            ++ j;
        }
        if(B[j] == A[i] + delta){
            ans[0] = A[i];
            ans[1] = B[j];
            return ans;
        }
    }
    return ans;
}