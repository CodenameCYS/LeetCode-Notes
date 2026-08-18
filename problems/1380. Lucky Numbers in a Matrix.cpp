/*
=== 1380. Lucky Numbers in a Matrix ===

Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
    Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
    Output: [15]
    Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:
    Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    Output: [12]
    Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:
    Input: matrix = [[7,8],[1,2]]
    Output: [7]
 
Constraints:
    1. m == mat.length
    2. n == mat[i].length
    3. 1 <= n, m <= 50
    4. 1 <= matrix[i][j] <= 10^5.
    5. All elements in the matrix are distinct.
*/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void find_lucky_number(int** matrix, int RowSize, int ColSize, int row, int* ans, int* returnSize){
    int col = 0;
    for(int j=1; j<ColSize; ++j){
        if(matrix[row][j] < matrix[row][col]){
            col = j;
        }
    }
    for(int i=0; i<RowSize; ++i){
        if(matrix[i][col] > matrix[row][col]){
            return;
        }
    }
    ans[*returnSize] = matrix[row][col];
    ++ *returnSize;
}
// === 20ms && 6.3MB === //
int* luckyNumbers (int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    *returnSize = 0;
    if(matrixSize == 0 || *matrixColSize == 0){
        return NULL;
    }
    int maxsize = matrixSize < *matrixColSize ? matrixSize : *matrixColSize;
    int* ans = (int*)malloc(maxsize * sizeof(int));
    for(int i=0; i<matrixSize; ++i){
        find_lucky_number(matrix, matrixSize, *matrixColSize, i, ans, returnSize);
    }
    return ans;
}

