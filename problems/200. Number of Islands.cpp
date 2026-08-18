/*
=== 200. Number of Islands ===

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
*/
# include <stdlib.h>
int TraverseIsland(char** grid, int gridRowSize, int gridColSize, int row, int col){
    int size = 0;
    int maxstacklen = 2500;
    int* rowstack = (int*)malloc(maxstacklen * sizeof(int));
    int* colstack = (int*)malloc(maxstacklen * sizeof(int));
    int stacklen = 0;
    
    rowstack[0] = row,  colstack[0] = col,  stacklen = 1;
    while(stacklen > 0){
        -- stacklen;
        int temprow = rowstack[stacklen],   tempcol = colstack[stacklen];
        if(grid[temprow][tempcol] == '1'){
            grid[temprow][tempcol] = '0';
            ++ size;
        }
        
        if(temprow - 1 >= 0 && grid[temprow-1][tempcol] == '1'){
            rowstack[stacklen] = temprow - 1,   colstack[stacklen] = tempcol;
            ++ stacklen;
        }
        if(temprow + 1 < gridRowSize && grid[temprow+1][tempcol] == '1'){
            rowstack[stacklen] = temprow + 1,   colstack[stacklen] = tempcol;
            ++ stacklen;
        }
        if(tempcol - 1 >= 0 && grid[temprow][tempcol-1] == '1'){
            rowstack[stacklen] = temprow,   colstack[stacklen] = tempcol - 1;
            ++ stacklen;
        }
        if(tempcol + 1 < gridColSize && grid[temprow][tempcol+1] == '1'){
            rowstack[stacklen] = temprow,   colstack[stacklen] = tempcol + 1;
            ++ stacklen;
        }
    }
    
    free(rowstack);
    free(colstack);
    return size;
}
// === beat 100% === //
int numIslands(char** grid, int gridRowSize, int gridColSize) {
    int ans = 0;
    
    for(int row=0; row<gridRowSize; ++row){
        for(int col=0; col<gridColSize; ++col){
            if(grid[row][col] == '1'){
                ++ ans;
                TraverseIsland(grid, gridRowSize, gridColSize, row, col);
            }
        }
    }
    
    return ans;
}