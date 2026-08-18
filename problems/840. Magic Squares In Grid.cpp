/*
=== 840. Magic Squares In Grid ===

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:
    Input: [[4,3,8,4],
            [9,5,1,9],
            [2,7,6,2]]
    Output: 1
    Explanation: 
    The following subgrid is a 3 x 3 magic square:
        438
        951
        276
    while this one is not:
        384
        519
        762
    In total, there is only one magic square inside the given grid.

Note:
    1. 1 <= grid.length <= 10
    2. 1 <= grid[0].length <= 10
    3. 0 <= grid[i][j] <= 15
*/
bool is_magic_square(int** grid, int i, int j){
    int counter[16] = {0};
    for(int x=i; x<i+3; ++x){
        for(int y=j; y<j+3; ++y){
            counter[grid[x][y]] = 1;
        }
    }
    for(int k=1; k<10; ++k){
        if(counter[k] != 1){
            return false;
        }
    }
    return grid[i][j] + grid[i][j+1] + grid[i][j+2] == 15 &&
        grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] == 15 &&
        grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] == 15 &&
        grid[i][j] + grid[i+1][j] + grid[i+2][j] == 15 &&
        grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] == 15 &&
        grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] == 15 &&
        grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == 15 &&
        grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] == 15;
}
// === 0ms(100%) && 5.2MB(100%) === //
int numMagicSquaresInside(int** grid, int gridSize, int* gridColSize){
    int ans = 0;
    for(int i=0; i<gridSize-2; ++i){
        for(int j=0; j<gridColSize[0]-2; ++j){
            if(is_magic_square(grid, i, j)){
                ++ ans;
            }
        }
    }
    return ans;
}