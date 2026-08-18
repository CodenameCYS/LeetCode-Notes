/*
=== 889. Spiral Matrix III ===

On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.
Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.
Now, we walk in a clockwise spiral shape to visit every position in this grid. 
Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.) 
Eventually, we reach all R * C spaces of the grid.
Return a list of coordinates representing the positions of the grid in the order they were visited.


Example 1:
Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:
Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]


Note:
1. 1 <= R <= 100
2. 1 <= C <= 100
3. 0 <= r0 < R
4. 0 <= c0 < C
*/
# include <stdlib.h>
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int calRuntime(int R, int C, int r0, int c0){
    int max1 = r0 > R-r0 ? r0 : R-r0;
    int max2 = c0 > C-c0 ? c0 : C-c0;
    return max1 > max2 ? max1 : max2;
}
void Traverse(int R, int C, int r0, int c0, int* columnSizes, int* returnSize, int** ans, int runtime){
    if(runtime == 0){
        ans[*returnSize] = (int*)malloc(2*sizeof(int));
        ans[*returnSize][0] = r0;
        ans[*returnSize][1] = c0;
        columnSizes[*returnSize] = 2;
        ++ *returnSize;
        return;
    }
    int row = r0 - runtime + 1;
    int col = c0 + runtime;
    for(int i=0; i<2*runtime; ++i){
        if(row>=0 && row<R && col>=0 && col<C){
            ans[*returnSize] = (int*)malloc(2*sizeof(int));
            ans[*returnSize][0] = row;
            ans[*returnSize][1] = col;
            columnSizes[*returnSize] = 2;
            ++ *returnSize;
        }
        if(i != 2*runtime-1){
            ++ row;
        }
        else{
            -- col;
        }
    }
    for(int i=0; i<2*runtime; ++i){
        if(row>=0 && row<R && col>=0 && col<C){
            ans[*returnSize] = (int*)malloc(2*sizeof(int));
            ans[*returnSize][0] = row;
            ans[*returnSize][1] = col;
            columnSizes[*returnSize] = 2;
            ++ *returnSize;
        }
        if(i != 2*runtime-1){
            -- col;
        }
        else{
            -- row;
        }
    }
    for(int i=0; i<2*runtime; ++i){
        if(row>=0 && row<R && col>=0 && col<C){
            ans[*returnSize] = (int*)malloc(2*sizeof(int));
            ans[*returnSize][0] = row;
            ans[*returnSize][1] = col;
            columnSizes[*returnSize] = 2;
            ++ *returnSize;
        }
        if(i != 2*runtime-1){
            -- row;
        }
        else{
            ++ col;
        }
    }
    for(int i=0; i<2*runtime; ++i){
        if(row>=0 && row<R && col>=0 && col<C){
            ans[*returnSize] = (int*)malloc(2*sizeof(int));
            ans[*returnSize][0] = row;
            ans[*returnSize][1] = col;
            columnSizes[*returnSize] = 2;
            ++ *returnSize;
        }
        if(i != 2*runtime-1){
            ++ col;
        }
        else{
            -- row;
        }
    }
}
int** spiralMatrixIII(int R, int C, int r0, int c0, int** columnSizes, int* returnSize) {
    int runtime = calRuntime(R, C, r0, c0);
    // printf("need to traverse %d times\n",runtime);
    int** ans = (int**)malloc(R*C*sizeof(int*));
    *columnSizes = (int*)malloc(R*C*sizeof(int));
    *returnSize = 0;
    for(int i=0; i<=runtime; ++i){
        Traverse(R, C, r0, c0, *columnSizes, returnSize, ans, i);
    }
    return ans;
}