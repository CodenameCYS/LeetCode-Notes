/*
=== 1260. Shift 2D Grid ===

Given a 2D grid of size n * m and an integer k. You need to shift the grid k times.
In one shift operation:
    - Element at grid[i][j] becomes at grid[i][j + 1].
    - Element at grid[i][m - 1] becomes at grid[i + 1][0].
    - Element at grid[n - 1][m - 1] becomes at grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
    Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:
    Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
    Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:
    Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
    Output: [[1,2,3],[4,5,6],[7,8,9]]
 
Constraints:
    1. 1 <= grid.length <= 50
    2. 1 <= grid[i].length <= 50
    3. -1000 <= grid[i][j] <= 1000
    4. 0 <= k <= 100
*/
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
// === 64ms & 15.6MB === //
int** shiftGrid(int** grid, int gridSize, int* gridColSize, int k, int* returnSize, int** returnColumnSizes){
    int** ans = (int**)malloc(gridSize*sizeof(int*));
    *returnSize = gridSize;
    *returnColumnSizes = (int *)malloc(gridSize*sizeof(int));
    int n = gridSize, m = gridColSize[0];
    for(int i=0; i<gridSize; ++i){
        returnColumnSizes[0][i] = m;
        ans[i] = (int*)malloc(m * sizeof(int));
    }
    k = k % (m*n);
    for(int i=0; i<n; ++i){
        for(int j=0; j<m; ++j){
            int flag = (m*i+j+k) % (n*m);
            int x = flag / m, y = flag % m;
            ans[x][y] = grid[i][j];
        }
    }
    return ans;
}

