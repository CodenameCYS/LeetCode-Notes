/*
=== 1351. Count Negative Numbers in a Sorted Matrix= ===

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
Return the number of negative numbers in grid.

Example 1:
    Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.
Example 2:
    Input: grid = [[3,2],[1,0]]
    Output: 0
Example 3:
    Input: grid = [[1,-1],[-1,-1]]
    Output: 3
Example 4:
    Input: grid = [[-1]]
    Output: 1
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m, n <= 100
    4. -100 <= grid[i][j] <= 100
*/
// === 20ms && 8.1MB === //
int countNegatives(int** grid, int gridSize, int* gridColSize){
    int pos = 0;
    for(int i=0; i<gridSize; ++i){
        if(grid[i][0] < 0){
            break;
        }
        for(int j=0; j<*gridColSize && grid[i][j] >= 0; ++j){
            ++ pos;
        }
    }
    return gridSize * *gridColSize - pos;
}

