/*
=== 892. Surface Area of 3D Shapes ===

On a N * N grid, we place some 1 * 1 * 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Return the total surface area of the resulting shapes.

Example 1:
Input: [[2]]
Output: 10

Example 2:
Input: [[1,2],[3,4]]
Output: 34

Example 3:
Input: [[1,0],[0,2]]
Output: 16

Example 4:
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 5:
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 
Note:
1. 1 <= N <= 50
2. 0 <= grid[i][j] <= 50
*/
# include <stdlib.h>
# include <stdio.h>
# include <math.h>

int surfaceArea(int** grid, int gridRowSize, int *gridColSizes) {
    int ans = 2 * gridRowSize * gridRowSize;
    for(int i=0; i<gridRowSize; ++i){
        int colnow = 0;
        int rownow = 0;
        for(int j=0; j<gridColSizes[i]; ++j){
            ans += abs(grid[i][j] - colnow);
            ans += abs(grid[j][i] - rownow);
            colnow = grid[i][j];
            rownow = grid[j][i];
            if(grid[i][j] == 0){
                ans -= 2;
            }
        }
        ans += colnow;
        ans += rownow;
    }
    return ans;
}