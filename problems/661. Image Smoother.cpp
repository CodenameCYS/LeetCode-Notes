/*
=== 661. Image Smoother ===

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
    Input:
    [[1,1,1],
    [1,0,1],
    [1,1,1]]
    Output:
    [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]
    Explanation:
    For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
    For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
    For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
    1. The value in the given matrix is in the range of [0, 255].
    2. The length and width of the given matrix are in the range of [1, 150].
*/
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int fill(int** M, int MSize, int* MColSize, int row, int col){
    int sum=0, tot=0;
    for(int i=row-1; i<=row+1; ++i){
        if(i<0 || i>=MSize){
            continue;
        }
        for(int j=col-1; j<=col+1; ++j){
            if(j<0 || j>=*MColSize){
                continue;
            }
            sum += M[i][j];
            ++ tot;
        }
    }
    return sum / tot;
}
// === 136ms(51.61%) && 20.5MB(100%) === //
int** imageSmoother(int** M, int MSize, int* MColSize, int* returnSize, int** returnColumnSizes){
    int** ans = (int**)malloc(MSize * sizeof(int*));
    *returnColumnSizes = (int*)malloc(MSize * sizeof(int));
    *returnSize = MSize;
    for(int i=0; i<MSize; ++i){
        ans[i] = (int*)malloc(*MColSize*sizeof(int));
        returnColumnSizes[0][i] = *MColSize;
        for(int j=0; j<*MColSize; ++j){
            ans[i][j] = fill(M, MSize, MColSize, i, j);
        }
    }
    return ans;
}

