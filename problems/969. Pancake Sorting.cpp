/*
=== 969. Pancake Sorting ===

Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.
Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

Example 1:
    Input: [3,2,4,1]
    Output: [4,2,4,3]
Explanation: 
    We perform 4 pancake flips, with k values 4, 2, 4, and 3.
    Starting state: A = [3, 2, 4, 1]
    After 1st flip (k=4): A = [1, 4, 2, 3]
    After 2nd flip (k=2): A = [4, 1, 2, 3]
    After 3rd flip (k=4): A = [3, 2, 1, 4]
    After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
Example 2:
    Input: [1,2,3]
    Output: []
Explanation: 
    The input is already sorted, so there is no need to flip anything.
    Note that other answers, such as [3, 3], would also be accepted.
 
Note:
    1. 1 <= A.length <= 100
    2. A[i] is a permutation of [1, 2, ..., A.length]
*/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 4ms === //
void myreverse(int* A, int size){
    for(int i=0; i<=size/2; ++i){
        int temp = A[i];
        A[i] = A[size-i];
        A[size-i] = temp;
    }
}
int* pancakeSort(int* A, int ASize, int* returnSize) {
    int* ans = (int*)malloc(2*ASize*sizeof(int));
    *returnSize = 0;
    for(int i=ASize; i>0; --i){
        for(int j=0; j<i; ++j){
            if(A[j] == i){
                // printf("%d\t%d\n", j, i);
                if(j != i-1){
                    if(j != 0){
                        myreverse(A, j);
                        ans[*returnSize] = j+1;
                        *returnSize += 1;
                    }
                    if(i-1 != 0){
                        myreverse(A, i-1);
                        ans[*returnSize] = i;
                        *returnSize += 1;
                    }
                }
                /*
                for(int i=0; i<ASize; ++i){
                    printf("%d\t", A[i]);
                }
                printf("\n");
                */
                break;
            }
        }
    }
    return ans;
}