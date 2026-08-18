/*
=== 1267. Count Servers that Communicate ===

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
Return the number of servers that communicate with any other server.

Example 1:
    Input: grid = [[1,0],[0,1]]
    Output: 0
    - Explanation: No servers can communicate with others.
Example 2:
    Input: grid = [[1,0],[1,1]]
    Output: 3
    - Explanation: All three servers can communicate with at least one other server.
Example 3:
    Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
    Output: 4
    - Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 
Constraints:
    1. m == grid.length
    2. n == grid[i].length
    3. 1 <= m <= 250
    4. 1 <= n <= 250
    5. grid[i][j] == 0 or 1
*/
// === 76ms && 11.1MB === //
int countServers(int** grid, int gridSize, int* gridColSize){
    int m=gridSize, n=gridColSize[0];
    int rows[m], cols[n];
    int ans = 0;
    for(int i=0; i<m; ++i){
        rows[i] = 0;
        for(int j=0; j<n; ++j){
            rows[i] += grid[i][j];
        }
        if(rows[i] > 1){
            ans += rows[i];
        }
    }
    // printf("%d\n", ans);
    for(int i=0; i<n; ++i){
        cols[i] = 0;
        for(int j=0; j<m; ++j){
            cols[i] += grid[j][i];
        }
        if(cols[i] > 1){
            ans += cols[i];
        }
    }
    // printf("%d\n", ans);
    for(int i=0; i<m; ++i){
        for(int j=0; j<n; ++j){
            if(grid[i][j] == 1 && rows[i] > 1 && cols[j] > 1){
                -- ans;
            }
        }
    }
    // printf("%d\n", ans);
    return ans;
}

