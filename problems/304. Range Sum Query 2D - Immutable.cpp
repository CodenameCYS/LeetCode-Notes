/*
=== 304. Range Sum Query 2D - Immutable ===

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
    Given matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    sumRegion(2, 1, 4, 3) -> 8
    sumRegion(1, 1, 2, 2) -> 11
    sumRegion(1, 2, 2, 4) -> 12

Note:
    1. You may assume that the matrix does not change.
    2. There are many calls to sumRegion function.
    3. You may assume that row1 ≤ row2 and col1 ≤ col2.
*/
// === 16ms(50%) & 11.8MB(100%) === //
typedef struct {
    int rowsize, colsize;
    int** matrix;
} NumMatrix;

NumMatrix* numMatrixCreate(int** matrix, int matrixRowSize, int matrixColSize) {
    NumMatrix* obj = (NumMatrix*)malloc(sizeof(NumMatrix));
    obj->rowsize = matrixRowSize;
    obj->colsize = matrixColSize;
    if(matrixRowSize==0 || matrixColSize==0){
        obj->matrix=NULL;
    }
    else{
        obj->matrix = (int**)malloc(matrixRowSize*sizeof(int*));
        (obj->matrix)[0] = (int*)malloc(matrixColSize*sizeof(int));
        (obj->matrix)[0][0] = matrix[0][0];
        for(int i=1; i<matrixColSize; ++i){
            (obj->matrix)[0][i] = (obj->matrix)[0][i-1]+matrix[0][i];
        }
        for(int i=1; i<matrixRowSize; ++i){
            (obj->matrix)[i] = (int*)malloc(matrixColSize*sizeof(int));
            (obj->matrix)[i][0] = (obj->matrix)[i-1][0] + matrix[i][0];
            for(int j=1; j<matrixColSize; ++j){
                (obj->matrix)[i][j] = (obj->matrix)[i-1][j]+(obj->matrix)[i][j-1]
                    -(obj->matrix)[i-1][j-1]+matrix[i][j];
            }
        }
    }
    return obj;
}

int numMatrixSumRegion(NumMatrix* obj, int row1, int col1, int row2, int col2) {
    if(row1==0 && col1==0){
        return (obj->matrix)[row2][col2];
    }
    else if(row1==0){
        return (obj->matrix)[row2][col2]-(obj->matrix)[row2][col1-1];
    }
    else if(col1==0){
        return (obj->matrix)[row2][col2]-(obj->matrix)[row1-1][col2];
    }
    else{
        return (obj->matrix)[row2][col2]-(obj->matrix)[row1-1][col2]
            -(obj->matrix)[row2][col1-1]+(obj->matrix)[row1-1][col1-1];
    }
}

void numMatrixFree(NumMatrix* obj) {
    for(int i=0; i<obj->rowsize; ++i){
        free((obj->matrix)[i]);
    }
    free(obj->matrix);
    free(obj);
}

/**
 * Your NumMatrix struct will be instantiated and called as such:
 * struct NumMatrix* obj = numMatrixCreate(matrix, matrixRowSize, matrixColSize);
 * int param_1 = numMatrixSumRegion(obj, row1, col1, row2, col2);
 * numMatrixFree(obj);
 */