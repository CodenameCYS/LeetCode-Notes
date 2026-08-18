/*
=== 216. Combination Sum III ===

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
    1. All numbers will be positive integers.
    2. The solution set must not contain duplicate combinations.

Example 1:
    Input: k = 3, n = 7
    Output: [[1,2,4]]
Example 2:
    Input: k = 3, n = 9
    Output: [[1,2,6], [1,3,5], [2,3,4]]
*/
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void my_combination(int k, int n, int** ans, int* returnSize, int* returnColumnSizes, int* present, int size, int min){
    // printf("%d\t%d\t%d\t%d\t%d :: ", k, n, *returnSize, size, min);
    // for(int i=0; i<size; ++i){
    //     printf("%d ,", present[i]);
    // }
    // printf("\n");
    if(n < k*min + k*(k+1)/2 || n > 10*k-k*(k+1)/2){
        return;
    }
    else if(k == 1 && n <= 9 && n > min){
        ans[*returnSize] = (int*)malloc((size+1)*sizeof(int));
        for(int i=0; i<size; ++i){
            ans[*returnSize][i] = present[i];
        }
        ans[*returnSize][size] = n;
        returnColumnSizes[*returnSize] = size+1;
        ++ *returnSize;
    }
    else{
        for(int i=min+1; i<=10-k; ++i){
            present[size] = i;
            my_combination(k-1, n-i, ans, returnSize, returnColumnSizes, present, size+1, i);
        }
    }
}
// === 4ms(37.5%) && 7.3MB(100%) === //
int** combinationSum3(int k, int n, int* returnSize, int** returnColumnSizes){
    int** ans = (int**)malloc(512*sizeof(int*));
    returnColumnSizes[0] = (int*)malloc(512*sizeof(int));
    *returnSize = 0;
    int present[k], size=0;
    my_combination(k, n, ans, returnSize, returnColumnSizes[0], present, size, 0);
    return ans;
}

