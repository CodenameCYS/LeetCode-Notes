/*
=== 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold ===

Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

Example 1:
    Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
    Output: 2
    - Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:
    Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
    Output: 0
Example 3:
    Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
    Output: 3
Example 4:
    Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
    Output: 2
 
Constraints:
    1. 1 <= m, n <= 300
    2. m == mat.length
    3. n == mat[i].length
    4. 0 <= mat[i][j] <= 10000
    5. 0 <= threshold <= 10^5
*/
// === 148ms && 12.8MB === //
int maxSideLength(int** mat, int matSize, int* matColSize, int threshold){
    int m = matSize, n = matColSize[0];
    int cumsum[m+1][n+1];
    for(int i=0; i<=m; ++i){
        for(int j=0; j<=n; ++j){
            if(i*j == 0){
                cumsum[i][j] = 0;
            }
            else{
                cumsum[i][j] = mat[i-1][j-1] + cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1];
            }
            // printf("%d ", cumsum[i][j]);
        }
        // printf("\n");
    }
    int ans = 0;
    int min = m < n ? m : n;
    for(int k=1; k<=min; ++k){
        int tmp = 0;
        for(int i=0; i+k<=m; ++i){
            for(int j=0; j+k<=n; ++j){
                if(cumsum[i+k][j+k] + cumsum[i][j] - cumsum[i+k][j] - cumsum[i][j+k] <= threshold){
                    ++ tmp;
                }
            }
        }
        if(tmp > 0){
            ans = k;
        }
        else{
            break;
        }
    }
    return ans;
}

