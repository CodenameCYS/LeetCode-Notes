/*
=== 1252. Cells with Odd Values in a Matrix ===

Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.
Return the number of cells with odd values in the matrix after applying the increment to all indices.
 
Example 1:
    Input: n = 2, m = 3, indices = [[0,1],[1,1]]
    Output: 6
    - Explanation: Initial matrix = [[0,0,0],[0,0,0]].
    After applying first increment it becomes [[1,2,1],[0,1,0]].
    The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
Example 2:
    Input: n = 2, m = 2, indices = [[1,1],[0,0]]
    Output: 0
    - Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
    
Constraints:
    1. 1 <= n <= 50
    2. 1 <= m <= 50
    3. 1 <= indices.length <= 100
    4. 0 <= indices[i][0] < n
    5. 0 <= indices[i][1] < m
*/
// === 4ms(87.10%) & 7.1MB === //
int oddCells(int n, int m, int** indices, int indicesSize, int* indicesColSize){
    int cells[n][m];
    for(int i=0; i<n; ++i){
        for(int j=0; j<m; ++j){
            cells[i][j] = 0;
        }
    }
    for(int i=0; i<indicesSize; ++i){
        int r=indices[i][0], c=indices[i][1];
        for(int j=0; j<n; ++j){
            ++ cells[j][c];
        }
        for(int j=0; j<m; ++j){
            ++ cells[r][j];
        }
    }
    int ans = 0;
    for(int i=0; i<n; ++i){
        for(int j=0; j<m; ++j){
            if(cells[i][j] % 2 == 1){
                ++ ans;
            }
        }
    }
    return ans;
}

