/*
=== 463. Island Perimeter ===

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
    Input:
    [[0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]
    Output: 16
    Explanation: The perimeter is the 16 yellow stripes in the image below:
*/
int count_edge(int** grid, int gridSize, int* gridColSize, int x, int y){
    if(grid[x][y] == 0){
        return 0;
    }
    int edge = 0;
    if(x == 0 || grid[x-1][y] == 0){
        ++ edge;
    }
    if(x == gridSize-1 || grid[x+1][y] == 0){
        ++ edge;
    }
    if(y == 0 || grid[x][y-1] == 0){
        ++ edge;
    }
    if(y == *gridColSize-1 || grid[x][y+1] == 0){
        ++ edge;
    }
    return edge;
}
// === 72ms(88.68%) && 10.3MB(25%) === //
int islandPerimeter(int** grid, int gridSize, int* gridColSize){
    int ans = 0;
    for(int i=0; i<gridSize; ++i){
        for(int j=0; j<*gridColSize; ++j){
            ans += count_edge(grid, gridSize, gridColSize, i, j);
        }
    }
    return ans;
}

