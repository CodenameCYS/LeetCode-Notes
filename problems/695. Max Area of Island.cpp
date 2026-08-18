/*
=== 695. Max Area of Island ===

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
*/
# include <stdlib.h>
int TraverseIsland(int** grid, int gridRowSize, int gridColSize, int row, int col){
    int size = 0;
    int maxstacklen = 2500;
    int* rowstack = (int*)malloc(maxstacklen * sizeof(int));
    int* colstack = (int*)malloc(maxstacklen * sizeof(int));
    int stacklen = 0;
    
    rowstack[0] = row,  colstack[0] = col,  stacklen = 1;
    while(stacklen > 0){
        -- stacklen;
        int temprow = rowstack[stacklen],   tempcol = colstack[stacklen];
        if(grid[temprow][tempcol] == 1){
            grid[temprow][tempcol] = 0;
            ++ size;
        }
        
        if(temprow - 1 >= 0 && grid[temprow-1][tempcol] == 1){
            rowstack[stacklen] = temprow - 1,   colstack[stacklen] = tempcol;
            ++ stacklen;
        }
        if(temprow + 1 < gridRowSize && grid[temprow+1][tempcol] == 1){
            rowstack[stacklen] = temprow + 1,   colstack[stacklen] = tempcol;
            ++ stacklen;
        }
        if(tempcol - 1 >= 0 && grid[temprow][tempcol-1] == 1){
            rowstack[stacklen] = temprow,   colstack[stacklen] = tempcol - 1;
            ++ stacklen;
        }
        if(tempcol + 1 < gridColSize && grid[temprow][tempcol+1] == 1){
            rowstack[stacklen] = temprow,   colstack[stacklen] = tempcol + 1;
            ++ stacklen;
        }
    }
    
    free(rowstack);
    free(colstack);
    return size;
}
// === beat 96.15% === //
int maxAreaOfIsland(int** grid, int gridRowSize, int gridColSize) {
    int maxsize = 0;
    
    for(int row=0; row<gridRowSize; ++row){
        for(int col=0; col<gridColSize; ++col){
            if(grid[row][col] == 1){
                int size = TraverseIsland(grid, gridRowSize, gridColSize, row, col);
                // printf("%d\t", size);
                maxsize = maxsize > size ? maxsize : size;
            }
        }
    }
    
    return maxsize;
}