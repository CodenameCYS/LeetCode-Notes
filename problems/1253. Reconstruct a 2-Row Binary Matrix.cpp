/*
=== 1253. Reconstruct a 2-Row Binary Matrix ===

Given the following details of a matrix with n columns and 2 rows :
    - The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
    - The sum of elements of the 0-th(upper) row is given as upper.
    - The sum of elements of the 1-st(lower) row is given as lower.
    - The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
Your task is to reconstruct the matrix with upper, lower and colsum.
Return it as a 2-D integer array.
If there are more than one valid solution, any of them will be accepted.
If no valid solution exists, return an empty 2-D array.

Example 1:
    Input: upper = 2, lower = 1, colsum = [1,1,1]
    Output: [[1,1,0],[0,0,1]]
    - Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
Example 2:
    Input: upper = 2, lower = 3, colsum = [2,2,1,1]
    Output: []
Example 3:
    Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
    Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
 
Constraints:
    1. 1 <= colsum.length <= 10^5
    2. 0 <= upper, lower <= colsum.length
    3. 0 <= colsum[i] <= 2
*/
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
// === 236ms(71.43%) && 36.6MB === //
int** reconstructMatrix(int upper, int lower, int* colsum, int colsumSize, int* returnSize, int** returnColumnSizes){
    int n0=0, n1=0, n2=0;
    for(int i=0; i<colsumSize; ++i){
        if(colsum[i] == 0){
            ++ n0;
        }
        else if(colsum[i] == 1){
            ++ n1;
        }
        else{
            ++ n2;
        }
    }
    if(upper+lower!=2*n2+n1 || upper>colsumSize || lower>colsumSize || upper<n2 || lower<n2){
        int** ans=NULL;
        *returnSize=0;
        **returnColumnSizes=NULL;
        return ans;
    }
    
    *returnSize = 2;
    int** ans = (int**)malloc(2*sizeof(int*));
    ans[0] = (int*)malloc(colsumSize * sizeof(int));
    ans[1] = (int*)malloc(colsumSize * sizeof(int));
    *returnColumnSizes = (int*)malloc(2*sizeof(int));
    returnColumnSizes[0][0] = colsumSize;
    returnColumnSizes[0][1] = colsumSize;
    
    int upnum = upper-n2;
    int count = 0;
    for(int i=0; i<colsumSize; ++i){
        if(colsum[i] == 0){
            ans[0][i] = 0;
            ans[1][i] = 0;
        }
        else if(colsum[i] == 2){
            ans[0][i] = 1;
            ans[1][i] = 1;
        }
        else if(count < upnum){
            ans[0][i] = 1;
            ans[1][i] = 0;
            ++ count;
        }
        else{
            ans[0][i] = 0;
            ans[1][i] = 1;
            ++ count;
        }
    }
    return ans;
}

