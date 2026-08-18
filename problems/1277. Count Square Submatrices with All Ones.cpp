/*
=== 1277. Count Square Submatrices with All Ones ===

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
    Input: matrix =
    [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]
    Output: 15
    - Explanation: 
    There are 10 squares of side 1.
    There are 4 squares of side 2.
    There is  1 square of side 3.
    Total number of squares = 10 + 4 + 1 = 15.
Example 2:
    Input: matrix = 
    [
        [1,0,1],
        [1,1,0],
        [1,1,0]
    ]
    Output: 7
    - Explanation: 
    There are 6 squares of side 1.  
    There is 1 square of side 2. 
    Total number of squares = 6 + 1 = 7.
    
Constraints:
    1. 1 <= arr.length <= 300
    2. 1 <= arr[0].length <= 300
    3. 0 <= arr[i][j] <= 1
*/
// === 336ms && 11.5MB === //
int countSquares(int** matrix, int matrixSize, int* matrixColSize){
    int n = matrixSize;
    int m = matrixColSize[0];
    // printf("%d,%d\n", n, m);
    int sum[n+1][m+1];
    for(int i=0; i<=n; ++i){
        for(int j=0; j<=m; ++j){
            if(i == 0 || j == 0){
                sum[i][j] == 0;
            }
            else{
                sum[i][j] = matrix[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1];
            }
        }
    }
    // printf("=== sum matrix built ===");
    int ans = 0;
    int len = m < n ? m : n;
    for(int l=1; l<=len; ++l){
        for(int i=0; i+l<=n; ++i){
            for(int j=0; j+l<=m; ++j){
                if(sum[i+l][j+l] - sum[i][j+l] - sum[i+l][j] + sum[i][j] == l*l){
                    ++ ans;
                }
            }
        }
    }
    return ans;
}

