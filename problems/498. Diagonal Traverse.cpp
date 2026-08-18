/*
=== 498. Diagonal Traverse ===

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
    Input:
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    Output:  [1,2,4,7,5,3,6,8,9]

Note:
    1. The total number of elements of the given matrix will not exceed 10,000.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// === 64ms(100%) && 15.8MB(100%) === //
int* findDiagonalOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    if(matrixSize == 0){
        *returnSize = 0;
        return NULL;
    }
    int* ans = (int*)malloc(*matrixColSize * matrixSize * sizeof(int));
    *returnSize = 0;
    int row=0, col=0;
    while(row < matrixSize && col < *matrixColSize){
        while(row < matrixSize && col < *matrixColSize && col >= 0 && row >= 0){
            ans[*returnSize] = matrix[row][col];
            ++ *returnSize;
            -- row;
            ++ col;
        }
        if(col == *matrixColSize){
            row += 2;
            -- col;
        }
        else{
            ++ row;
        }
        while(row < matrixSize && col < *matrixColSize && col >= 0 && row >= 0){
            ans[*returnSize] = matrix[row][col];
            ++ *returnSize;
            ++ row;
            -- col;
        }
        if(row == matrixSize){
            col += 2;
            -- row;
        }
        else{
            ++ col;
        }
    }
    return ans;
}

